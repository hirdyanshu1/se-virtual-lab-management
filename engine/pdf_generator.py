"""
ReportLab PDF Generation Module
LabPilot AI — RTU Software Engineering Virtual Lab

Generates professional, downloadable academic PDF documents:
1. IEEE 830 Formatted SRS Documents
2. RTU Practical Experiment Completion Reports
"""

import os
import io
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from engine.rtu_data import get_rtu_experiment_by_id

def create_srs_pdf_buffer(srs_data, student_name="Rahul Sharma", roll_no="22EBKCS042"):
    """
    Builds an IEEE 830 compliant SRS document as an in-memory BytesIO PDF buffer.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    header_style = ParagraphStyle(
        'HeaderUniv',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        textColor=colors.HexColor("#4B5563"),
        alignment=1,
        fontName='Helvetica-Bold'
    )
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1,
        fontName='Helvetica-Bold',
        spaceAfter=10
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#3B82F6"),
        alignment=1,
        spaceAfter=15
    )
    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#374151")
    )
    h1_style = ParagraphStyle(
        'SecH1',
        parent=styles['Heading2'],
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=14,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    h2_style = ParagraphStyle(
        'SecH2',
        parent=styles['Heading3'],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#1F2937"),
        spaceBefore=8,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )
    body_style = ParagraphStyle(
        'BodyP',
        parent=styles['Normal'],
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=6
    )
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1F2937")
    )
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11.5,
        fontName='Helvetica-Bold',
        textColor=colors.white
    )

    story = []

    # Title & Header
    story.append(Paragraph("RAJASTHAN TECHNICAL UNIVERSITY (RTU), KOTA", header_style))
    story.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING", header_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", title_style))
    story.append(Paragraph("Conforming to IEEE Standard 830-1998 Guidelines", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=12))

    # Metadata Table
    project_title = srs_data.get("title", "LabPilot AI — Virtual Software Engineering Laboratory")
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    
    meta_data = [
        [Paragraph(f"<b>Project Title:</b> {project_title}", meta_style), Paragraph(f"<b>Prepared By:</b> {student_name}", meta_style)],
        [Paragraph(f"<b>Document Version:</b> 1.0 (Baseline)", meta_style), Paragraph(f"<b>University Roll No:</b> {roll_no}", meta_style)],
        [Paragraph(f"<b>Course:</b> B.Tech 3rd Sem (SE Lab)", meta_style), Paragraph(f"<b>Date:</b> {current_date}", meta_style)]
    ]
    meta_table = Table(meta_data, colWidths=[260, 260])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F3F4F6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D1D5DB")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 15))

    # Section 1: Introduction
    story.append(Paragraph("1. INTRODUCTION", h1_style))
    purpose = srs_data.get("purpose", "The purpose of this document is to specify all functional and non-functional requirements for the LabPilot AI platform.")
    scope = srs_data.get("scope", "The scope encompasses an interactive virtual laboratory for software engineering students performing RTU curriculum practicals.")
    story.append(Paragraph(f"<b>1.1 Purpose:</b> {purpose}", body_style))
    story.append(Paragraph(f"<b>1.2 Scope:</b> {scope}", body_style))
    story.append(Paragraph("<b>1.3 Definitions and Acronyms:</b> SRS (Software Requirements Specification), IEEE (Institute of Electrical and Electronics Engineers), OOAD (Object-Oriented Analysis & Design), GCC (GNU Compiler Collection).", body_style))

    # Section 2: Overall Description
    story.append(Paragraph("2. OVERALL DESCRIPTION", h1_style))
    story.append(Paragraph("<b>2.1 Product Perspective:</b> LabPilot AI is an independent, self-hosted web-based virtual laboratory operating in academic environments.", body_style))
    story.append(Paragraph("<b>2.2 User Classes and Characteristics:</b> Primary users include B.Tech Computer Science students (performers) and faculty lab evaluators (supervisors).", body_style))
    story.append(Paragraph(f"<b>2.3 Operating Environment:</b> Python 3.10+, SQLite database, MinGW GCC C compiler, accessible via modern HTML5/W3C standards compliant web browsers.", body_style))
    
    hw_reqs = srs_data.get("hardware_reqs", "Minimum 2 GHz Dual-Core CPU, 2 GB RAM, 500 MB free storage.")
    sw_reqs = srs_data.get("software_reqs", "Windows 10/11, Python 3, MinGW GCC, Modern Web Browser (Chrome/Firefox/Edge).")
    story.append(Paragraph(f"<b>2.4 Hardware Requirements:</b> {hw_reqs}", body_style))
    story.append(Paragraph(f"<b>2.5 Software Requirements:</b> {sw_reqs}", body_style))

    # Section 3: Functional Requirements Table
    story.append(Paragraph("3. SPECIFIC FUNCTIONAL REQUIREMENTS", h1_style))
    story.append(Paragraph("The following functional requirements define the explicit capabilities and operations the system shall perform:", body_style))

    reqs = srs_data.get("functional_requirements", [])
    if not reqs:
        reqs = [
            {"id": "FR-01", "text": "The system shall authenticate student credentials using valid roll number records.", "priority": "Must-Have"},
            {"id": "FR-02", "text": "The system shall provide an interactive text-to-diagram Mermaid.js UML canvas.", "priority": "Must-Have"},
            {"id": "FR-03", "text": "The system shall compile C code using local MinGW GCC compiler with stdin test piping.", "priority": "Must-Have"},
            {"id": "FR-04", "text": "The system shall track student experiment completion in persistent SQLite tables.", "priority": "Should-Have"}
        ]

    table_data = [[
        Paragraph("Req ID", table_cell_bold),
        Paragraph("Requirement Statement (Shall / Must)", table_cell_bold),
        Paragraph("Priority", table_cell_bold)
    ]]

    for r in reqs:
        table_data.append([
            Paragraph(r.get("id", "FR"), table_cell),
            Paragraph(r.get("text", ""), table_cell),
            Paragraph(r.get("priority", "Must-Have"), table_cell)
        ])

    fr_table = Table(table_data, colWidths=[65, 385, 70])
    fr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#9CA3AF")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F9FAFB")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(fr_table)
    story.append(Spacer(1, 10))

    # Section 4: Non-Functional Requirements
    story.append(Paragraph("4. NON-FUNCTIONAL REQUIREMENTS", h1_style))
    nfrs = srs_data.get("non_functional_requirements", [])
    if not nfrs:
        nfrs = [
            {"id": "NFR-01", "text": "The system shall render lab interface pages within 500 milliseconds under normal load.", "priority": "Performance"},
            {"id": "NFR-02", "text": "The system shall enforce SQLite ACID compliance to prevent submission corruption.", "priority": "Reliability"},
            {"id": "NFR-03", "text": "The user interface shall be accessible on displays with resolution >= 1280x720 pixels.", "priority": "Usability"}
        ]

    nfr_table_data = [[
        Paragraph("NFR ID", table_cell_bold),
        Paragraph("Non-Functional Specification & Measurable Metric", table_cell_bold),
        Paragraph("Category", table_cell_bold)
    ]]

    for nr in nfrs:
        nfr_table_data.append([
            Paragraph(nr.get("id", "NFR"), table_cell),
            Paragraph(nr.get("text", ""), table_cell),
            Paragraph(nr.get("priority", "Quality"), table_cell)
        ])

    nfr_table = Table(nfr_table_data, colWidths=[65, 385, 70])
    nfr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#374151")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#9CA3AF")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F9FAFB")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(nfr_table)
    story.append(Spacer(1, 12))

    # Verification & Sign-off Block
    story.append(Paragraph("5. VERIFICATION & APPROVAL", h1_style))
    sign_data = [
        [Paragraph("<b>Student Signature:</b>", meta_style), Paragraph("<b>Faculty Guide Signature:</b>", meta_style)],
        [Spacer(1, 15), Spacer(1, 15)],
        [Paragraph(f"{student_name} ({roll_no})", meta_style), Paragraph("Prof. Sunita Rao (Dept of CSE)", meta_style)]
    ]
    sign_table = Table(sign_data, colWidths=[260, 260])
    sign_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#D1D5DB")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(sign_table)

    doc.build(story)
    buffer.seek(0)
    return buffer

def create_experiment_report_pdf(exp_id, student_name="Rahul Sharma", roll_no="22EBKCS042", progress_data=None):
    """
    Generates a formal RTU Laboratory Experiment Practical Completion Certificate/Report.
    """
    exp = get_rtu_experiment_by_id(exp_id)
    if not exp:
        return None

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    header_style = ParagraphStyle('Head1', parent=styles['Normal'], fontSize=11, fontName='Helvetica-Bold', alignment=1, textColor=colors.HexColor("#4B5563"))
    title_style = ParagraphStyle('Head2', parent=styles['Heading1'], fontSize=16, fontName='Helvetica-Bold', alignment=1, textColor=colors.HexColor("#1E3A8A"), spaceAfter=6)
    meta_style = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=9.5, leading=13)
    h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=12, fontName='Helvetica-Bold', textColor=colors.HexColor("#1E3A8A"), spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=9, leading=13, spaceAfter=4)

    story = []
    story.append(Paragraph("RAJASTHAN TECHNICAL UNIVERSITY, KOTA", header_style))
    story.append(Paragraph("B.TECH 3RD SEMESTER — SOFTWARE ENGINEERING LABORATORY", header_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"PRACTICAL REPORT: {exp['code']}", title_style))
    story.append(Paragraph(f"<b>Title:</b> {exp['title']}", ParagraphStyle('PTitle', parent=styles['Normal'], fontSize=11, alignment=1, textColor=colors.HexColor("#2563EB"), spaceAfter=10)))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceAfter=10))

    # Meta
    current_date = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")
    quiz_score = progress_data.get("quiz_score", 0) if progress_data else 0
    quiz_total = progress_data.get("quiz_total", 5) if progress_data else 5
    status = progress_data.get("status", "COMPLETED") if progress_data else "COMPLETED"

    meta_table_data = [
        [Paragraph(f"<b>Student Name:</b> {student_name}", meta_style), Paragraph(f"<b>Roll Number:</b> {roll_no}", meta_style)],
        [Paragraph(f"<b>Category:</b> {exp['category']}", meta_style), Paragraph(f"<b>Difficulty:</b> {exp['difficulty']}", meta_style)],
        [Paragraph(f"<b>Status:</b> <font color='green'><b>{status}</b></font>", meta_style), Paragraph(f"<b>Quiz Score:</b> {quiz_score} / {quiz_total}", meta_style)],
        [Paragraph(f"<b>Completion Date:</b> {current_date}", meta_style), Paragraph("<b>Evaluator:</b> Lab Faculty In-Charge", meta_style)]
    ]
    t = Table(meta_table_data, colWidths=[260, 260])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F3F4F6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4)
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Objectives
    story.append(Paragraph("1. LEARNING OBJECTIVES ACHIEVED", h2_style))
    for obj in exp["learning_objectives"]:
        story.append(Paragraph(f"• {obj}", body_style))

    # Procedure
    story.append(Paragraph("2. PRACTICAL PROCEDURE SUMMARY", h2_style))
    for idx, proc in enumerate(exp["procedure"], 1):
        story.append(Paragraph(f"<b>Step {idx}:</b> {proc}", body_style))

    # Checklist
    story.append(Paragraph("3. VERIFIED PRACTICAL CHECKLIST", h2_style))
    for chk in exp["checklist"]:
        story.append(Paragraph(f" [✓] {chk}", body_style))

    # Viva Questions summary
    story.append(Paragraph("4. SAMPLE VIVA QUESTIONS & EXPLANATION", h2_style))
    for v in exp["viva_questions"][:3]:
        story.append(Paragraph(f"<b>Q: {v['q']}</b>", body_style))
        story.append(Paragraph(f"A: {v['a']}", ParagraphStyle('Ans', parent=body_style, textColor=colors.HexColor("#374151"), leftIndent=10)))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 15))
    sign_data = [
        [Paragraph("<b>Student Signature</b>", meta_style), Paragraph("<b>Faculty Evaluation & Signature</b>", meta_style)],
        [Spacer(1, 20), Spacer(1, 20)],
        [Paragraph(f"{student_name}", meta_style), Paragraph("Grade Awarded: _______________", meta_style)]
    ]
    st = Table(sign_data, colWidths=[260, 260])
    st.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (0,0), 0.5, colors.black),
        ('LINEBELOW', (1,0), (1,0), 0.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(st)

    doc.build(story)
    buffer.seek(0)
    return buffer
