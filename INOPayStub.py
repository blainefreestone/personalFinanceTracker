import datetime, PyPDF2

'''
Members:
filepath:str
startDate:datetime
endDate:datetime
documentDate:datetime
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
        with open(self.__filepath, 'rb') as pdfFileObject:
            print("Not implemented")