from kaiser import Kaiser



print('This is a Python based open source encryption and decryption tool.The author is a cryptographic beginner, will gradually improve this tool according to the progress of learning. If you have any suggestions for improvement, you can contact me. \n')
print('                      	      author:blue and white from Different space safety\n')
print('                      	      e-mail:blueandwhite@yeah.net\n')
print('********************************************************************************\n')
print('这是一个一个开源的基于python的开源密码加密解密工具,作者是一个密码学初学者, 会给予自己的学习进度,逐渐完善这个工具.如果您有什么改进的意见可以联系我.\n')
print(' 					            作者：青花 form 异空间安全\n')
print('  					            e-mail:blueandwhite@yeah.net\n')



def usekaiser():
	
	print('Input digital 1 to encrypt Kaiser cipher\n输入数字1进行凯撒密码加密\n')
	print('Input number 2 for decryption of Kaiser cipher\n输入数字2进行凯撒密码解密\n')
	choice=int(input('Please enter your choice\n请输入您的选择\n'))
	a=Kaiser()
	
	if choice==1:
		a.encryption()
	if choice==2:
		a.Decrypt()
	

if __name__=='__main__':
	print('Please enter your choice according to the function\n根据功能请输入您的选择\n')
	print('Enter the number 1 to select the Kaiser password\n输入数字1，选择凯撒密码\n')
	
	
	choice=int(input('Please enter your choice\n请输入您的选择\n'))
	#try:
	if choice==1:
		usekaiser()
	if choice !=1:
		print("Input error please reenter!\n输入有误请重新输入!\n")
	#except:
		#print('Program error, please restart, if there are still errors, please contact me, you can put forward your amendment advice to me!\n程序错误，请重新启动，如果仍然有错误，请联系我，您可以提出您的修改意见给我！\n')