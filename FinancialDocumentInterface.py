import pickle

class FinancialDocumentInterface:
    def readFinancialDocument(self):
        """ Open and read financial document file and extract important data from the text. """
        pass

    def getSerializedByteStream(self):
        """ Serialize current instance of the specific financial document object in order to save to save file."""
        return pickle.dumps(self)

    def createExcelRepresentation(self):
        """ Creates an excel sheet that represents the data contained in the current instance of the class. """
        pass