import datetime, fitz
from FinancialDocumentInterface import FinancialDocumentInterface

class INOPayStub(FinancialDocumentInterface):
    """ 
    Saves and represents the important information contained in a single In-N-Out paystub as a pdf. 
    
    ...

    Attributes
    ----------
    __filepath : str
        the filepath of the paystub as a pdf
    __preDeductionPay : float
        the total pay before deductions
    __netPay : float
        the total pay after deductions; this is the amount that arrives in the bank account
    __startDate : datetime
        the start date of the pay period of the paystub
    __endDate : datetime
        the end date of the pay period of the paystub
    __rate : float
        the rate of hourly pay of the pay period of the paystub
    __hours : float
        the total hours worked of the pay period of the paystub
    __deductions : dict
        <key> : string
            name of the deduction
        <value> : float
            amount of the deduction

    Methods
    -------
    readPayStub()
        Opens and reads the pdf at the filepath and sets member variables: __preDeductionPay, __netPay, __startDate, __endDate, __rate, __hours, and __deductions.
    getSerializeByteStream()
        Serializing this instance of the INOPayStub class as a pickle byte stream which can be saved to a save file.
    """

    def __init__(self, filepath:str):
        """ 
        Parameters
        ----------
        filepath : str
            the filepath of the paystub as a pdf
        """
        self.__filepath = filepath 
        self.readPayStub()
    
    def __str__(self):
        return f"Filepath: {self.__filepath}\nPre Deduction Pay: {self.__preDeductionPay}\nDeductions: {self.__deductions}\nNet Pay: {self.__netPay}\nStart Date: {self.__startDate}\nEnd Date: {self.__endDate}\nRate: {self.__rate}\nHours: {self.__hours}\n"

    def readFinancialDocument(self):
        """
        Opens and reads the pdf at the filepath and initializes member variables: __preDeductionPay, __netPay, __startDate, __endDate, __rate, __hours, and __deductions.
        Raises
        ------
        AssertionError as DeductionAmountsAndNamesDoNotMatch
            If the deductionNames and deductionAmounts lists do not have the same lengths (i.e., there isn't a deduction name for each deduction amount).
        """
        # Text block tuple indexes.
        BLOCK_NO = 5
        BLOCK_TEXT = 4
        # Elements of pdf file in text block numbers.
        DEDUCTIONSAMOUNT = 12
        PREDEDUCTIONPAY = 21
        NETPAY = 22
        DATES = 27
        RATE = 29
        HOURS = 31
        DEDUCTIONSNAME = 35

        # Open and access pdf file.
        payStubPdfObj = fitz.open(self.__filepath)
        for page in payStubPdfObj:
            # Divide pdf file into text block tuples.
            blocks = page.get_text("blocks")

            # Save pre-deduction pay as float. 
            self.__preDeductionPay = float(blocks[PREDEDUCTIONPAY][BLOCK_TEXT].strip())
            
            # Save net pay as float. 
            self.__netPay = float(blocks[NETPAY][BLOCK_TEXT].strip())

            # Parse and save start and end dates as datetime objects.
            datesString = blocks[DATES][BLOCK_TEXT].strip()
            dates = datesString.split(' - ')
            self.__startDate = datetime.datetime.strptime(dates[0], "%m/%d/%Y")
            self.__endDate = datetime.datetime.strptime(dates[1], "%m/%d/%Y")

            # Save rate as float. 
            self.__rate = float(blocks[RATE][BLOCK_TEXT].strip())

            # Save total hours as float. 
            self.__hours = float(blocks[HOURS][BLOCK_TEXT].strip())

            # Create two seperate lists of deduction amounts and deduction names. 
            deductionNames = list(filter(None, blocks[DEDUCTIONSNAME][BLOCK_TEXT].split("\n")))
            deductionAmounts = list(filter(None, blocks[DEDUCTIONSAMOUNT][BLOCK_TEXT].split("\n")))
            assert len(deductionAmounts) == len(deductionNames), "deductionAmountsAndNamesDoNotMatch" # Each name should correspond with an amount. List lengths should be the same.
            
            # Combine and save deduction amounts and deduction names as a dictionary.
            deductionsIndex = 0
            self.__deductions = {}
            while (deductionsIndex < len(deductionAmounts)):
                self.__deductions[deductionNames[deductionsIndex].strip()] = float(deductionAmounts[deductionsIndex].strip())
                deductionsIndex += 1

    def getSerializeByteStream(self):
        return super().getSerializedByteStream()
    
    def createExcelRepresentation(self):
        pass