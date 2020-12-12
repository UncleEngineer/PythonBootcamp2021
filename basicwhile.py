money = 998
transfer = 2000

# print('Condition: ', money < transfer)
print('ต้องการโอน', transfer , '(มีค่าบริการ 15 บาท)')
while money < (transfer + 15 ) :
	print('คุณมีเงิน', money)
	print('กรุณาโอนเงินเข้าบัญชี เงินไม่พอโอน')
	getmoney = int(input('ฝากเงินเท่าไร?: '))
	money = money + getmoney # 998 + xxx
	print('---')

print('คุณมีเงิน', money)
print('โอนเงินได้เลย')
print('เหลือเงินในบัญชี: ', money - (transfer+15))