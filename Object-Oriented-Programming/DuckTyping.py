# Duck typing : It is a concept where the type of an object is determined by its behaviour not by its class
class InkjetPrinter:
    def PrinterDocument(self,document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def PrinterDocument(self,document):
        print("Laser printer printing : ",document)


class PDFWriter:
    def PrinterDocument(self,document):
        print(f"saving : {document} as PDF")

def StartPrinting(Device):

    Device.PrinterDocument("Marvellous notes")

def main():

    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()
