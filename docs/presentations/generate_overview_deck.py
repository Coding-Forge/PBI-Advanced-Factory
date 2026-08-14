"""Advanced Power BI -- Program Overview Deck

Original content deck (not derived from the internal training-outline docs)
covering the arc of an advanced Power BI curriculum: modeling, DAX, Power
Query, report UX, performance, analytics/AI, security, Service deployment,
governance, platform architecture, DevOps, and a capstone.

Visual language: "Signal & Slate" palette -- deep slate/navy base with a
electric-green/teal accent (distinct from the navy/cyan datasheet branding),
dark title/section slides, light content slides, one repeated motif: icons in
a rounded accent-colored badge, thin left-edge accent bars on cards.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import os
import copy

HERE = os.path.dirname(__file__)
ICON_DIR = os.path.join(HERE, "assets", "icons")
OUT_PATH = os.path.join(HERE, "Advanced-PowerBI-Program-Overview.pptx")

# ---------------------------------------------------------------- palette
SLATE_DARK = RGBColor(0x0E, 0x17, 0x24)     # near-black slate (dark bg)
SLATE = RGBColor(0x1B, 0x2A, 0x3D)          # panel slate
SLATE_MED = RGBColor(0x2D, 0x41, 0x59)      # card / divider
INK = RGBColor(0x11, 0x18, 0x22)            # body text on light bg
MUTED = RGBColor(0x5B, 0x6B, 0x7E)          # secondary text
ACCENT = RGBColor(0x3D, 0xDC, 0x97)         # electric green/teal
ACCENT_DEEP = RGBColor(0x10, 0x9A, 0x6A)    # deeper green for light-bg text
GOLD = RGBColor(0xE8, 0xB4, 0x4D)           # warm secondary accent
LIGHT_BG = RGBColor(0xF3, 0xF6, 0xF9)       # content slide background
CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ICE = RGBColor(0xC9, 0xDA, 0xE8)

HEAD_FONT = "Cambria"
BODY_FONT = "Calibri"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height


def add_slide():
    return prs.slides.add_slide(BLANK)


def set_bg(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def no_line(shape):
    shape.line.fill.background()


def add_rect(slide, x, y, w, h, color, line=False):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if not line:
        no_line(shp)
    shp.shadow.inherit = False
    return shp


def add_rrect(slide, x, y, w, h, color, radius=0.06, line=False, shadow=False):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    try:
        shp.adjustments[0] = radius
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if not line:
        no_line(shp)
    shp.shadow.inherit = False
    return shp


def add_text(slide, x, y, w, h, text, size=14, color=INK, bold=False, italic=False,
             align=PP_ALIGN.LEFT, font=BODY_FONT, anchor=MSO_ANCHOR.TOP, line_spacing=1.0,
             char_spacing=None):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = font
    return tb


def add_bullets(slide, x, y, w, h, items, size=13, color=INK, font=BODY_FONT,
                 space_after=8, bullet_color=None, line_spacing=1.08):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        pPr = p._pPr
        if pPr is None:
            pPr = p.get_or_add_pPr()
        buChar = pPr.makeelement(qn('a:buChar'), {'char': '\u2013'})
        buFont = pPr.makeelement(qn('a:buFont'), {'typeface': font})
        buClr = pPr.makeelement(qn('a:buClr'), {})
        srgb = pPr.makeelement(qn('a:srgbClr'), {'val': '%02X%02X%02X' % ((bullet_color or ACCENT_DEEP)[0], (bullet_color or ACCENT_DEEP)[1], (bullet_color or ACCENT_DEEP)[2])})
        buClr.append(srgb)
        pPr.append(buClr)
        pPr.append(buFont)
        pPr.append(buChar)
        pPr.set('marL', '182880')
        pPr.set('indent', '-182880')
        r = p.add_run()
        r.text = item
        r.font.size = Pt(size)
        r.font.color.rgb = color
        r.font.name = font
    return tb


def add_icon(slide, icon_name, x, y, size, badge_color=ACCENT, badge=True):
    if badge:
        b = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
        b.fill.solid()
        b.fill.fore_color.rgb = badge_color
        no_line(b)
        b.shadow.inherit = False
    pad = size * 0.22
    slide.shapes.add_picture(os.path.join(ICON_DIR, f"{icon_name}.png"), x + pad, y + pad, size - 2 * pad, size - 2 * pad)


def add_page_footer(slide, label, page_num, dark=False):
    color = ICE if dark else MUTED
    add_text(slide, Inches(0.5), Inches(7.14), Inches(8), Inches(0.3),
              f"Advanced Power BI  ·  {label}", size=9, color=color, font=BODY_FONT)
    add_text(slide, Inches(12.4), Inches(7.14), Inches(0.5), Inches(0.3),
              str(page_num), size=9, color=color, align=PP_ALIGN.RIGHT, font=BODY_FONT)


MODULE_COLOR = ACCENT
PAGE = [0]


def next_page():
    PAGE[0] += 1
    return PAGE[0]


# ============================================================== SLIDE 1: TITLE
def slide_title():
    s = add_slide()
    set_bg(s, SLATE_DARK)
    # background geometric accents
    add_rect(s, Emu(0), Emu(0), SW, Inches(0.12), ACCENT)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.6), Inches(-2.2), Inches(6), Inches(6))
    circle.fill.solid()
    circle.fill.fore_color.rgb = SLATE
    no_line(circle)
    circle.shadow.inherit = False
    circle2 = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.6), Inches(-1.0), Inches(3.6), Inches(3.6))
    circle2.fill.solid()
    circle2.fill.fore_color.rgb = SLATE_MED
    no_line(circle2)
    circle2.shadow.inherit = False

    add_text(s, Inches(0.9), Inches(1.55), Inches(7.5), Inches(0.5),
              "A DATA STORYTELLING & GOVERNANCE CURRICULUM", size=13, color=ACCENT,
              bold=True, font=BODY_FONT, char_spacing=2)
    add_text(s, Inches(0.85), Inches(2.05), Inches(10.8), Inches(2.0),
              "Advanced Power BI", size=58, color=WHITE, bold=True, font=HEAD_FONT)
    add_text(s, Inches(0.9), Inches(3.35), Inches(9.5), Inches(0.9),
              "From modeling fundamentals to enterprise-grade delivery: an 11-module\narc for analysts, BI developers, and platform owners who need Power BI\nto hold up under real production weight.",
              size=15, color=ICE, font=BODY_FONT, line_spacing=1.3)

    # stat strip
    stats = [("11", "Curriculum modules"), ("40+", "Guided exercises"), ("1", "Capstone solution")]
    x = Inches(0.9)
    for label_num, label_txt in stats:
        add_text(s, x, Inches(5.15), Inches(2.6), Inches(0.7), label_num, size=34, color=ACCENT, bold=True, font=HEAD_FONT)
        add_text(s, x, Inches(5.85), Inches(2.6), Inches(0.4), label_txt, size=11.5, color=ICE, font=BODY_FONT)
        x += Inches(2.85)

    add_text(s, Inches(0.9), Inches(6.9), Inches(6), Inches(0.4), "Program Overview", size=10.5, color=MUTED, font=BODY_FONT)


# ============================================================== SLIDE 2: WHY THIS PROGRAM EXISTS
def slide_why():
    s = add_slide()
    set_bg(s, LIGHT_BG)
    add_rect(s, Emu(0), Emu(0), SW, Inches(0.12), ACCENT)
    add_text(s, Inches(0.7), Inches(0.5), Inches(10), Inches(0.4), "WHY THIS PROGRAM EXISTS", size=12, color=ACCENT_DEEP, bold=True, font=BODY_FONT, char_spacing=1.5)
    add_text(s, Inches(0.7), Inches(0.85), Inches(11.5), Inches(0.8), "Most Power BI training stops at chart-building.\nThis one doesn't.", size=28, color=INK, bold=True, font=HEAD_FONT, line_spacing=1.1)

    cards = [
        ("gauge", "Reports that survive contact with real data", "Large fact tables, messy sources, and slow refreshes expose weak modeling fast. This program builds habits that hold up at scale, not just in a demo."),
        ("shield", "Governance is part of the design, not an afterthought", "Row-level security, workspace strategy, and monitoring are taught alongside DAX and visuals -- because a report nobody trusts doesn't get used."),
        ("gear", "A path from author to platform owner", "Learners move from single-report skills toward the operational and architectural judgment that senior BI roles actually require."),
    ]
    x = Inches(0.7)
    w = Inches(3.85)
    for icon, title, body in cards:
        add_rrect(s, x, Inches(2.15), w, Inches(4.3), CARD_BG, radius=0.05, shadow=True)
        add_rect(s, x, Inches(2.15), Inches(0.09), Inches(4.3), ACCENT)
        add_icon(s, icon, x + Inches(0.35), Inches(2.5), Inches(0.9), badge_color=SLATE_DARK)
        add_text(s, x + Inches(0.35), Inches(3.65), w - Inches(0.7), Inches(1.0), title, size=15.5, color=INK, bold=True, font=HEAD_FONT, line_spacing=1.15)
        add_text(s, x + Inches(0.35), Inches(4.55), w - Inches(0.7), Inches(1.8), body, size=11.5, color=MUTED, font=BODY_FONT, line_spacing=1.35)
        x += w + Inches(0.25)

    add_page_footer(s, "Program Overview", next_page())


# ============================================================== SLIDE 3: CURRICULUM MAP (dark, timeline)
def slide_curriculum_map():
    s = add_slide()
    set_bg(s, SLATE_DARK)
    add_text(s, Inches(0.7), Inches(0.45), Inches(10), Inches(0.4), "CURRICULUM MAP", size=12, color=ACCENT, bold=True, font=BODY_FONT, char_spacing=1.5)
    add_text(s, Inches(0.7), Inches(0.8), Inches(11), Inches(0.7), "Four arcs, eleven modules, one capstone", size=26, color=WHITE, bold=True, font=HEAD_FONT)

    arcs = [
        ("BUILD", ["1. Advanced Semantic Modeling", "2. Advanced DAX", "3. Advanced Power Query"], ACCENT),
        ("PRESENT", ["4. Report Design & UX", "5. Performance Optimization", "6. Advanced Analytics & AI"], GOLD),
        ("PROTECT & OPERATE", ["7. Security Design", "8. Service Deployment", "9. Monitoring & Governance"], RGBColor(0x6E, 0xA8, 0xE0)),
        ("SCALE", ["10. Capacity & Architecture", "11. DevOps & Lifecycle", "Capstone Project"], RGBColor(0xE0, 0x7A, 0x5F)),
    ]
    x = Inches(0.7)
    w = Inches(2.95)
    for label, items, color in arcs:
        add_rrect(s, x, Inches(1.75), w, Inches(4.9), SLATE, radius=0.06)
        add_rect(s, x, Inches(1.75), w, Inches(0.55), color)
        add_text(s, x, Inches(1.75), w, Inches(0.55), label, size=13, color=SLATE_DARK, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, font=BODY_FONT)
        yy = Inches(2.5)
        for item in items:
            dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.3), yy + Inches(0.08), Inches(0.12), Inches(0.12))
            dot.fill.solid(); dot.fill.fore_color.rgb = color; no_line(dot); dot.shadow.inherit = False
            add_text(s, x + Inches(0.55), yy, w - Inches(0.75), Inches(0.9), item, size=12, color=ICE, font=BODY_FONT, line_spacing=1.15)
            yy += Inches(1.35)
        x += w + Inches(0.2)

    add_page_footer(s, "Program Overview", next_page(), dark=True)


# ============================================================== MODULE SLIDE TEMPLATE
def slide_module(num, title, icon, tagline, points, skill_level, arc_label, arc_color):
    s = add_slide()
    set_bg(s, LIGHT_BG)
    # left rail
    add_rect(s, Emu(0), Emu(0), Inches(4.3), SH, SLATE_DARK)
    add_rect(s, Inches(4.3), Emu(0), Inches(0.06), SH, arc_color)

    add_text(s, Inches(0.55), Inches(0.55), Inches(3), Inches(0.4), arc_label, size=11, color=arc_color, bold=True, font=BODY_FONT, char_spacing=1.5)
    add_text(s, Inches(0.55), Inches(0.95), Inches(1.6), Inches(0.9), f"{num:02d}", size=52, color=WHITE, bold=True, font=HEAD_FONT)
    add_icon(s, icon, Inches(0.55), Inches(2.1), Inches(1.15), badge_color=arc_color)
    add_text(s, Inches(0.55), Inches(3.5), Inches(3.3), Inches(1.6), title, size=22, color=WHITE, bold=True, font=HEAD_FONT, line_spacing=1.15)
    add_text(s, Inches(0.55), Inches(5.15), Inches(3.3), Inches(1.5), tagline, size=12.5, color=ICE, italic=True, font=BODY_FONT, line_spacing=1.35)
    add_text(s, Inches(0.55), Inches(6.55), Inches(3.3), Inches(0.4), f"LEVEL: {skill_level}", size=10, color=arc_color, bold=True, font=BODY_FONT, char_spacing=1.2)

    add_text(s, Inches(4.75), Inches(0.55), Inches(8), Inches(0.4), "WHAT LEARNERS WALK AWAY WITH", size=12, color=ACCENT_DEEP, bold=True, font=BODY_FONT, char_spacing=1.2)
    yy = Inches(1.15)
    for head, body in points:
        add_rrect(s, Inches(4.75), yy, Inches(8.0), Inches(1.35), CARD_BG, radius=0.08, shadow=True)
        add_rect(s, Inches(4.75), yy, Inches(0.08), Inches(1.35), arc_color)
        add_text(s, Inches(5.05), yy + Inches(0.14), Inches(7.4), Inches(0.4), head, size=13.5, color=INK, bold=True, font=HEAD_FONT)
        add_text(s, Inches(5.05), yy + Inches(0.55), Inches(7.4), Inches(0.75), body, size=11, color=MUTED, font=BODY_FONT, line_spacing=1.25)
        yy += Inches(1.55)

    add_page_footer(s, title, next_page())


# ============================================================== SECTION DIVIDER
def slide_section(arc_label, arc_title, arc_desc, arc_color, module_titles):
    s = add_slide()
    set_bg(s, SLATE_DARK)
    add_rect(s, Emu(0), Emu(0), SW, Inches(0.12), arc_color)
    add_text(s, Inches(0.9), Inches(1.5), Inches(6), Inches(0.4), f"ARC · {arc_label}", size=13, color=arc_color, bold=True, font=BODY_FONT, char_spacing=2)
    add_text(s, Inches(0.85), Inches(2.0), Inches(9.5), Inches(1.3), arc_title, size=40, color=WHITE, bold=True, font=HEAD_FONT, line_spacing=1.05)
    add_text(s, Inches(0.9), Inches(3.35), Inches(8.3), Inches(1.0), arc_desc, size=14, color=ICE, font=BODY_FONT, line_spacing=1.35)

    x = Inches(0.9)
    w = Inches(3.75)
    for t in module_titles:
        add_rrect(s, x, Inches(4.7), w, Inches(1.5), SLATE, radius=0.08)
        add_rect(s, x, Inches(4.7), Inches(0.07), Inches(1.5), arc_color)
        add_text(s, x + Inches(0.3), Inches(4.95), w - Inches(0.5), Inches(1.0), t, size=13.5, color=WHITE, bold=True, font=BODY_FONT, line_spacing=1.2, anchor=MSO_ANCHOR.MIDDLE)
        x += w + Inches(0.2)

    add_page_footer(s, arc_label, next_page(), dark=True)


# ============================================================== CAPSTONE SLIDE
def slide_capstone():
    s = add_slide()
    set_bg(s, SLATE_DARK)
    add_rect(s, Emu(0), Emu(0), SW, Inches(0.12), GOLD)
    add_icon(s, "rocket", Inches(0.9), Inches(1.15), Inches(1.5), badge_color=GOLD)
    add_text(s, Inches(2.75), Inches(1.2), Inches(4), Inches(0.4), "CAPSTONE", size=13, color=GOLD, bold=True, font=BODY_FONT, char_spacing=2)
    add_text(s, Inches(2.7), Inches(1.6), Inches(9.5), Inches(0.9), "One dataset. One deadline.\nEvery skill from Modules 1-11.", size=30, color=WHITE, bold=True, font=HEAD_FONT, line_spacing=1.1)

    add_text(s, Inches(0.9), Inches(3.05), Inches(11.5), Inches(0.7),
              "Learners take a single messy source dataset from raw files to a governed, secured, production-ready Power BI solution -- end to end, without a script to follow.",
              size=14, color=ICE, font=BODY_FONT, line_spacing=1.3)

    steps = [
        ("1", "Model it", "Build a star schema, handle grain and role-playing dates, and validate relationships."),
        ("2", "Calculate it", "Write the DAX measures the business actually asked for, not the easy ones."),
        ("3", "Present it", "Design a navigable, accessible report with drillthrough and a mobile layout."),
        ("4", "Ship it", "Publish, secure with RLS, and document it like it has to survive an audit."),
    ]
    x = Inches(0.9)
    w = Inches(2.75)
    for num, head, body in steps:
        add_rrect(s, x, Inches(4.0), w, Inches(2.6), SLATE, radius=0.06)
        add_text(s, x + Inches(0.3), Inches(4.2), Inches(1), Inches(0.7), num, size=30, color=GOLD, bold=True, font=HEAD_FONT)
        add_text(s, x + Inches(0.3), Inches(4.95), w - Inches(0.6), Inches(0.4), head, size=15, color=WHITE, bold=True, font=HEAD_FONT)
        add_text(s, x + Inches(0.3), Inches(5.4), w - Inches(0.6), Inches(1.1), body, size=10.5, color=ICE, font=BODY_FONT, line_spacing=1.25)
        x += w + Inches(0.2)

    add_page_footer(s, "Capstone", next_page(), dark=True)


# ============================================================== CLOSING SLIDE
def slide_closing():
    s = add_slide()
    set_bg(s, SLATE_DARK)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(-2.2), Inches(3.6), Inches(6), Inches(6))
    circle.fill.solid(); circle.fill.fore_color.rgb = SLATE; no_line(circle); circle.shadow.inherit = False
    add_rect(s, Emu(0), Emu(0), SW, Inches(0.12), ACCENT)

    add_text(s, Inches(0.9), Inches(2.2), Inches(10), Inches(0.4), "WHERE LEARNERS END UP", size=12, color=ACCENT, bold=True, font=BODY_FONT, char_spacing=2)
    add_text(s, Inches(0.85), Inches(2.65), Inches(11), Inches(1.6), "Confident modeling, defensible\nnumbers, and reports people trust.", size=36, color=WHITE, bold=True, font=HEAD_FONT, line_spacing=1.15)
    add_text(s, Inches(0.9), Inches(4.35), Inches(9), Inches(0.9),
              "Advanced Power BI is built for teams who are past the tutorials and need\nthe judgment, patterns, and habits that hold up in production.",
              size=14, color=ICE, font=BODY_FONT, line_spacing=1.35)

    add_page_footer(s, "Program Overview", next_page(), dark=True)


# ================================================================ BUILD DECK
slide_title()
slide_why()
slide_curriculum_map()

slide_section(
    "BUILD", "Model it right before you calculate anything",
    "The foundation arc: turning raw, flat data into a trustworthy semantic model and a clean transformation layer -- the two things every later module depends on.",
    ACCENT,
    ["01 · Advanced Semantic Modeling", "02 · Advanced DAX", "03 · Advanced Power Query"],
)

slide_module(
    1, "Advanced Semantic Modeling", "layers",
    "Turning a flat file into a model that scales, and a schema that survives new requirements.",
    [
        ("Star schema from first principles", "Fact and dimension design, grain decisions, and why a wide flat table eventually breaks every report built on it."),
        ("Relationships that don't fight you", "Role-playing dimensions, bridge tables, and composite/DirectQuery model choices with their tradeoffs."),
        ("Models built for growth", "Handling large fact tables, incremental refresh readiness, and keeping a model maintainable as it scales."),
    ],
    "Intermediate → Advanced", "BUILD", ACCENT,
)

slide_module(
    2, "Advanced DAX", "formula",
    "Getting past copy-pasted measures into real command of filter and row context.",
    [
        ("Context, demystified", "Filter context vs. row context, and why the same measure can return different numbers on two visuals."),
        ("Patterns that hold up under scrutiny", "Time intelligence, semi-additive measures, ranking, and calculation groups -- built and explained, not memorized."),
        ("Measures that perform", "Diagnosing slow DAX, using variables deliberately, and validating logic before layering complexity on top."),
    ],
    "Advanced", "BUILD", ACCENT,
)

slide_module(
    3, "Advanced Power Query", "funnel",
    "Building a transformation layer that's traceable, testable, and reusable -- not a black box.",
    [
        ("Staged, parameterized pipelines", "Parameters for source switching, staged queries, and functions that eliminate copy-pasted steps."),
        ("Query folding and performance", "Understanding when a query pushes work back to the source, and when it silently stops."),
        ("Data quality as a first-class step", "Error-review patterns and cleansing functions that make bad rows visible instead of silently dropped."),
    ],
    "Advanced", "BUILD", ACCENT,
)

slide_section(
    "PRESENT", "Turn a correct model into a report people actually use",
    "The experience arc: report UX that guides rather than overwhelms, a model fast enough to stay that way under load, and analytics that go beyond a static chart.",
    GOLD,
    ["04 · Report Design & UX", "05 · Performance Optimization", "06 · Advanced Analytics & AI"],
)

slide_module(
    4, "Report Design & UX", "canvas_layout",
    "Designing navigation and interaction, not just placing visuals on a canvas.",
    [
        ("Guided interaction patterns", "Drillthrough, bookmarks, custom tooltips, and navigation that leads users somewhere intentional."),
        ("Flexible by design", "Field parameters and dynamic titles that let one report answer several questions instead of one."),
        ("Built for every screen and every user", "Mobile-optimized layouts, conditional formatting, and an accessibility pass before anything ships."),
    ],
    "Intermediate → Advanced", "PRESENT", GOLD,
)

slide_module(
    5, "Performance Optimization", "gauge",
    "Finding out why a report is slow before guessing how to fix it.",
    [
        ("Evidence before optimization", "Performance Analyzer baselines and DAX Studio comparisons -- measure first, then change one thing."),
        ("Model size is a design decision", "Cardinality reduction, aggregation tables, and composite model choices that shrink refresh and query time."),
        ("Refresh strategy at scale", "Incremental refresh policy design and the licensing/capacity tradeoffs that come with it."),
    ],
    "Advanced", "PRESENT", GOLD,
)

slide_module(
    6, "Advanced Analytics & AI", "spark",
    "Going past the default chart into scenario modeling and AI-assisted analysis -- with eyes open about where it's available.",
    [
        ("What-if, not just what-happened", "Parameter-driven scenario analysis that lets stakeholders test assumptions live in the report."),
        ("The analytics visual toolkit", "Decomposition trees, forecasting, and key influencers for driver analysis beyond a trend line."),
        ("AI-assisted authoring, used deliberately", "Python/R visuals and Azure ML integration explored with a clear-eyed view of cloud and tenant availability."),
    ],
    "Advanced", "PRESENT", GOLD,
)

slide_section(
    "PROTECT & OPERATE", "A report that can't be trusted won't be used",
    "The trust arc: locking data down to the right audience, getting a solution live in the Service, and keeping it healthy once real users depend on it.",
    RGBColor(0x6E, 0xA8, 0xE0),
    ["07 · Security Design", "08 · Service Deployment", "09 · Monitoring & Governance"],
)

slide_module(
    7, "Security Design", "shield",
    "Designing row-level security like an architecture decision, not a checkbox.",
    [
        ("Static and dynamic RLS", "Building roles that scale from a handful of regions to a dynamic, user-driven security model."),
        ("Testing security like a user would", "Validating roles in Desktop and Service, not just trusting the DAX filter is correct."),
        ("Where Build permission fits in", "Understanding what elevated permissions expose, and designing around that risk deliberately."),
    ],
    "Advanced", "PROTECT & OPERATE", RGBColor(0x6E, 0xA8, 0xE0),
)

slide_module(
    8, "Service Deployment", "gear",
    "Getting from a working PBIX/PBIP to a solution real people depend on daily.",
    [
        ("Publishing with intent", "Workspace strategy, App packaging, and deployment pipelines instead of ad hoc publish clicks."),
        ("Refresh you can trust", "Scheduled refresh, gateway considerations, and troubleshooting failures before users notice them."),
        ("A repeatable release process", "Moving a report from dev to test to production with a process, not tribal memory."),
    ],
    "Intermediate → Advanced", "PROTECT & OPERATE", RGBColor(0x6E, 0xA8, 0xE0),
)

slide_module(
    9, "Monitoring, Administration & Governance", "gauge",
    "Running Power BI like a platform, not a pile of individually-managed reports.",
    [
        ("Usage as a signal", "Usage metrics and refresh history read as operational data, not vanity numbers."),
        ("Tenant settings with intention", "Understanding what each governance lever controls and who should be allowed to change it."),
        ("An operations runbook that outlives you", "Documenting the processes so governance survives a team change, not just a tenure."),
    ],
    "Advanced", "PROTECT & OPERATE", RGBColor(0x6E, 0xA8, 0xE0),
)

slide_section(
    "SCALE", "From one great report to a platform that scales",
    "The platform arc: capacity and architecture decisions, engineering discipline around Power BI artifacts, and the capstone that proves it all fits together.",
    RGBColor(0xE0, 0x7A, 0x5F),
    ["10 · Capacity & Architecture", "11 · DevOps & Lifecycle", "Capstone · End-to-End Build"],
)

slide_module(
    10, "Premium, Fabric & Capacity Architecture", "layers",
    "Choosing the right capacity and architecture before scale forces the decision for you.",
    [
        ("Capacity models compared", "Shared, Premium, and Fabric capacity tradeoffs mapped to real workload patterns, not just price sheets."),
        ("Fabric-aware design", "OneLake and Direct Lake concepts, and what they change about how a model should be built."),
        ("Planning for growth, not just today", "Architecture decisions that anticipate the next 10x of data volume and user count."),
    ],
    "Advanced", "SCALE", RGBColor(0xE0, 0x7A, 0x5F),
)

slide_module(
    11, "Automation, DevOps & Lifecycle Management", "gear",
    "Treating Power BI artifacts like source code, because eventually they have to be.",
    [
        ("PBIP and version control", "Git-friendly project files that make Power BI diffable, reviewable, and mergeable."),
        ("External tools and APIs", "Using the broader tooling ecosystem to script, validate, and automate what used to be manual."),
        ("CI/CD concepts for BI", "Deployment pipeline thinking applied to semantic models and reports, not just application code."),
    ],
    "Advanced", "SCALE", RGBColor(0xE0, 0x7A, 0x5F),
)

slide_capstone()
slide_closing()

prs.save(OUT_PATH)
print(f"Saved {OUT_PATH}")
print(f"Total slides: {len(prs.slides.__iter__.__self__._sldIdLst)}")
