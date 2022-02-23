test = "test"
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('times', size=20)
pdf.cell(0, 12, txt="Test", ln=True, align='L')
pdf.output('test-exe.pdf')
