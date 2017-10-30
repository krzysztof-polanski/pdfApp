from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from dbhelper import DBHelper

DB = DBHelper()
document = open('pdf-sample.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
page = PDFPage.get_pages(document).next()
interpreter.process_page(page)
layout = device.get_result()
for e in layout:
    if isinstance(e, LTTextBoxHorizontal):
        data = [e.get_text(),
                round(e.x0,2),
                round(e.x1,2),
                round(e.y0,2),
                round(e.y1,2)
                ]
        DB.add_input(data)
