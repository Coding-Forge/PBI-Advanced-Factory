"""
Generates the CSAM-facing "Exercise Cloud Coverage Matrix" PDF.

Cross-references every hands-on exercise across the 11 training modules against
Azure Commercial, Azure Government (GCC High), and Azure DoD delivery, using a
three-state status per cloud:

  READY        - Runs as-is in this cloud today.
  VERIFY       - May work, but the instructor must confirm in the target tenant
                 before relying on it (licensing, region, preview status, capacity).
  NOT COVERED  - Not expected to be available; deliver conceptually or use the
                 documented alternate exercise instead.

Usage:
    python generate_matrix.py
"""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

READY = "READY"
VERIFY = "VERIFY"
NONE_ = "NOT COVERED"

# (module_num, module_name, [(exercise, commercial, gov, dod, note), ...])
MATRIX = [
    ("01", "Advanced Semantic Modeling", [
        ("Build a star schema from a flat sales dataset", READY, READY, READY, ""),
        ("Refactor a weak model into fact/dimension tables", READY, READY, READY, ""),
        ("Add role-playing date dimensions", READY, READY, READY, ""),
        ("Compare Import, DirectQuery, and composite models", READY, VERIFY, VERIFY, "Validate connector/gateway support in tenant"),
        ("Hybrid tables & advanced incremental refresh", READY, VERIFY, VERIFY, "Requires Premium/PPU/Fabric capacity validation"),
        ("Large semantic model handling", READY, VERIFY, VERIFY, "Capacity/licensing dependent"),
    ]),
    ("02", "Advanced DAX", [
        ("Diagnose incorrect totals from context misunderstanding", READY, READY, READY, ""),
        ("Build a measure branching pattern", READY, READY, READY, ""),
        ("Create advanced time intelligence measures", READY, READY, READY, ""),
        ("Build dynamic Top N / ranking visuals", READY, READY, READY, ""),
        ("Optimize slow measures with variables", READY, READY, READY, ""),
        ("DAX Studio external tool session", READY, VERIFY, VERIFY, "Local tool; Service/XMLA access depends on tenant policy"),
    ]),
    ("03", "Advanced Power Query", [
        ("Build a staged Power Query pipeline", READY, READY, READY, ""),
        ("Prove whether a query folds", READY, READY, READY, ""),
        ("Convert repeated steps into a custom function", READY, READY, READY, ""),
        ("Add parameters for dev/test/prod source switching", READY, READY, READY, ""),
        ("Prepare a table for incremental refresh", READY, READY, VERIFY, "Confirm refresh policy support in DoD capacity"),
        ("Cloud dataflows / Dataflows Gen2", READY, VERIFY, NONE_, "Fabric-dependent; typically unavailable in DoD"),
    ]),
    ("04", "Report Design & UX", [
        ("Add drillthrough from summary to detail", READY, READY, READY, ""),
        ("Build a multi-level hierarchy and drill down/up in a visual", READY, READY, READY, ""),
        ("Configure drill-across between related visuals/pages", READY, READY, READY, ""),
        ("Group and bin field values into custom categories", READY, READY, READY, ""),
        ("Build a bookmark-driven guided analysis", READY, READY, READY, ""),
        ("Create report page tooltips", READY, READY, READY, ""),
        ("Design executive summary + analyst detail pages", READY, READY, READY, ""),
        ("Create a mobile-optimized report layout", READY, READY, VERIFY, "Validate mobile app policy for DoD users"),
        ("Personalized visuals", READY, VERIFY, VERIFY, "Depends on Service feature availability and tenant settings"),
        ("AI-assisted / preview visuals", READY, VERIFY, NONE_, "Often commercial-first; confirm before use"),
    ]),
    ("05", "Performance Optimization", [
        ("Use Performance Analyzer to find slow visuals", READY, READY, READY, ""),
        ("Reduce model size by lowering cardinality", READY, READY, READY, ""),
        ("Use DAX Studio to compare measure performance", READY, VERIFY, VERIFY, "Local tool; Service model access depends on XMLA/tenant"),
        ("Create an aggregation table over DirectQuery", READY, READY, VERIFY, "Validate source/DirectQuery support"),
        ("Configure incremental refresh and test policy", READY, VERIFY, VERIFY, "Licensing/workspace/capacity dependent"),
        ("Capacity metrics review", READY, VERIFY, VERIFY, "Telemetry availability varies by cloud/capacity type"),
    ]),
    ("06", "Advanced Analytics & AI", [
        ("Build a what-if parameter scenario analysis", READY, READY, READY, ""),
        ("Use decomposition tree for driver analysis", READY, NONE_, NONE_, "Not covered in Gov/DoD; treat as Commercial-only"),
        ("Add forecasting to a time-series visual", READY, NONE_, NONE_, "Not covered in Gov/DoD; treat as Commercial-only"),
        ("Key influencers visual", READY, NONE_, NONE_, "Not covered in Gov/DoD; treat as Commercial-only"),
        ("Python/R visuals", READY, NONE_, NONE_, "Not covered in Gov/DoD; treat as Commercial-only"),
        ("Azure Machine Learning integration", READY, NONE_, NONE_, "Not covered in Gov/DoD; treat as Commercial-only"),
        ("Copilot / AI-assisted authoring", READY, NONE_, NONE_, "Treat as conceptual unless confirmed in sovereign tenant"),
    ]),
    ("07", "Security Design", [
        ("Implement static and dynamic RLS", READY, READY, READY, ""),
        ("Test RLS roles in Desktop and Service", READY, READY, READY, ""),
        ("Demonstrate Build permission effects", READY, READY, READY, ""),
        ("Object-level security (OLS)", READY, VERIFY, VERIFY, "Often requires XMLA-compatible tooling and capacity"),
        ("Add sensitivity labels", READY, VERIFY, VERIFY, "Requires Purview Information Protection configuration/cloud support"),
        ("Review export/sharing governance settings", READY, READY, VERIFY, "Confirm B2B/GCC High/DoD sharing policy"),
    ]),
    ("08", "Service Enterprise Deployment", [
        ("Publish a report and semantic model to a workspace", READY, READY, READY, ""),
        ("Configure scheduled refresh and credentials", READY, READY, READY, ""),
        ("Configure a gateway-backed data source", READY, READY, READY, ""),
        ("Create an App with audience targeting", READY, VERIFY, VERIFY, "Confirm Service parity in target cloud"),
        ("Configure deployment pipelines", READY, VERIFY, VERIFY, "Requires compatible licensing/capacity and Service availability"),
        ("Promote/certify a semantic model", READY, READY, VERIFY, "Requires tenant endorsement settings and governance process"),
    ]),
    ("09", "Monitoring & Governance", [
        ("Interpret usage metrics for a deployed report", READY, READY, READY, ""),
        ("Troubleshoot a failed refresh", READY, READY, READY, ""),
        ("Review tenant settings affecting export/sharing", READY, READY, READY, ""),
        ("Inspect gateway status and data source mappings", READY, READY, READY, ""),
        ("Activity logs and audit logs review", READY, VERIFY, VERIFY, "Requires admin permissions and audit configuration"),
        ("Capacity metrics app walkthrough", READY, VERIFY, VERIFY, "Confirm for Premium/Fabric capacity type and cloud"),
        ("Purview integration and DLP policies", READY, VERIFY, NONE_, "Depends on M365/Purview cloud, licensing, tenant config"),
    ]),
    ("10", "Premium, Fabric & Capacity", [
        ("Compare Pro, PPU, Premium, and Fabric capacity", READY, VERIFY, VERIFY, "Validate SKU, tenant, and cloud availability"),
        ("Connect to a semantic model via XMLA endpoint", READY, VERIFY, VERIFY, "Requires compatible capacity and admin settings"),
        ("Publish and manage a paginated report", READY, VERIFY, VERIFY, "Usually supported; validate cloud and licensing"),
        ("Demonstrate Direct Lake / OneLake / Lakehouse concepts", READY, VERIFY, NONE_, "Fabric service parity in sovereign clouds must be confirmed"),
        ("Analyze capacity metrics and autoscale behavior", READY, VERIFY, NONE_, "Validate availability and licensing before including"),
    ]),
    ("11", "Automation & DevOps", [
        ("Save a report as PBIP and review file structure", READY, READY, READY, ""),
        ("Use source control to track report/model changes", READY, READY, READY, ""),
        ("Deploy content using a scripted REST API approach", READY, VERIFY, VERIFY, "Validate endpoint/permission/service principal behavior in target cloud"),
        ("Compare ALM Toolkit changes between model versions", READY, VERIFY, VERIFY, "Local tool; Service connectivity depends on XMLA/tenant policy"),
        ("Git integration in Fabric workspaces", READY, NONE_, NONE_, "Do not require in Gov/DoD labs unless confirmed"),
        ("Conceptual CI/CD pipeline (Azure DevOps/GitHub Actions)", READY, VERIFY, VERIFY, "Depends on network, identity, API endpoint, platform policy"),
    ]),
    ("CAP", "Capstone: Enterprise-Ready Solution", [
        ("Full Gov-ready path (model, DAX, report, RLS, publish, refresh, App)", READY, READY, READY, ""),
        ("Optional: Fabric Git integration, Direct Lake, Copilot, deployment pipelines", READY, VERIFY, NONE_, "Optional commercial-enhanced path only"),
    ]),
]


def status_class(v):
    return {"READY": "s-ready", "VERIFY": "s-verify", "NOT COVERED": "s-none"}[v]


def render_html():
    rows_html = []
    for num, name, exercises in MATRIX:
        rows_html.append(f'<tr class="module-row"><td colspan="5">Module {num} &middot; {name}</td></tr>')
        for exercise, com, gov, dod, note in exercises:
            note_html = f'<div class="note">{note}</div>' if note else ""
            rows_html.append(f"""
            <tr>
              <td class="ex-cell">{exercise}{note_html}</td>
              <td class="stat-cell"><span class="pill {status_class(com)}">{com}</span></td>
              <td class="stat-cell"><span class="pill {status_class(gov)}">{gov}</span></td>
              <td class="stat-cell"><span class="pill {status_class(dod)}">{dod}</span></td>
            </tr>""")
    rows = "\n".join(rows_html)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Exercise Cloud Coverage Matrix</title>
<style>
  @page {{ size: Letter landscape; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    margin: 0;
    color: #1A1A1A;
    background: #F4F6F9;
  }}
  .page {{
    width: 11in;
    height: 8.5in;
    position: relative;
  }}
  .cover {{
    background: linear-gradient(135deg, #0B2545 0%, #13315C 55%, #1E2761 100%);
    color: #fff;
    padding: 0.5in 0.65in;
    height: 8.5in;
    position: relative;
    overflow: hidden;
  }}
  .cover::after {{
    content: "";
    position: absolute;
    right: -100px;
    top: -100px;
    width: 380px;
    height: 380px;
    border-radius: 50%;
    background: #00B4D822;
  }}
  .eyebrow {{
    font-size: 11px;
    letter-spacing: 2.5px;
    font-weight: 700;
    color: #90E0EF;
    margin-bottom: 12px;
  }}
  .cover h1 {{
    font-size: 38px;
    font-weight: 800;
    margin: 0 0 14px 0;
    max-width: 8in;
    line-height: 1.15;
  }}
  .cover .sub {{
    font-size: 15px;
    color: #E7EEF7;
    max-width: 7.5in;
    line-height: 1.6;
    position: relative;
    z-index: 2;
  }}
  .legend-grid {{
    display: flex;
    gap: 16px;
    margin-top: 40px;
    position: relative;
    z-index: 2;
  }}
  .legend-card {{
    flex: 1;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 10px;
    padding: 16px 18px;
  }}
  .legend-card .badge {{
    display: inline-block;
    padding: 5px 12px;
    border-radius: 14px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 10px;
  }}
  .legend-card p {{
    font-size: 11.5px;
    color: #E7EEF7;
    line-height: 1.5;
    margin: 0;
  }}
  .badge-ready {{ background: #2E7D32; }}
  .badge-verify {{ background: #B8860B; }}
  .badge-none {{ background: #757575; }}

  .howto {{
    margin-top: 34px;
    position: relative;
    z-index: 2;
    background: rgba(255,255,255,0.06);
    border-left: 4px solid #00B4D8;
    padding: 14px 18px;
    border-radius: 6px;
    max-width: 8in;
  }}
  .howto div {{ font-size: 12px; color: #E7EEF7; line-height: 1.6; }}
  .howto strong {{ color: #fff; }}

  /* Table pages */
  .table-header {{
    background: #0B2545;
    color: #fff;
    padding: 0.28in 0.5in 0.18in 0.5in;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .table-header h2 {{
    margin: 0;
    font-size: 17px;
    font-weight: 800;
  }}
  .table-header .cols {{
    display: flex;
    gap: 10px;
  }}
  .col-chip {{
    font-size: 9.5px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 12px;
    background: rgba(255,255,255,0.15);
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9.6px;
  }}
  thead th {{
    background: #E9EDF3;
    color: #0B2545;
    text-align: left;
    font-size: 9.5px;
    font-weight: 800;
    padding: 6px 10px;
    border-bottom: 2px solid #C9D3E0;
  }}
  th.stat-cell, td.stat-cell {{ text-align: center; width: 1.15in; }}
  td {{
    padding: 5px 10px;
    border-bottom: 1px solid #E4E7EC;
    vertical-align: top;
  }}
  tr.module-row td {{
    background: #1E2761;
    color: #fff;
    font-weight: 800;
    font-size: 10.5px;
    padding: 6px 10px;
    letter-spacing: 0.3px;
  }}
  .ex-cell {{ font-weight: 600; color: #1A1A1A; }}
  .note {{ font-size: 8.6px; color: #777; font-weight: 400; margin-top: 2px; font-style: italic; }}
  .pill {{
    display: inline-block;
    padding: 2.5px 9px;
    border-radius: 10px;
    font-size: 8.6px;
    font-weight: 800;
    color: #fff;
    min-width: 0.85in;
  }}
  .s-ready {{ background: #2E7D32; }}
  .s-verify {{ background: #B8860B; }}
  .s-none {{ background: #757575; }}

  .footer-bar {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: #0B2545;
    color: #fff;
    font-size: 9px;
    padding: 7px 0.5in;
    display: flex;
    justify-content: space-between;
  }}
  .table-page {{ position: relative; height: 8.5in; padding-bottom: 0.3in; }}
  .table-body-wrap {{ padding: 0 0.5in; }}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="page">
  <div class="cover">
    <div class="eyebrow">CSAM CROSS-CLOUD PLANNING TOOL</div>
    <h1>Advanced Power BI<br>Exercise Cloud Coverage Matrix</h1>
    <div class="sub">Every hands-on exercise across all 11 training modules, cross-filtered against Azure Commercial, Azure Government (GCC High), and Azure DoD delivery &mdash; so a CSAM can scope a customer-ready agenda before the engagement, and instructors know exactly what to verify live in-tenant.</div>

    <div class="legend-grid">
      <div class="legend-card">
        <div class="badge badge-ready">READY</div>
        <p>Runs as-is in this cloud today under normal licensing and tenant settings.</p>
      </div>
      <div class="legend-card">
        <div class="badge badge-verify">VERIFY</div>
        <p>May work, but the instructor must confirm live in the target tenant before relying on it &mdash; licensing, region, preview status, or capacity dependent.</p>
      </div>
      <div class="legend-card">
        <div class="badge badge-none">NOT COVERED</div>
        <p>Not expected to be available in this cloud. Deliver conceptually or substitute the documented alternate exercise.</p>
      </div>
    </div>

    <div class="howto">
      <div><strong>How to use this matrix:</strong> Filter by target cloud to build a customer-specific agenda, flag every VERIFY item for the instructor to confirm in a pre-delivery tenant check, and swap NOT COVERED items for the suggested alternate before finalizing the statement of work.</div>
    </div>
  </div>
</div>

<!-- TABLE PAGES -->
<div class="page">
  <div class="table-page">
    <div class="table-header">
      <h2>Exercise-Level Cloud Coverage</h2>
      <div class="cols">
        <div class="col-chip">COMMERCIAL</div>
        <div class="col-chip">GOVERNMENT (GCC HIGH)</div>
        <div class="col-chip">DOD</div>
      </div>
    </div>
    <div class="table-body-wrap">
      <table>
        <thead>
          <tr>
            <th>Exercise</th>
            <th class="stat-cell">Commercial</th>
            <th class="stat-cell">Government</th>
            <th class="stat-cell">DoD</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>
    <div class="footer-bar">
      <div>Advanced Power BI &middot; Exercise Cloud Coverage Matrix</div>
      <div>For CSAM and instructor planning use</div>
    </div>
  </div>
</div>

</body>
</html>
"""
    return html


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        html = render_html()
        html_path = os.path.join(HERE, "Exercise-Cloud-Coverage-Matrix.html")
        pdf_path = os.path.join(HERE, "Exercise-Cloud-Coverage-Matrix.pdf")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.pdf(path=pdf_path, format="Letter", landscape=True, print_background=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        print(f"Generated {pdf_path}")
        browser.close()


if __name__ == "__main__":
    main()
