Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.', i)

	
No. 0
No. 1
No. 2
No. 3
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(90)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(180)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(135)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8 เหลี่ยมรูปที่',i)
	tao.left(36)

	
8 เหลี่ยมรูปที่ 0
8 เหลี่ยมรูปที่ 1
8 เหลี่ยมรูปที่ 2
8 เหลี่ยมรูปที่ 3
8 เหลี่ยมรูปที่ 4
8 เหลี่ยมรูปที่ 5
8 เหลี่ยมรูปที่ 6
8 เหลี่ยมรูปที่ 7
8 เหลี่ยมรูปที่ 8
8 เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> 