# Validate-Pbip.ps1
# Runs known-error checks against a PBIP project before every commit that
# touches .Report or .SemanticModel definition files. Add new checks here
# whenever a new PBIP parse/load error is discovered (see pbip_error_log
# in the session SQL DB for the full history/root-cause notes).
#
# Usage: .\Validate-Pbip.ps1 -ProjectPath "C:\...\pbi-stepwise"

param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath
)

$ErrorActionPreference = "Stop"
$failures = @()

Write-Host "=== Validating PBIP project: $ProjectPath ===" -ForegroundColor Cyan

# --- Check 0: Desktop must be closed before editing/committing PBIP files ---
$pbiProc = Get-Process PBIDesktop -ErrorAction SilentlyContinue
$msmdsrvProc = Get-Process msmdsrv -ErrorAction SilentlyContinue
$lockFiles = Get-ChildItem -Path $ProjectPath -Filter "~$*" -Recurse -ErrorAction SilentlyContinue
if ($pbiProc -or $msmdsrvProc -or $lockFiles) {
    $failures += "Power BI Desktop appears to be open (process and/or lock file found). Close Desktop before committing."
}

# --- Check 1: All JSON files parse ---
$jsonFiles = Get-ChildItem -Path $ProjectPath -Filter "*.json" -Recurse -ErrorAction SilentlyContinue
foreach ($f in $jsonFiles) {
    try {
        $null = Get-Content $f.FullName -Raw | ConvertFrom-Json
    } catch {
        $failures += "INVALID JSON: $($f.FullName) - $($_.Exception.Message)"
    }
}

# --- Check 2: visual.json files must not have filterConfig nested inside "visual", and
#     visualContainerObjects must be nested INSIDE "visual" (sibling of "objects"), not at file root ---
$visualFiles = Get-ChildItem -Path $ProjectPath -Filter "visual.json" -Recurse -ErrorAction SilentlyContinue
foreach ($f in $visualFiles) {
    $raw = Get-Content $f.FullName -Raw
    $obj = $raw | ConvertFrom-Json
    if ($obj.visual.PSObject.Properties.Name -contains 'filterConfig') {
        $failures += "SCHEMA ERROR: 'filterConfig' nested inside 'visual' in $($f.FullName) - must be a sibling of 'visual' at the container root."
    }
    if ($obj.visual.PSObject.Properties.Name -contains 'title') {
        $failures += "SCHEMA ERROR: bare 'title' property found inside 'visual' in $($f.FullName) - title formatting belongs under visual.visualContainerObjects.title, not directly under visual."
    }
    if ($obj.PSObject.Properties.Name -contains 'visualContainerObjects') {
        $failures += "SCHEMA ERROR: 'visualContainerObjects' found at the ROOT of $($f.FullName) - it must be nested INSIDE 'visual' (sibling of 'objects'), e.g. visual.visualContainerObjects.general.altText."
    }
    if ($raw -match '"altText"' -and $raw -notmatch '"visualContainerObjects"') {
        $failures += "SCHEMA ERROR: 'altText' found in $($f.FullName) but no 'visualContainerObjects' present - altText belongs under visual.visualContainerObjects.general.altText, not inside visual.objects.general."
    }
    if ($raw -match '"reportTooltip"') {
        $failures += "SCHEMA ERROR: 'reportTooltip' found in $($f.FullName) - this is not a valid PBIR property. Use visual.visualContainerObjects.visualTooltip with type='ReportPage' and section='<tooltip page name>' instead."
    }
    if ($obj.visual.objects.general.properties.action -or $obj.visual.objects.general.properties.bookmark -or $obj.visual.objects.general.properties.pageNavigation) {
        $failures += "SCHEMA ERROR: button/navigation wiring ('action'/'bookmark'/'pageNavigation') found inside visual.objects.general.properties in $($f.FullName) - must use visual.visualContainerObjects.visualLink with type='Bookmark' (+ 'bookmark') or type='PageNavigation' (+ 'navigationSection') instead."
    }
}

# --- Check 3: lineageTag uniqueness + adjacent-duplicate-line detection across all .tmdl files ---
$tmdlFiles = Get-ChildItem -Path $ProjectPath -Filter "*.tmdl" -Recurse -ErrorAction SilentlyContinue
$allTagLines = @()
foreach ($f in $tmdlFiles) {
    $matches = Select-String -Path $f.FullName -Pattern "lineageTag:\s*(\S+)"
    $allTagLines += $matches
    for ($i = 0; $i -lt $matches.Count - 1; $i++) {
        if ($matches[$i].LineNumber + 1 -eq $matches[$i + 1].LineNumber) {
            $failures += "TMDL DUPLICATE: adjacent lineageTag lines in $($f.FullName) at lines $($matches[$i].LineNumber),$($matches[$i+1].LineNumber) - leftover fragment from an edit."
        }
    }
}
$tagValues = $allTagLines | ForEach-Object { $_.Matches.Groups[1].Value }
$dupTags = $tagValues | Group-Object | Where-Object { $_.Count -gt 1 }
if ($dupTags) {
    foreach ($d in $dupTags) {
        $failures += "TMDL DUPLICATE: lineageTag '$($d.Name)' appears $($d.Count) times across the model (must be globally unique)."
    }
}

# --- Report ---
if ($failures.Count -eq 0) {
    Write-Host "ALL CHECKS PASSED ($($jsonFiles.Count) JSON files, $($tmdlFiles.Count) TMDL files, $($tagValues.Count) lineage tags)." -ForegroundColor Green
    exit 0
} else {
    Write-Host "VALIDATION FAILED - $($failures.Count) issue(s):" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
    exit 1
}
