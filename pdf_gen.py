from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def gen_pdf(student_id, existing_pdf, logo):
    # path = 'input_logo.jpg'
    path = logo
    # existing = PdfFileReader('./inputfile.pdf')
    existing = PdfFileReader(existing_pdf+'.pdf')
    pdf = PdfFileWriter()
    msg1 = """It’s easy to play any musical instrument"""
    msg2 = """all you have to do is touch the right key at the right
              time and the instrument will play itself."""
    for num in range(existing.getNumPages()):  # for each slide
        # Using ReportLab Canvas to insert image into PDF
        img_temp = BytesIO()
        packet = BytesIO()
        img_doc = canvas.Canvas(img_temp, pagesize=A4)
        # Draw image on Canvas and save PDF in buffer
        img_doc.drawImage(path.format(num), 0, 740, 100, 50, True, True)
        img_doc.save()
        can = canvas.Canvas(packet, pagesize=A4)
        can.drawString(500, 740, "Jhon Institute")
        can.drawString(70, 50, msg1)
        can.drawString(70, 30, msg2)
        can.save()
        packet.seek(0)
        # Use PyPDF to merge the image-PDF into the template
        page = existing.getPage(num)
        page.mergePage(PdfFileReader(BytesIO(img_temp.getvalue())).getPage(0))
        page.mergePage(PdfFileReader(packet).getPage(0))


        pdf.addPage(page)
        

    pdf.write(open("out{}_{}.pdf".format(student_id,existing_pdf),"wb"))
    return "out{}_{}.pdf".format(student_id,existing_pdf)


# if __name__ == '__main__':
#     gen_pdf()