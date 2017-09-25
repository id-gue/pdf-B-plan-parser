import textract


text = textract.process("amtsblatt/abl_2017_38_4261_4376_online.pdf")

text_list = str(text).split(' ')

for idx, entry in enumerate(text_list):
	if('Bebauungsplan' in entry):
		print(text_list[idx+1])




bebauungsplan = text.find(str, beg=0, end=len(text))

print(bebauungsplan)