import PyPDF2


filename = 'amtsblatt/abl_2017_38_4261_4376_online.pdf'

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages

count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()



text_list =text.split(' ')

for idx, entry in enumerate(text_list):
	if('Bebauungsplan' in entry):
		print(text_list[idx+1])

    