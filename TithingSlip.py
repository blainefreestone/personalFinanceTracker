import datetime, fitz

class TithingSlip:
    def __init__(self, filepath:str):
        self.__filepath = filepath
        self.readTithingSlip()

    def readTithingSlip(self):
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