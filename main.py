from INOPayStub import INOPayStub
from TithingSlip import TithingSlip
from SideIncomeStatement import SideIncomeStatement

def main():
    payStub = INOPayStub("payStub.pdf")
    payStub.createExcelRepresentation()

main()