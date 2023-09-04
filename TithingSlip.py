import datetime, fitz
from FinancialDocumentInterface import FinancialDocumentInterface

class TithingSlip(FinancialDocumentInterface):
    """
    Saves and represents the important information contained in a single Tithing Slip as a pdf.

    ...

    Attributes
    ----------
    __filepath : str
        the filepath of the tithing slip as a pdf
    __date : datetime
        the date of the tithing slip
    __tithingAmount : float
        the amount of tithing recorded as paid in the slip

    Methods
    -------
    readPayStub()
        Open and read the pdf at the filepath and sets member variables: __date, __tithingAmount
    getSerializeByteStream()
        Serialize this instance of the TithingSlip class as a pickle byte stream which can be saved to a save file.
    createExcelRepresentation()
        Create an excel that represents the data contained in this instance of the TithingSlip class.
    """
    def __init__(self, filepath:str):
        """ 
        Parameters
        ----------
        filepath : str
            the filepath of the paystub as a pdf
        """
        self.__filepath = filepath
        self.readFinancialDocument()

    def __str__(self):
        return f"Date: {self.__date}\nTithing Amount: {self.__tithingAmount}"

    def readFinancialDocument(self):
        """ Open and read the pdf at the filepath and sets member variables: __date, __tithingAmount """
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

    def getSerializedByteStream(self):
        """ Serialize this instance of the TithingSlip class as a pickle byte stream which can be saved to a save file. """
        return super().getSerializedByteStream()
    
    def createExcelRepresentation(self):
        """ Create an excel that represents the data contained in this instance of the TithingSlip class. """
        pass