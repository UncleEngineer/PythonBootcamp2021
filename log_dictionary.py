Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> fruit = ['แอปเปิ้ล','ส้ม','มะม่วง']
>>> print(fruit[1])
ส้ม
>>> fruits = {'japan':'เมล่อน','usa':'องุ่น','china':'แอปเปิ้ล'}
>>> print(fruits['japan'])
เมล่อน
>>> fruits['thailand'] = 'ทุเรียน'
>>> print(fruits)
{'japan': 'เมล่อน', 'usa': 'องุ่น', 'china': 'แอปเปิ้ล', 'thailand': 'ทุเรียน'}
>>> fruits['china'] = 'ลูกท้อ'
>>> print(fruits)
{'japan': 'เมล่อน', 'usa': 'องุ่น', 'china': 'ลูกท้อ', 'thailand': 'ทุเรียน'}
>>> fruit.append('ส้ม')
>>> print(fruit)
['แอปเปิ้ล', 'ส้ม', 'มะม่วง', 'ส้ม']
>>> for f in fruit:
... 	print(f)
... 
แอปเปิ้ล
ส้ม
มะม่วง
ส้ม
>>> for pollamai in fruit:
... 	print(pollamai)
... 
แอปเปิ้ล
ส้ม
มะม่วง
ส้ม
>>> print(fruits)
{'japan': 'เมล่อน', 'usa': 'องุ่น', 'china': 'ลูกท้อ', 'thailand': 'ทุเรียน'}
>>> for f in fruits:
... 	print(f)
... 
japan
usa
china
thailand
>>> for f in fruits.values():
... 	print(f)
... 
เมล่อน
องุ่น
ลูกท้อ
ทุเรียน
>>> for f in fruits.keys():
... 	print(f)
... 
japan
usa
china
thailand
>>> for k,v in fruits.items():
... 	print('ลูกค้าครับ รบกวนหยิบ{} ในกล่องที่มีป้ายติดไว้ว่า{}'.format(v,k))
... 
ลูกค้าครับ รบกวนหยิบเมล่อน ในกล่องที่มีป้ายติดไว้ว่าjapan
ลูกค้าครับ รบกวนหยิบองุ่น ในกล่องที่มีป้ายติดไว้ว่าusa
ลูกค้าครับ รบกวนหยิบลูกท้อ ในกล่องที่มีป้ายติดไว้ว่าchina
ลูกค้าครับ รบกวนหยิบทุเรียน ในกล่องที่มีป้ายติดไว้ว่าthailand
>>> mobile = {}
>>> mobile['samsung'] = {'title':'Samsung A51 2020 Ram 8/Rom 128GB',}
>>> mobile['samsung'] = {'title':'Samsung A51 2020 Ram 8/Rom 128GB','price':7660,'discount':2,'oriprice':7777,'star':5}
>>> print(mobile)
{'samsung': {'title': 'Samsung A51 2020 Ram 8/Rom 128GB', 'price': 7660, 'discount': 2, 'oriprice': 7777, 'star': 5}}
>>> mobile['iphone7'] = {'title':'iPhone7 128gb เครื่องแท้','price':10300,'color':['red','blue','yellow']}
>>> print(mobile)
{'samsung': {'title': 'Samsung A51 2020 Ram 8/Rom 128GB', 'price': 7660, 'discount': 2, 'oriprice': 7777, 'star': 5}, 'iphone7': {'title': 'iPhone7 128gb เครื่องแท้', 'price': 10300, 'color': ['red', 'blue', 'yellow']}}
>>> for m in mobile:
... 	print(m)
... 
samsung
iphone7
>>> for m,d in mobile.items():
... 	print(f'Mobile: {m}')
... 	print('Title: {}'.format(d['title']))
... 	print('Price: {} Baht'.format(d['price']))
... 	if 'color' in d:
... 		for c in d['color']:
... 			print(c)
... 	print('------')
... 
Mobile: samsung
Title: Samsung A51 2020 Ram 8/Rom 128GB
Price: 7660 Baht
------
Mobile: iphone7
Title: iPhone7 128gb เครื่องแท้
Price: 10300 Baht
red
blue
yellow
------
>>> print(mobile)
{'samsung': {'title': 'Samsung A51 2020 Ram 8/Rom 128GB', 'price': 7660, 'discount': 2, 'oriprice': 7777, 'star': 5}, 'iphone7': {'title': 'iPhone7 128gb เครื่องแท้', 'price': 10300, 'color': ['red', 'blue', 'yellow']}}
>>> del mobile['samsung']
>>> print(mobile)
{'iphone7': {'title': 'iPhone7 128gb เครื่องแท้', 'price': 10300, 'color': ['red', 'blue', 'yellow']}}
>>> del mobile['iphone7']
>>> print(mobile)
{}
>>> car = 'bmw'
>>> car == 'bmw'
True
>>> car = 'audi'
>>> car == 'bmw'
False
>>> car != 'bmw'
True
>>> 