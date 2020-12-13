#basic-class.py

class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		#Call Function
		# self.AddEXP(10)

	def Hello(self):
		print('สวัสดีจ้าาาา ผมชื่อ{}'.format(self.name))

	def Coding(self):
		print('{}: กำลังเขียนโปรแกรม..'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print('- {} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
		print('- เรียนไป {} ครั้งแล้ว'.format(self.lesson))

	def AddEXP(self,score):
		self.exp += score # self.exp = self.exp + score
		self.lesson += 1


class SpecialStudent(Student):

	def __init__(self,name,father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill Gates','Thomas Edison']
		if father in mafia:
			self.exp += 100

	def AddEXP(self,score):
		self.exp += (score * 3)
		self.lesson += 1

	def AskEXP(self,score=10):
		print('ครู!! ขอคะแนนพิเศษให้ผมหน่อยสิสัก {} EXP'.format(score))
		self.AddEXP(score)


print('========1 Jan========')
student0 = SpecialStudent('Mark Zuckerberg','Bill Gates')
student0.AskEXP()
student0.ShowEXP()
student1 = Student('Albert')
print(student1.name)
student1.Hello()

print('------------')
student2 = Student('Steve')
print(student2.name)
student2.Hello()
print('========2 Jan========')
print('------uncle: ใครอยากเรียนโค้ดดิ้ง?---(ให้ 10 exp)----')
student1.AddEXP(10)

print('========3 Jan========')
student1.name = 'Albert Einstein'
print('ตอนนี้ exp ของแต่ละคนได้เท่าไรกันแล้ว')

print(student1.name, student1.exp)
print(student2.name, student2.exp)
print('========4 Jan========')

for i in range(5):
	student2.Coding()

student1.ShowEXP()
student2.ShowEXP()