__author__ = 'kranthi'

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import sys


fp = open('/Users/kranthi/Downloads/166160-chicken_prn.pdf', 'rb')

parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)

doc.initialize('')

rsrcmgr = PDFResourceManager()
device = TextConverter(rsrcmgr, sys.stdout, codec='utf-8', laparams=LAParams())

process_pdf(rsrcmgr, device, fp, set(), maxpages=0, password='', caching=True, check_extractable=True)

fp.close()

