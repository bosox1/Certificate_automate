import csv
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from nbformat import reader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial Unicode MS', 'arialuni.ttf'))

with open('Cerf_csv.csv', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for i, row in enumerate(csv_reader):
        # Load the blank template
        template = PdfReader(open("cerf_temp.pdf", "rb"))
        # Create a new writer to write the modified template to a new PDF
        writer = PdfWriter()

        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Arial Unicode MS", 16)
        can.setFillColorRGB(0, 0, 0)
        can.drawString(400, 370, row[0])
        can.setFont("Arial Unicode MS", 22)
        can.setFillColorRGB(0, 0, 0)
        can.drawString(270, 345, row[1])
        can.setFont("Arial Unicode MS", 16)
        can.setFillColorRGB(0, 0, 0)
        can.drawString(590, 225, row[2])
        can.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)

        # Get the first page of the template and merge it with the modified content

        page = template.pages[0]
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)

        # Write the new PDF to a file with a name based on the certificate recipient's name
        filename = f"{row[1].strip().replace(' ', '_')}_certif.pdf"
        with open(filename, "wb") as out_file:
            writer.write(out_file)

