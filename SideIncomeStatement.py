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
    def __init__(self, filepath:str):
        self.__filepath = filepath
        self.readFinancialDocument()

    def __str__(self):
        return f"Date: {self.__date}\nIncome Amount: {self.__incomeAmount}\nSource: {self.__source}"
    
    def readFinancialDocument(self):
        DATE = 0
        INCOMEAMOUNT = 1
        SOURCE = 2
        
        with open(self.__filepath, "r") as sideIncomeStatementTxt:
            lines = sideIncomeStatementTxt.readlines()

            dateString = lines[DATE][18:]
            self.__date = datetime.datetime.strptime(dateString.strip(), "%m/%d/%Y")

            incomeString = lines[INCOMEAMOUNT][16:]
            self.__incomeAmount = float(incomeString.strip())

            self.__source = lines[SOURCE][8:].strip()
    
    def getSerializedByteStream(self):
        return super().getSerializedByteStream()
    
    def createExcelRepresentation(self):
        return super().createExcelRepresentation();