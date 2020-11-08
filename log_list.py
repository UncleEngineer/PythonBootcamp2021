Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> print(garage[2])
izusu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzuki']
>>> garage.insert(1,'benz')
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> print(garage[-1])
suzuki
>>> print(garage[-2])
benz
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> print(garage)
['toyota', 'benz']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> users.sort()
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse=True)
>>> users
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in users.reverse():
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for u in users.reverse():
TypeError: 'NoneType' object is not iterable
>>> users.reverse()
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+u)

	
สวัสดี p
สวัสดีp
สวัสดี n
สวัสดีn
สวัสดี b
สวัสดีb
สวัสดี t
สวัสดีt
สวัสดี r
สวัสดีr
สวัสดี z
สวัสดีz
>>> 