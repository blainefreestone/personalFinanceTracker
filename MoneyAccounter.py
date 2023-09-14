from INOPayStub import INOPayStub
from TithingSlip import TithingSlip
from SideIncomeStatement import SideIncomeStatement

class MoneyAccounter:
    """
    Calculates and saves data from various types of financial documents in lists. 

    ...

    Attributes
    ----------
    __INOPayStubs : list<INOPayStub>
        list of INOPayStub objects
    __tithingSlips : list<TithingSlip>
        list of TithingSlip objects
    __sideIncomeStatements : list<SideIncomeStatement>
        list of SideIncomeStatement objects
    __totalIncome : float
        total income reported in all financial documents
    __totalTithingOwed : float
        total amount of tithing that should be paid based on total income
    __totalTithingPaid : float
        total amount of tithing paid according to all TithingSlip objects
    __totalTaxDeducted : float
        total amount of tax deducted from all forms of income reported in financial documents

    Methods
    -------
    addINOPayStub(payStub:INOPayStub)
        add...
    addTithingSlip(tithingSlip:TithingSlip)
        add...
    addSideIncomeStatement(incomeStatement:SideIncomeStatement)
        add...
    updateData(newIncome:float, newTithingPaid:float, newTaxDeducted=0)
        update...
    getFileRepresentation()
        get...
    """

    def __init__(self):
        self.__INOPayStubs = []
        self.__tithingSlips = []
        self.__sideIncomeStatements = []
        self.__totalIncome = 0
        self.__totalTithingOwed = 0
        self.__totalTithingPaid = 0
        self.__totalTaxDeducted = 0

    def addINOPayStub(self, payStub:INOPayStub):
        self.__INOPayStubs.append(payStub)

        self.__INOPayStubs.sort(key=lambda x : x.getEndDate())

    def addTithingSlip(self, tithingSlip:TithingSlip):
        self.__tithingSlips.append(tithingSlip)
        self.__tithingSlips.sort(key=lambda x : x.getDate())

    def addSideIncomeStatement(self, incomeStatement:SideIncomeStatement):
        self.__sideIncomeStatements.append(SideIncomeStatement)
        self.__sideIncomeStatements.sort(key=lambda x : x.getDate())
        
    def updateData(self, newIncome:float=0, newTithingPaid:float=0, newTaxDeducted:float=0):
        self.__totalIncome += newIncome
        self.__totalTithingOwed += newIncome * .1

        self.__totalTithingPaid += newTithingPaid
        self.__totalTithingOwed -= newTithingPaid

        self.__totalTaxDeducted += newTaxDeducted
        