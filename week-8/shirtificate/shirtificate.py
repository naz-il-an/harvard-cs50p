from fpdf import FPDF

class PDF(FPDF):    
    def header(self):        
        self.set_font('Helvetica', size=32)
        self.cell(0, 10, 'CS50 Shirtificate', align='C')
        self.ln(20)
        self.image('shirtificate.png', w=190)
        self.set_fill_color(255,255,255)

    def name(self, name):
        self.name = name
        self.set_font('Helvetica', size=30)
        self.set_text_color(255,255,255)
        self.cell(0, -250, name, align='C')


pdf = PDF()
pdf.add_page()
pdf.name(input('Name: '))
pdf.output('shirtificate.pdf')

