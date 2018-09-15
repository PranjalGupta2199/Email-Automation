import textract
import re
import shutil
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf(file_path):
    ''' 
    Splits the timetable pdf into individual pages 
    '''
    infile = PdfFileReader(open(file_path, 'rb'))
    

    for i in range(infile.getNumPages()):
        p = infile.getPage(i)
        
        outfile = PdfFileWriter()
        outfile.addPage(p)
        
        split_page_path = os.path.join(os.getcwd(), 'Pages/page-%d.pdf' % i)

        with open(split_page_path, 'wb') as f:
            outfile.write(f)

def extract(folderName) : 

    try : 
        os.mkdir(folderName)
    except :
        pass

    mainPath = os.path.join(os.getcwd(), "Pages")
    savePath = os.path.join(os.getcwd(), folderName)

    totalFiles = len(os.listdir(mainPath))

    count = -1
    for i in range (totalFiles) :
        file = 'page-' + str(i) + '.pdf' 
        path = os.path.join(mainPath, file)
        txt = textract.process(path)
        txt = txt.decode('utf-8')

        infile = PdfFileReader(open(path, 'rb'))
        if ("BIRLA" in txt) :
            count += 1
            try : 
                if (count != 0) :
                    with open(os.path.join(savePath,fileName + '.pdf'), 'wb') as f :
                        outfile.write(f)
                else :
                    pass
            except :
                os.remove(os.path.join(savePath,fileName + '.pdf'))

            fileName = txt[txt.find('Ms.') + 4 : txt.find('\n', txt.find('Ms.'))]
            outfile = PdfFileWriter()
            outfile.addPage(infile.getPage(0))
        else :
            outfile.addPage(infile.getPage(0))
    try : 
        shutil.rmtree(mainPath)
    except :
        pass



if __name__ == '__main__' :
    try : 
        os.mkdir("Pages")
    except : 
        pass
    file_path = os.path.join(os.getcwd(), 'pdf files/ic.pdf')
    split_pdf(file_path)
    extract('IC')



