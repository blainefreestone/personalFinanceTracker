import datetime, fitz
from FinancialDocumentInterface import FinancialDocumentInterface

class TithingSlip(FinancialDocumentInterface):
    def __init__(self, filepath:str):
        self.__filepath = filepath
        self.readTithingSlip()

    def __str__(self):
        return f"Date: {self.__date}\nTithing Amount: {self.__tithingAmount}"

    def readFinancialDocument(self):
        # Text block tuple indexes.
        BLOCK_NO = 5
        BLOCK_TEXT = 4
        # Elements of pdf file in text block numbers.
        DATE = 3
        TITHINGAMOUNT = 6
        
        # Open and access pdf file.
        tithingSlipPdf = fitz.open(self.__filepath)
        for page in tithingSlipPdf:
            # Divide pdf file into text block tuples.
            blocks = page.get_text("blocks")

            # Save tithing slip date as a datetime object.
            dateStringElements = blocks[DATE][BLOCK_TEXT].strip().split()
            dateString = dateStringElements[0] + dateStringElements[1] + dateStringElements[2]
            self.__date = datetime.datetime.strptime(dateString, "%d%b%Y")

            # Save tithng amount as a float.
            tithingAmountStringElements = blocks[TITHINGAMOUNT][BLOCK_TEXT].strip().split()
            self.__tithingAmount = float(tithingAmountStringElements[1])

            print("HELLO   ")

    def getSerializedByteStream(self):
        return super().getSerializedByteStream()
    
    def createExcelRepresentation(self):
        pass