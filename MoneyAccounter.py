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
    addSideIncomeStatemnt(incomeStatement:SideIncomeStatement)
        add...
    updateData(newIncome:float, newTithingPaid:float, newTaxDeducted=0)
        update...
    getFileRepresentation()
        get...
    """