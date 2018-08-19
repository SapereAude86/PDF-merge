from PyPDF2 import PdfFileMerger
import sys

pdfs = []
#loop through all pdf arguments
for x in sys.argv:
	if (x.endswith(".pdf")):
		pdfs.append(x)
#listing used pdfs
print(pdfs)
merger = PdfFileMerger()
print("merging files: " + str(sys.argv))
#start using the first argument given and append/merge subsequential pdf's given.
for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

#write a new pdf with all given pdf's
with open('result.pdf', 'wb') as fout:
    merger.write(fout)
