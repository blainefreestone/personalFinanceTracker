import datetime, fitz
from FinancialDocumentInterface import FinancialDocumentInterface

class SideIncomeStatement(FinancialDocumentInterface):
    """
    Saves and represents the important information contained in a single Side Income Statement file as txt. 
    
    ...

    Attributes
    ----------
    __filepath : str
        the filepath of the paystub as a pdf
    __date : datetime
        the date of the reported income
    __source : str
        the source of the reported income as a string

    Methods
    -------
    readFinancialDocument()
        Open and read the pdf at the filepath and sets member variables: 
    getSerializeByteStream()
        Serialize this instance of the SideIncomeStatement class as a pickle byte stream which can be saved to a save file.
    createExcelRepresentation()
        Create an excel that represents the data contained in this instance of the SideIncomeStatement class.    
    """

    def __str__(self):
        pass
    
    def readFinancialDocument(self):
        return super().readFinancialDocument()
    
    def getSerializedByteStream(self):
        return super().getSerializedByteStream()
    
    def createExcelRepresentation(self):
        return super().createExcelRepresentation()