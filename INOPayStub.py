import datetime, fitz

class INOPayStub:
    
    def __init__(self, filepath):
        self.__filepath = filepath
        self.readPayStub()
    
    def __str__(self):
        return f"Filepath: {self.__filepath}\nPre Deduction Pay: {self.__preDeductionPay}\nDeductions: {self.__deductions}\nNet Pay: {self.__netPay}\nStart Date: {self.__startDate}\nEnd Date: {self.__endDate}\nRate: {self.__rate}\nHours: {self.__hours}\n"

    def readPayStub(self):
        BLOCK_NO = 5
        BLOCK_TEXT = 4

        DEDUCTIONSAMOUNT = 12
        PREDEDUCTIONPAY = 21
        NETPAY = 22
        DATES = 27
        RATE = 29
        HOURS = 31
        DEDUCTIONSNAME = 35

        payStubPdfObj = fitz.open(self.__filepath)
        for page in payStubPdfObj:
            blocks = page.get_text("blocks")

            self.__preDeductionPay = float(blocks[PREDEDUCTIONPAY][BLOCK_TEXT].strip())
            
            self.__netPay = float(blocks[NETPAY][BLOCK_TEXT].strip())

            datesString = blocks[DATES][BLOCK_TEXT].strip()
            dates = datesString.split(' - ')
            self.__startDate = datetime.datetime.strptime(dates[0], "%m/%d/%Y")
            self.__endDate = datetime.datetime.strptime(dates[1], "%m/%d/%Y")

            self.__rate = float(blocks[RATE][BLOCK_TEXT].strip())

            self.__hours = float(blocks[HOURS][BLOCK_TEXT].strip())

            self.__deductions = {}
            deductionNames = list(filter(None, blocks[DEDUCTIONSNAME][BLOCK_TEXT].split("\n")))
            deductionAmounts = list(filter(None, blocks[DEDUCTIONSAMOUNT][BLOCK_TEXT].split("\n")))
            assert len(deductionAmounts) == len(deductionNames), "deductionAmountsAndNamesDoNotMatch"
            deductionsIndex = 0
            while (deductionsIndex < len(deductionAmounts)):
                self.__deductions[deductionNames[deductionsIndex].strip()] = float(deductionAmounts[deductionsIndex].strip())
                deductionsIndex += 1

payStub = INOPayStub("payStub.pdf")
print(payStub)