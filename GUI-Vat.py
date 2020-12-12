from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมคำนวน vat')

# FONT ทั้งหมด
FONT1 = ('Angsana New',20)


#########ช่องกรอกข้อมูล (ชื่อสินค้า) ##########
L = ttk.Label(GUI,text='ชื่อสินค้า',font=FONT1).pack() # ข้อความแสดง

v_product = StringVar() # ตัวแปรสำหรับเก็บชื่อสินค้าตอนพิมพ์
E1 = ttk.Entry(GUI,textvariable=v_product,font=FONT1)
E1.pack()
#########ช่องกรอกข้อมูล (ราคาสินค้า) ##########
L = ttk.Label(GUI,text='ราคาสินค้า',font=FONT1).pack() # ข้อความแสดง

v_price = StringVar() # ตัวแปรสำหรับเก็บราคาสินค้าตอนพิมพ์
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1)
E2.pack()
#########ช่องกรอกข้อมูล (จำนวน) ##########
L = ttk.Label(GUI,text='จำนวน',font=FONT1).pack() # ข้อความแสดง

v_quantity = StringVar() # ตัวแปรสำหรับเก็บจำนวนสินค้าตอนพิมพ์
E3 = ttk.Entry(GUI,textvariable=v_quantity,font=FONT1)
E3.pack()
######### ปุ่มกดเพื่อคำนวณ ##########
def Calc(event=None):
	# int() คำสั่งแปลงข้อความเป็นตัวเลข '2' -- > 2
	# print( type( int( v_price.get() ) ) )
	product = v_product.get()
	price = int(v_price.get())
	quantity = int(v_quantity.get())
	total = price * quantity

	vat7 = total * (7/107)
	nettotal = total * (100/107)

	print('ราคาก่อน vat: {:.2f} (vat 7%: {:.2f})'.format(nettotal,vat7))

	v_result.set('สินค้า: {} {} ชิ้นทั้งหมด {} บาท ({} บาท/ชิ้น)\nราคาสินค้า: {:.2f}.- VAT7%: {:.2f}.-'.format(product,
																							quantity,total,
																							price,
																							nettotal,vat7))
B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

E3.bind('<Return>',Calc)

######### ผลลัพท์จากการคำนวณ ##########
v_result = StringVar()
v_result.set('<<<ผลลัพท์โชว์จุดนี้>>>') # โชว์ข้อมูลเริ่มต้น

R1 = ttk.Label(GUI,textvariable=v_result,font=FONT1)
R1.pack()


GUI.mainloop()