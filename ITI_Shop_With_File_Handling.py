#Defining the elements of the grocery shop deictionary
grocery = {
    "apple": [40,15],
    "banana": [30,10],
    "cherry":[70,20],
}

#Defining the employee information dictionary
employee={

"Ahmed":[25,1000,'Delivary Man'],
"Mohammed":[20,500,'HR'],
"Khaled" : [22,850,'Cashier'],
"Mahmoud":[30,2000,'Office boy'],
"Sameer" : [28,1500,'Sales'],}


# Defining variables related to the client bill
bill=[]
total=0

# ---------------------------------------------------------------------------------------------

# Defining the file.txt to add the the shop information to it
f1=open("ITI_shop.txt",'w+')
f1.write("-------------------------------------------------")
f1.write("\nWelcome to ITI grocery Shop !!\n")
f1.write("-------------------------------------------------")
f1.write("\nThis file includes all the grocery information\n")
f1.write("-------------------------------------------------\n")
f1.write("Initially our products include the following: \n")
for key in grocery:		
	f1=open("ITI_shop.txt",'a')
	f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
	f1.write("\n")
f1.close()


# Defining the file.txt to add the information of fired employee to it
f3=open("ITI_fired.txt",'w+')
f3.write("\nFired Employees are: \n")
f3.close()
				
# ---------------------------------------------------------------------------------------------

# Defining a loop to stay inside it while running the program
while True:

	print("\n-------------------------------")
	print("  Welcome to ITI Grocery Shop")
	print("-------------------------------")

	# selecting a mode 
	print("\nYou can select a mode from the following:")
	print ("Select Client Mode by enteing C")
	print ("Select Owner Mode by enteing O")
	print("Exit the system by entering E\n")
	mode=input("Enter your choice: ")
	
    # customer mode
	if mode == 'C':
	
		while True:
			#Dispalying the options of Client mode
			print()
			print("To show our products enter 's'")
			print("To buy from our products enter 'p'")
			print("To print the bill enter 'b'")
			print("To exit enter 'e'")
			
			#Choosing an option
			choice=input("\nEnter you choice: ")
			
			# showing available products when choosing 's'
			if choice == 's' :
				for i in grocery:
					print("Fruit Type:",i, " costs: ", grocery[i][1], " quantity: ", grocery[i][0])
				
				# Adding the info of the products to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nProducts include the following: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
				
				
			# buying from the products when choosing 'b'
			elif choice == 'p' :
				for i in grocery:
					#print("\nHow many "+i+"s do you want to buy? ")
					quantity = int(input("\nHow many "+i+"s do you want to buy? "))
					if quantity <= grocery[i][0] and quantity >=0:
						grocery[i][0] = grocery[i][0] - quantity
						bill.append(i)
						bill.append(grocery[i][1])
						bill.append(quantity)
						total += quantity*grocery[i][1]	
					else: 
						print("The quantity of "+i+"s is not valid")
						continue
				print("\nProducts were purchased successfully")
				
				# Adding the info of the remaining products to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nRemaining products after purchasing: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
				
				
             # printing the bill by choosing 'p'
			elif choice == 'b' :
				# adding the products info to the bill
				print(bill, "Total=", total)
				f2=open("ITI_bill.txt",'w+')
				f2.write("**************************************" )
				f2.write("\n*            ITI Shop Bill           *")      
				f2.write("\n*                                    *")
				f2.write("\n**************************************" )
				
				head=['Item','Cost','Quantity']
				col=3
				f2.write("\n")
				f2.write(f'{head[0] : <15}{head[1]: <15}{head[2]: <10}')
				f2.write("\n**************************************\n" )
				f2.write("\n")
				
				for f,s,t in zip(bill[::col],bill[1::col],bill[2::col]):
					f2.write(f'{f: <15}{s: <15}{ t: <10}')
					f2.write("\n")
				f2.write("\n**************************************\n")
				f2.write("                                        ")
				f2.write("\n                          Total= ")
				f2.write(str(total))
				f2.write("\n")
				f2.write("\n**************************************\n")
				f2.close()
				
				
			# exiting from Client mode
			elif choice == 'e':
				break
				
				
			# in case user enterd a wrong choice 
			else:
				print("\nWrong Choice!")
				continue
				
# ---------------------------------------------------------------------------------------------
				
     # owner mode     
	elif mode == 'O':
	
	#Dispalying the options of Owner mode
		while True:
			print()
			print("To add new products enter 'a'")
			print("To show products enter 's'")
			print("To change cost enter'c")
			print("To delete a product enter 'd'")
			print("To show employees enter 'm'")
			print("To add a new employee enter 'n'")
			print("To remove an employee enter 'r'")
			print("To exit enter 'e'\n")
			
			#Choosing an option
			choice=input("Enter your choice: ")
			
			
			# adding new products by entering 'a'
			if choice == 'a' :
				name = input("Enter product name : ")
				quantity = int(input("Enter product quantity : "))
				price = int(input("Enter product price : "))
				grocery[name]=[quantity,price]
				print("Product was added successfully")
				
				# Adding the info of all products (new and old) to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nOur products after addition: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
			
			
			# showing products by entering 's'
			elif choice == 's' :
				for i in grocery:
					print("Fruit Type:",i, " quantity: ", grocery[i][0], " cost: ", grocery[i][1])
					
				# Adding the info of the products to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nNow our products include the following: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
					
				
			# changing the cost of any product by entering 'c'
			elif choice == 'c' :
				name = input("Enter the product name : ")
				
				#checking if name exist in grocery dictionary
				if name in grocery:
					new_price = int(input("Enter the new price : "))
					grocery[name][1]=new_price
					print("Cost changed successfully")
					
				#in case the product wasn't in the grocery dictionary
				else:
					print("This Product doesn't exist!")
					continue
				
				# Adding the info of the products after changing the cost to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nOur products after changing the cost: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
				
				
			# deleting a product by entering 'd'
			elif choice == 'd' :
				name = input("Enter the product name : ")
				
				#checking if name exist in grocery dictionary
				if name in grocery:
					del grocery[name]
					print("Product was deleted successfully")
				
				#in case the product wasn't in the grocery dictionary
				else:
					print("This Product doesn't exist!")
					continue
				
				# Adding the info of the products after deleting to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nOur products after deleting: \n")
				for key in grocery:
					f1.write(f"Fruit type= {key}, Quantity= {grocery[key][0]}, Price={grocery[key][1]}.")
					f1.write("\n")
				f1.close()
					
					
			#Printing Emplyees info by entering 'm'
			elif choice == 'm':
				for j in employee:
					print(j,", Age= ",employee[j][0]," Salary= ",employee[j][1]," Title: ",employee[j][2])
				
				# Adding the employees info to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nEmployees are: \n")
				for key in employee:
					f1.write(f"Name= {key}, Age= {employee[key][0]}, Salary={employee[key][1]}, Title={employee[key][2]}.")
					f1.write("\n")
				f1.close()	
				
			
			# Adding new Emplyees by entering 'n'
			elif choice == 'n':
				n=input("Enter an emplyee name: ")
				n_1=int(input("Enter the emplyee age: "))
				n_2=int(input("Enter the emplyee salary: "))
				n_3=input("Enter the emplyee title: ")
				employee[n]=[n_1,n_2,n_3]
				print("Employee was added successfully")
				
				# Adding the employees info after addition to the file_txt
				f1=open("ITI_shop.txt",'a')
				f1.write("\nYour employees after addition: \n")
				for key in employee:
					f1.write(f"Name= {key}, Age= {employee[key][0]}, Salary={employee[key][1]}, Title={employee[key][2]}.")
					f1.write("\n")
				f1.close()
				
			
			# Removing Emplyees by entering 'r'
			elif choice == 'r':
				n = input("Enter the employee name : ")
				
				#checking if the emplyee name exist in the employee dictionary
				if n in employee:
					# Adding the fired employee info to a file_txt
					f3=open("ITI_fired.txt",'a')
					f3.write("\n")
					f3.write(f"Name= {n}, Age= {employee[n][0]}, Salary={employee[n][1]}, Title={employee[n][2]}.")
					f3.close()
					
					#deleting the employee info from employee dictionary
					del employee[n]
					print("Employee was deleted successfully")
					
					# Adding the employees info after removing to the file_txt
					f1=open("ITI_shop.txt",'a')
					f1.write("\nYour employees after deleting: \n")
					for key in employee:
						f1.write(f"Name= {key}, Age= {employee[key][0]}, Salary={employee[key][1]}, Title={employee[key][2]}.")
						f1.write("\n")
					f1.close()
					
				# in case the employee name didn't exist in employee dictionary
				else: 
					print ("This employee doesn't exist!")
					continue
			
			
			# exiting by entering 'e'
			elif choice == 'e':
				break
			
			
			# in case user entered any wrong option 
			else:
				print("\nWrong Choice!")
				continue
				
# ---------------------------------------------------------------------------------------------
				
	# exiting from the system by entering 'E'
	elif mode == 'E':
		break
	
	# if the user enters a choice not = 'C' or 'O' or 'E'
	else:
		print("\nWrong choice!")
		continue

# ---------------------------------------------------------------------------------------------

# printing the file.txt to display all the shop information line by line		
f1=open("ITI_shop.txt",'r')
# for L in f1:
	# print(L)
print(f1.readlines())
f1.close()	


