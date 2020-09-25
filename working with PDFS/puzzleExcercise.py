# download the pdf from the google drive link and find the phone number
# that is in the document

import  PyPDF2
import  re

f = open('Find_the_Phone_Number.pdf','rb')

pdf = PyPDF2.PdfFileReader(f)
pdf.numPages
# print the number of pages in that pdf file
print(pdf.numPages)



pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ''

for n in range(pdf.numPages):

    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text+' '+page_text

re.search(pattern,all_text)

print(re.findall(pattern,all_text))

for match in re.finditer(pattern,all_text):
    print(match)

x = all_text[41790:41808+20]
print(x)
