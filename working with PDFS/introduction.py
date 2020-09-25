import PyPDF2
# rb = read binary
f = open('Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
# red number of pages in the pdf

print(pdf_reader.numPages)

print('\n')
# get page one
page_one = pdf_reader.getPage(0)
print(page_one)

# extra text in page one

page_one_text = page_one.extractText()
print(page_one_text)

f.close()

print('\n')
# Adding to the text to the pdf..
# Adding pages to a pdf

f = open('Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()

print(type(first_page))

pdf_writer.addPage(first_page)

pdf_output = open('Some_Brandnew_DOc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

# grap all the text in a pdf file

f = open('Working_Business_Proposal.pdf','rb')

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[4])