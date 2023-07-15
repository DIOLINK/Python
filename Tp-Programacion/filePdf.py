from fpdf import FPDF


class PDF(FPDF):
    def footer(self):
        # Pie de página del PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        # Título del capítulo en el PDF
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, image_path):
        # Cuerpo del capítulo en el PDF
        self.image(image_path, x=10, y=None, w=190)
