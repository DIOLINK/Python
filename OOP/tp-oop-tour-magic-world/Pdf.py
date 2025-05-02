from fpdf import FPDF


class PDFGenerator:
    def __init__(self, filename="output.pdf"):
        # Crear una instancia de la clase FPDF
        self.pdf = FPDF()
        # Agregar una página al PDF
        self.pdf.add_page()
        # Establecer la fuente y tamaño del texto
        self.pdf.set_font("Arial", size=12)
        # Establecer el nombre del archivo
        self.filename = filename

    def footer(self):
        # Pie de página del PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def chapterTitle(self, title):
        # Título del capítulo en el PDF
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def addText(self, text):
        # Agregar texto al PDF
        self.pdf.cell(200, 10, txt=text, ln=True, align='C')

    def savePdf(self):
        # Guardar el PDF en el archivo
        self.pdf.output(f'.//pdf/{self.filename}')
        print(f"El PDF se ha creado con éxito: {self.filename}")
