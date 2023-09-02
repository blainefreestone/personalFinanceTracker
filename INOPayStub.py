import datetime, fitz

'''
Members:
filepath:str
startDate:datetime
endDate:datetime
hours:float
rate:float
preDeductionPay:float
deductions:dict(name:str, amount:float)
netPay:float

Methods:
readPayStub()
'''

class INOPayStub:
    
    def __init__(self, filepath):
        self.__filepath = filepath
        self.readPayStub()
    
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
            
            for block in blocks:
                if block[BLOCK_NO] not in (12, 21, 22, 27, 29, 31, 35, 39):
                    continue

                print(f"{block[BLOCK_NO]}) {block[BLOCK_TEXT].strip()}")
            
payStub = INOPayStub("payStub.pdf")