from reportlab.graphics.shapes import Drawing, String, Image
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas

def convert(img_arr, pdf_url, title):
    pdf_handler = canvas.Canvas(pdf_url, pagesize=(1200, 950))
    pdf_handler.setLineWidth(1200)
    pdf_handler.setTitle(title)

    for cur_img in img_arr:
        pdf_handler.drawImage(cur_img, 0, 25)
        pdf_handler.showPage()

    pdf_handler.save()

    print(pdf_url)

