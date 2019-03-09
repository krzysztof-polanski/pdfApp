from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from dbhelper import DBHelper


class Miner:
    def __init__(self, db=DBHelper, document_name='pdf-sample.pdf',
                 res_manager=PDFResourceManager, laparams=LAParams,
                 device=PDFPageAggregator, interpreter=PDFPageInterpreter):
        self.db = db()
        self.document_name = document_name
        self.document = open(self.document_name, 'rb')
        self.res_manager = res_manager()
        self.laparams = laparams()
        self.device = device(self.res_manager, laparams=self.laparams)
        self.interpreter = interpreter(self.res_manager, self.device)

    def mine(self):
        page = PDFPage.get_pages(self.document).next()
        self.interpreter.process_page(page)
        layout = self.device.get_result()
        for e in layout:
            if isinstance(e, LTTextBoxHorizontal):
                data = [
                    e.get_text(),
                    round(e.x0, 2),
                    round(e.x1, 2),
                    round(e.y0, 2),
                    round(e.y1, 2),
                ]
                self.db.add_input(data)
