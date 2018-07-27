class Kaiser:
	'''def __init__(self):
		pass'''
	def encryption(self):
		self.text=str(input('Please enter the plaintext to be encrypted\n请输入要加密的密明文\n'))
		self.move=int(input('Please enter the number of digits to move\n请输入要移动的位数\n'))
		self.textlist=list(self.text)
		self.textstr=''
		for i in range(len(self.textlist)):
			self.textlist[i]=chr(ord(self.textlist[i])+self.move)
			
		for i in range(len(self.textlist)):
			self.textstr+=self.textlist[i]
			
		print('加密后的文本为:（The encrypted text is）\n'+self.textstr)
		
	def Decrypt(self):
		print('This tools Kaiser decryption is generally considered to be the use of ciphertext should be alphabetical character, considering up and down fluctuations should not exceed 25., if there is a special need to change the parameters inside the range\n')
		print('本工具的凯撒解密考虑到一般应该都是利用密文应该都是字母字符，考虑上下波动应该不超过25.如有特殊需要可以更改range里面的参数\n')
		
		
		self.text1=str(input('Please enter the ciphertext to be decrypted\n请输入要解密的密文\n'))
		self.bottom=int(input('Please enter the lower bound to be decrypted. This should be a negative number. We recommend that it be preferably between -25~0.\n请输入要解密的下限，这应该是一个负数,我们建议它最好在-25~0之间\n'))
		self.top=int(input('Please enter the upper limit to be decrypted. This should be a positive number. We recommend that it be preferably between 0~+25.\n请输入要解密的上限，这应该是一个正数，我们建议它最好在0~+25之间\n'))
		self.textlist1=list(self.text1)
		for i in range(self.bottom,self.top):
			self.textstr1=''
			self.temporary=list(self.text1)
			for a in range(len(self.textlist1)):
				self.temporary[a]=chr(ord(self.textlist1[a])+i)
			for a in range(len(self.textlist1)):
				self.textstr1+=self.temporary[a]
			print('第'+str(i)+'次解密的结果为'+self.textstr1)
			self.textstr1=''

			
			
if __name__=="__main__":
	a=Kaiser()
	
	