# Calculator with 2 modes: Scientific and Programming with only 2 input numbers

print ("Welcome\n")
m=str(input ("Enter 'S' to start the scientific mode or 'P' to start the programming mode: ")) #choosing between 2 modes
f=0
while f==0 :
	if(m == 'S'):
	#choosing between differnt caculation configurations
		num=input("For decimal calc. press 1, for binary calc. press 2, for hexadecimal calc. press 3, to exit press anything else: ")
		
		if (num == '1'):
			a,b,op=input("Enter number 1, number 2, and the operation separated by a space: ").split(" ",3)
			#addition operation - D
			if(op == '+'):
				sum=float(a)+float(b)
				print(sum)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#substraction operation - D
			elif(op =='-'):
				sub=float(a)-float(b)
				print(sub)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Multiplication operation - D
			elif(op =='*'):
				mul=float(a)*float(b)
				print(mul)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Division operation - D
			elif(op == '/'):
				div=float(a)/float(b)
				print(div)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Exponential operation - D
			elif(op == '**'):
				exp=float(a)**float(b)
				print(exp)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue 
				else:
					break
			#Reminder - D
			elif(op == '%'):
				mud=float(a)%float(b)
				print(mud)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue 
				else:
					break
    
		elif (num == '2'):
			c,d,o=input("Enter number 1 in binary, number 2 in binary, and the operation separated by a space: ").split(" ",3)
			#addition operation - B
			if(o == '+'):
				sum=bin((int(c,2))+(int(d,2)))
				print(sum)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Substraction operation - B
			if(o == '-'):
				sumn=bin((int(c,2))-(int(d,2)))
				print(sumn)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Multiplication operation - B
			if (o == '*'):
				muly=bin((int(c,2))*(int(d,2)))
				print(muly)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Division operation - B
			if (o == '/'):
				divh= bin(int((c,2))/int((d,2)))
				print(divh)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Reminder - B
			if (o == '%'):
				remh= bin(int((c,2))%int((d,2)))
				print(remh)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Exponential operation - B
			if (o == '**'):
				exph=bin((int(c,2))**(int(d,2)))
				print(exph)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
					
		elif (num == '3'):
			c,d,o=input("Enter number 1 in hexa, number 2 in hexa, and the operation separated by a space: ").split(" ",3)
			#Addition operation - H
			if(o == '+'):
				sum=hex((int(c,16))+(int(d,16)))
				print(sum)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Substraction operation - H
			if(o == '-'):
				sumn=hex((int(c,16))-(int(d,16)))
				print(sumn)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Multiplication operation - H
			if (o == '*'):
				muly=hex((int(c,16))*(int(d,16)))
				print(muly)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Division operation - H
			if (o == '/'):
				divh= hex((int(c,16))/(int(d,16)))
				print(divh)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Reminder - H
			if (o == '%'):
				remh=hex((int(c,16))%(int(d,16)))
				print(remh)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break
			#Exponential operation - H
			if (o == '**'):
				exph=hex((int(c,16))**(int(d,16)))
				print(exph)
				c=str(input("Do you want to continue? "))
				if(c == 'yes'):
					continue
				else:
					break	
		else:
			break;	

	elif (m=='P'):			
		op=input("Enter any bitwise operation: ")
		
		#Bitwise and operator
		if(op == '&'):
			x,y=input("Enter 2 numbers separated by a space: ").split(" ",2)
			an= int(x) & int(y)
			print("Your answer in decimal= ",an)
			ban=bin(an)
			han=hex(an)
			print("The answer in binary= ",ban," and in hexa= ",han)
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue
			else:
				break
		#Bitwise or operator
		elif(op =='|'):
			x,y=input("Enter 2 numbers separated by a space: ").split(" ",2)
			on= int(x)|int(y)
			print("Your answer in decimal= ",on)
			ban=bin(on)
			han=hex(on)
			print("The answer in binary= ",ban," and in hexa= ",han)
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue
			else:
				break
		#Bitwise xor operator
		elif(op =='^'):
			x,y=input("Enter 2 numbers separated by a space: ").split(" ",2)
			xon= int(x)^int(y)
			print("Your answer in decimal= ",xon)
			ban=bin(xon)
			han=hex(xon)
			print("The answer in binary= ",ban," and in hexa= ",han)
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue
			else:
				break
		#Bitwise not operator
		elif(op == '~'):
			x=input("Enter a number to complement: ")
			notx= ~(int(x))
			print("Your answer in decimal= ",notx)
			ban=bin(notx)
			han=hex(notx)
			print("The answer in binary= ",ban," and in hexa= ",han)
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue
			else:
				break
		#Bitwise shift left operator
		elif(op == '<<'):
			x,y=input("Enter a number, than the value of any shift you want separated by a space: ").split(" ",2)
			shifl= int(x) << int(y)
			print("Your answer in decimal= ",shifl)
			ban=bin(shifl)
			han=hex(shifl)
			print("The answer in binary= ",ban," and in hexa= ",han)
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue 
			else:
				break
		#Bitwise shift right operator
		elif(op == '>>'):
			x,y=input("Enter a number, than the value of any shift you want separated by a space: ").split(" ",2)
			shifr= int(x) >> int(y)
			print("Your answer in decimal= ",shifr)
			ban=bin(shifr)
			han=hex(shifr)
			print("The answer in binary= ",ban," and in hexa= ",han)				
			c=str(input("Do you want to continue? "))
			if(c == 'yes'):
				continue 
			else:
				break
		else:
			print("This operation is not valid")
			break
	else:
		print("The Caculator doesn't support this mode")
		break
