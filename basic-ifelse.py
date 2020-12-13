# basic-ifelse.py

money = int(input('คุณมีเงินเท่าไร?: '))
from pprint import pprint # pretty print
import random

restaurant = {'high': [{'name': 'shitsuka sushi', 'price': 700,},
          			   {'name': 'Peporini', 'price': 500}],
 			  'medium': [{'name': 'เสวย', 'price': 200}, 
 			  			 {'name': 'รสดี', 'price': 250}],
 			  'low': [{'name': 'ป้าส้ม', 'price': 40},
         			  {'name': 'ป้าเล็กกระเพรา', 'price': 50}]}
#pprint(restaurant)
# money = 1000

if money >= 500:
	select = random.choice(restaurant['high'])
	print('คุณผู้หญิงทานร้าน{}ดีไหมครับ? ราคาค่าเริ่มต้น {} บาท'.format(select['name'],select['price']))
elif money >= 250:
	select = random.choice(restaurant['medium'])
	print('คุณพี่ทานร้าน{}ดีไหมครับ? ราคาค่าเริ่มต้น {} บาท'.format(select['name'],select['price']))
else:
	select = random.choice(restaurant['low'])
	print('พี่ทานร้าน{}ดีไหมครับ? ราคาค่าเริ่มต้น {} บาท'.format(select['name'],select['price']))
