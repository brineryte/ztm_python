import PyPDF2 as pdf2
import sys

input_file_arg = sys.argv[1]
watermark_pdf = "wtr.pdf"
output_file = "watermarked.pdf"


def watermark(input_file):
    with open(input_file, "rb") as file:
        pdf = pdf2.PdfFileReader(file)
        with open(watermark_pdf, "rb") as wtr_file:
            wtr = pdf2.PdfFileReader(wtr_file)
            writer = pdf2.PdfFileWriter()

            for page in pdf.pages:
                page.mergePage(wtr.getPage(0))
                writer.addPage(page)

            with open(output_file, "wb") as file_output:
                writer.write(file_output)


watermark(input_file_arg)
