# รันซ้ำตามตัวเลขที่ต้องการ
import time

print(list(range(1,10+1)))
for i in range(10):
	print(i)
print('================')
for i in range(1,11):
	print(i)
	#time.sleep(1)
	print('----------')
print('================')

for i in range(1,10,2):
	print(i)
	print('----------')

print('================')
# แสดงผลสิ่งที่อยู่ในลิสต์
friend = ['Albert','Steve','Ada','Edison']
for f in friend:
	print(f)
print('================')
# แสดงผลสิ่งที่อยู่ในลิสต์เฉพาะตัว
friend = ['Albert','Steve','Ada','Edison']
for f in friend:
	if f == 'Albert':
		print(f)