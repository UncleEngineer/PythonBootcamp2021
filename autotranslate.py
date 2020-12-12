#autotranslate.py

# pip install easyread
# pip install openpyxl
from easyread.translator import Translate
from openpyxl import Workbook
from datetime import datetime

article = open('article.txt','r',encoding='utf-8')
article = article.read()
article = article.split()

print('Count: ',len(article))
result = []

for word in article:
	#print(word)
	res = Translate(word)
	if res != None:
		#print(res['meaning'])
		result.append([word,res['meaning']])
		# result.append(['Cat','[N] แมว'])

#print(result)
excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab','Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))
