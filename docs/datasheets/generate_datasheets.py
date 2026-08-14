"""
Generates three branded PDF datasheets (Commercial, Azure Government, Azure DoD)
for the Advanced Power BI training program.

Usage:
    python generate_datasheets.py
"""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

MODULES = [
    ("01", "Advanced Semantic Modeling", "Star schemas, relationships, composite models, aggregations, and large-model design."),
    ("02", "Advanced DAX", "Filter/row context, CALCULATE patterns, time intelligence, ranking, dynamic measures."),
    ("03", "Advanced Power Query", "Query folding, parameters, custom functions, staging patterns, incremental refresh prep."),
    ("04", "Report Design & UX", "Drillthrough, tooltip pages, bookmarks, navigation, field parameters, mobile & accessibility."),
    ("05", "Performance Optimization", "Performance Analyzer, DAX Studio, VertiPaq concepts, cardinality and model tuning."),
    ("06", "Advanced Analytics & AI", "What-if parameters, key influencers, decomposition tree, forecasting, AI-assisted insights."),
    ("07", "Security Design", "Static & dynamic row-level security, object-level security, sensitivity labels, sharing controls."),
    ("08", "Service Enterprise Deployment", "Workspaces, Apps, deployment pipelines, gateways, scheduled refresh at scale."),
    ("09", "Monitoring & Governance", "Usage metrics, activity logs, admin portal, capacity metrics, adoption tracking."),
    ("10", "Premium, Fabric & Capacity", "XMLA endpoint, Direct Lake, OneLake, paginated reports, capacity planning."),
    ("11", "Automation & DevOps", "PBIP source control, REST APIs, service principals, Tabular Editor, CI/CD lifecycle."),
]

# Each theme: primary (dark), secondary (mid), accent (bright), bg tint, label, cloud subtitle,
# audience blurb, availability legend copy, footer compliance note, hero eyebrow text.
THEMES = {
    "commercial": {
        "file": "Datasheet-AzureCommercial",
        "cloud_name": "Azure Commercial",
        "eyebrow": "PUBLIC / COMMERCIAL CLOUD TRACK",
        "primary": "#0B2545",
        "secondary": "#13315C",
        "accent": "#00B4D8",
        "accent2": "#90E0EF",
        "bg": "#F4F9FC",
        "card_bg": "#FFFFFF",
        "audience": "Enterprise BI teams, analysts, and platform owners working in commercial Microsoft 365 / Power BI / Fabric tenants who want to use the full breadth of current features, including Copilot, Fabric, and Direct Lake.",
        "availability_note": "This track uses the full commercial feature set, including the newest previews such as Copilot, Fabric, and Direct Lake mode.",
        "compliance": "Delivered against standard commercial Microsoft 365 / Power BI / Fabric tenants.",
        "show_gov_legend": False,
        "special_topics": [
            "Microsoft Fabric, OneLake, and Direct Lake mode",
            "Copilot and AI-assisted authoring experiences",
            "Deployment pipelines and Git integration in Fabric workspaces",
            "Latest preview visuals and AI-powered analytics",
        ],
    },
    "azuregov": {
        "file": "Datasheet-AzureGovernment",
        "cloud_name": "Azure Government (GCC High)",
        "eyebrow": "GOVERNMENT COMMUNITY CLOUD HIGH TRACK",
        "primary": "#1E2761",
        "secondary": "#2C3E7A",
        "accent": "#3E6B9A",
        "accent2": "#CADCFC",
        "bg": "#F3F5FB",
        "card_bg": "#FFFFFF",
        "audience": "Public sector, defense-adjacent contractors, and regulated-industry BI teams operating in GCC High tenants who need advanced authoring and governance skills validated for sovereign cloud constraints.",
        "availability_note": "Every advanced feature is labeled Gov-ready, Verify with Instructor, or Not Covered so instructors and learners always know what to confirm in-tenant during delivery.",
        "compliance": "Delivered with Gov-ready lab paths first; any feature not yet confirmed for this tenant is flagged for the instructor to verify live or substitute an alternate exercise.",
        "show_gov_legend": True,
        "special_topics": [
            "Feature-by-feature Gov-ready / Verify-with-Instructor labeling",
            "Dynamic RLS validated against Entra ID (Gov) identity formats",
            "Instructor-verified alternates for Fabric, Copilot, and AI visual features",
            "Sovereign cloud data residency and export-control awareness",
        ],
    },
    "azuredod": {
        "file": "Datasheet-AzureDoD",
        "cloud_name": "Azure DoD",
        "eyebrow": "DEPARTMENT OF DEFENSE CLOUD TRACK",
        "primary": "#1B1F23",
        "secondary": "#2E3438",
        "accent": "#B5121B",
        "accent2": "#C9A227",
        "bg": "#F5F5F4",
        "card_bg": "#FFFFFF",
        "audience": "DoD mission owners, uniformed and civilian BI developers, and contractor support teams operating in Azure DoD/IL5 tenants who need rigorously validated, mission-ready reporting skills.",
        "availability_note": "The DoD track defaults to the most conservative Gov-ready path. Any feature not already confirmed for the target tenant is treated as conceptual-only until the instructor verifies it live or authorizes an alternate exercise.",
        "compliance": "Delivered against Azure DoD (IL5) constraints; the instructor verifies each flagged feature in-tenant before it is used operationally.",
        "show_gov_legend": True,
        "special_topics": [
            "Conservative-by-default Gov-ready lab paths for every module",
            "Static and dynamic RLS hardened for mission data segregation",
            "Export-control and data-handling awareness built into report UX labs",
            "Instructor-verified, conceptual-only coverage of Fabric/Copilot pending tenant authorization",
        ],
    },
}

DELIVERY_FORMATS = [
    ("1-Day Executive Briefing", "Hours scoped at booking", "Leadership & architects", "Guided tour of modeling, DAX, report UX, security, and enterprise delivery considerations. Demo-driven with a short applied exercise."),
    ("3-Day Standard Workshop", "Hours scoped at booking", "Report authors & analysts", "Hands-on Modules 1-7: modeling, DAX, Power Query, report UX, performance, analytics, and security, using the full lab set."),
    ("5-Day Extended Workshop", "Hours scoped at booking", "BI developers & platform owners", "Full Modules 1-11 plus capstone: adds Service deployment, monitoring/governance, capacity architecture, and DevOps lifecycle."),
]

def render_html(theme):
    t = THEMES[theme]
    module_cards = "\n".join(
        f"""
        <div class="module-card">
          <div class="module-num">{num}</div>
          <div class="module-body">
            <div class="module-title">{title}</div>
            <div class="module-desc">{desc}</div>
          </div>
        </div>"""
        for num, title, desc in MODULES
    )

    delivery_cards = "\n".join(
        f"""
        <div class="delivery-card">
          <div class="delivery-title">{name}</div>
          <div class="delivery-meta">{hours} &middot; {audience}</div>
          <div class="delivery-desc">{desc}</div>
        </div>"""
        for name, hours, audience, desc in DELIVERY_FORMATS
    )

    special_topics = "\n".join(f"<li>{topic}</li>" for topic in t["special_topics"])

    legend_html = """
        <div class="legend-row">
          <div class="legend-pill pill-green">GOV-READY</div>
          <div class="legend-pill pill-amber">VERIFY WITH INSTRUCTOR</div>
          <div class="legend-pill pill-gray">NOT COVERED</div>
        </div>""" if t.get("show_gov_legend") else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Advanced Power BI - {t['cloud_name']} Datasheet</title>
<style>
  @page {{ size: Letter; margin: 0; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    margin: 0;
    color: #1A1A1A;
    background: {t['bg']};
  }}
  .page {{
    width: 8.5in;
    height: 11in;
    position: relative;
    overflow: hidden;
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}

  /* ---------- PAGE 1 ---------- */
  .hero {{
    background: linear-gradient(135deg, {t['primary']} 0%, {t['secondary']} 65%, {t['accent']} 130%);
    color: #ffffff;
    padding: 0.55in 0.6in 0.5in 0.6in;
    position: relative;
  }}
  .hero::after {{
    content: "";
    position: absolute;
    right: -80px;
    top: -80px;
    width: 320px;
    height: 320px;
    border-radius: 50%;
    background: {t['accent2']}22;
  }}
  .hero::before {{
    content: "";
    position: absolute;
    right: 40px;
    bottom: -120px;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: {t['accent']}33;
  }}
  .eyebrow {{
    font-size: 11px;
    letter-spacing: 2.5px;
    font-weight: 700;
    color: {t['accent2']};
    margin-bottom: 10px;
  }}
  .hero h1 {{
    font-size: 34px;
    line-height: 1.15;
    margin: 0 0 8px 0;
    font-weight: 800;
    max-width: 6.3in;
  }}
  .hero .sub {{
    font-size: 15px;
    color: #E7EEF7;
    max-width: 6.0in;
    line-height: 1.5;
    position: relative;
    z-index: 2;
  }}
  .cloud-chip {{
    display: inline-block;
    margin-top: 16px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 20px;
    padding: 6px 16px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    position: relative;
    z-index: 2;
  }}

  .stat-row {{
    display: flex;
    gap: 0.28in;
    padding: 0.24in 0.6in;
    background: {t['card_bg']};
    border-bottom: 1px solid #E7E7E7;
  }}
  .stat {{
    flex: 1;
    text-align: left;
  }}
  .stat .num {{
    font-size: 30px;
    font-weight: 800;
    color: {t['primary']};
    line-height: 1;
  }}
  .stat .label {{
    font-size: 11px;
    color: #555;
    margin-top: 4px;
    letter-spacing: 0.3px;
  }}
  .stat-divider {{
    width: 1px;
    background: #E2E2E2;
  }}

  .section {{
    padding: 0.2in 0.6in 0 0.6in;
  }}
  .section-title {{
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: {t['primary']};
    text-transform: uppercase;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .section-title::before {{
    content: "";
    width: 22px;
    height: 4px;
    background: {t['accent']};
    display: inline-block;
    border-radius: 2px;
  }}

  .module-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 14px;
  }}
  .module-card {{
    display: flex;
    gap: 9px;
    background: {t['card_bg']};
    border: 1px solid #E4E7EC;
    border-radius: 8px;
    padding: 7px 10px;
  }}
  .module-num {{
    font-size: 13px;
    font-weight: 800;
    color: #ffffff;
    background: {t['primary']};
    border-radius: 6px;
    width: 24px;
    height: 24px;
    min-width: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .module-title {{
    font-size: 11.5px;
    font-weight: 700;
    color: #1A1A1A;
    margin-bottom: 2px;
  }}
  .module-desc {{
    font-size: 9.3px;
    color: #555;
    line-height: 1.3;
  }}

  .footer-bar {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: {t['primary']};
    color: #fff;
    font-size: 9.5px;
    padding: 9px 0.6in;
    display: flex;
    justify-content: space-between;
    letter-spacing: 0.3px;
  }}

  /* ---------- PAGE 2 ---------- */
  .p2-header {{
    background: {t['primary']};
    color: #fff;
    padding: 0.4in 0.6in 0.3in 0.6in;
  }}
  .p2-header h2 {{
    margin: 0 0 4px 0;
    font-size: 24px;
    font-weight: 800;
  }}
  .p2-header .sub {{
    font-size: 12.5px;
    color: {t['accent2']};
  }}

  .delivery-row {{
    display: flex;
    gap: 12px;
    padding: 0.3in 0.6in 0 0.6in;
  }}
  .delivery-card {{
    flex: 1;
    background: {t['card_bg']};
    border: 1px solid #E4E7EC;
    border-top: 4px solid {t['accent']};
    border-radius: 8px;
    padding: 14px;
  }}
  .delivery-title {{
    font-size: 13px;
    font-weight: 800;
    color: {t['primary']};
    margin-bottom: 4px;
  }}
  .delivery-meta {{
    font-size: 10px;
    font-weight: 700;
    color: {t['accent']};
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  .delivery-desc {{
    font-size: 10.5px;
    color: #444;
    line-height: 1.45;
  }}

  .two-col {{
    display: flex;
    gap: 0.3in;
    padding: 0.28in 0.6in 0 0.6in;
  }}
  .col {{
    flex: 1;
  }}
  .info-card {{
    background: {t['card_bg']};
    border: 1px solid #E4E7EC;
    border-radius: 8px;
    padding: 14px 16px;
    height: 100%;
  }}
  .info-card h3 {{
    margin: 0 0 8px 0;
    font-size: 13px;
    color: {t['primary']};
    font-weight: 800;
  }}
  .info-card p {{
    font-size: 10.8px;
    color: #444;
    line-height: 1.5;
    margin: 0 0 8px 0;
  }}
  .info-card ul {{
    margin: 0;
    padding-left: 16px;
  }}
  .info-card li {{
    font-size: 10.5px;
    color: #333;
    margin-bottom: 5px;
    line-height: 1.4;
  }}

  .legend-row {{
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }}
  .legend-pill {{
    flex: 1;
    border-radius: 6px;
    padding: 7px 9px;
    font-size: 9px;
    font-weight: 700;
    color: #fff;
    text-align: center;
    line-height: 1.3;
  }}
  .pill-green {{ background: #2E7D32; }}
  .pill-amber {{ background: #B8860B; }}
  .pill-gray {{ background: #757575; }}

  .cta {{
    margin: 0.28in 0.6in 0 0.6in;
    background: linear-gradient(120deg, {t['primary']}, {t['secondary']});
    color: #fff;
    border-radius: 10px;
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .cta .cta-title {{
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 3px;
  }}
  .cta .cta-sub {{
    font-size: 10.5px;
    color: {t['accent2']};
  }}
  .cta .cta-badge {{
    background: {t['accent']};
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    white-space: nowrap;
  }}

  .flow-strip {{
    margin: 0.26in 0.6in 0 0.6in;
    display: flex;
    align-items: center;
    gap: 4px;
    flex-wrap: wrap;
  }}
  .flow-step {{
    background: {t['card_bg']};
    border: 1px solid #E4E7EC;
    border-left: 4px solid {t['accent']};
    border-radius: 6px;
    padding: 7px 11px;
    font-size: 9.8px;
    font-weight: 700;
    color: {t['primary']};
  }}
  .flow-arrow {{
    color: {t['accent']};
    font-size: 14px;
    font-weight: 800;
  }}

  .capstone-band {{
    margin: 0.26in 0.6in 0 0.6in;
    background: {t['card_bg']};
    border: 1px solid #E4E7EC;
    border-radius: 8px;
    padding: 16px 18px;
    display: flex;
    gap: 18px;
    align-items: flex-start;
  }}
  .capstone-icon {{
    width: 46px;
    height: 46px;
    min-width: 46px;
    border-radius: 10px;
    background: {t['primary']};
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
  }}
  .capstone-title {{
    font-size: 13px;
    font-weight: 800;
    color: {t['primary']};
    margin-bottom: 5px;
  }}
  .capstone-desc {{
    font-size: 10.5px;
    color: #444;
    line-height: 1.5;
  }}
</style>
</head>
<body>

<!-- PAGE 1 -->
<div class="page">
  <div class="hero">
    <div class="eyebrow">{t['eyebrow']}</div>
    <h1>Advanced Power BI<br>Training Program</h1>
    <div class="sub">An 11-module, capstone-driven curriculum that takes report authors and platform teams from advanced modeling and DAX through enterprise deployment, governance, and DevOps &mdash; purpose-built for {t['cloud_name']} delivery.</div>
    <div class="cloud-chip">CLOUD TRACK: {t['cloud_name'].upper()}</div>
  </div>

  <div class="stat-row">
    <div class="stat"><div class="num">11</div><div class="label">Core training modules</div></div>
    <div class="stat-divider"></div>
    <div class="stat"><div class="num">1&ndash;5</div><div class="label">Day delivery options</div></div>
    <div class="stat-divider"></div>
    <div class="stat"><div class="num">40+</div><div class="label">Hands-on guided exercises</div></div>
    <div class="stat-divider"></div>
    <div class="stat"><div class="num">1</div><div class="label">Capstone solution build</div></div>
  </div>

  <div class="section">
    <div class="section-title">Who this training is for</div>
    <div class="module-card" style="grid-column: span 2; margin-bottom: 14px;">
      <div class="module-body"><div class="module-desc" style="font-size: 11.5px;">{t['audience']}</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Curriculum at a glance</div>
    <div class="module-grid">
      {module_cards}
    </div>
  </div>

  <div class="footer-bar">
    <div>Advanced Power BI &middot; {t['cloud_name']} Datasheet</div>
    <div>Page 1 of 2</div>
  </div>
</div>

<!-- PAGE 2 -->
<div class="page">
  <div class="p2-header">
    <h2>Flexible Delivery Formats</h2>
    <div class="sub">Choose the depth that matches your audience &mdash; every format maps directly to the same 11-module curriculum.</div>
  </div>

  <div class="delivery-row">
    {delivery_cards}
  </div>

  <div class="two-col">
    <div class="col">
      <div class="info-card">
        <h3>{t['cloud_name']} delivery notes</h3>
        <p>{t['availability_note']}</p>
        {legend_html}
      </div>
    </div>
    <div class="col">
      <div class="info-card">
        <h3>Track highlights for this cloud</h3>
        <ul>
          {special_topics}
        </ul>
      </div>
    </div>
  </div>

  <div class="flow-strip">
    <div class="flow-step">Power Query</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">Semantic Model</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">DAX</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">Report UX</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">Performance &amp; Security</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">Service Deployment</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">Governance</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step">DevOps</div><div class="flow-arrow">&rarr;</div>
    <div class="flow-step" style="border-left-color: {t['primary']}; background:{t['primary']}; color:#fff;">Capstone</div>
  </div>

  <div class="capstone-band">
    <div class="capstone-icon">&#9733;</div>
    <div>
      <div class="capstone-title">Capstone: Enterprise-Ready Power BI Solution</div>
      <div class="capstone-desc">Learners apply the full lifecycle end to end &mdash; an optimized semantic model, advanced DAX, an interactive report with drillthrough and mobile layout, static &amp; dynamic RLS, Service publishing, scheduled refresh, and packaging as a governed Power BI App, all validated against {t['cloud_name']} constraints.</div>
    </div>
  </div>

  <div class="cta">
    <div>
      <div class="cta-title">Ready to schedule {t['cloud_name']} delivery?</div>
      <div class="cta-sub">{t['compliance']}</div>
    </div>
    <div class="cta-badge">CONTACT YOUR DELIVERY LEAD</div>
  </div>

  <div class="footer-bar">
    <div>Advanced Power BI &middot; {t['cloud_name']} Datasheet</div>
    <div>Page 2 of 2</div>
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
        for theme in THEMES:
            html = render_html(theme)
            html_path = os.path.join(HERE, f"{THEMES[theme]['file']}.html")
            pdf_path = os.path.join(HERE, f"{THEMES[theme]['file']}.pdf")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.pdf(path=pdf_path, format="Letter", print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
            print(f"Generated {pdf_path}")
        browser.close()


if __name__ == "__main__":
    main()
