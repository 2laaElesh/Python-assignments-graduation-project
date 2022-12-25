''' " Pola And Ramy 2sap Shop " '''

print("-------------------------------")
print("\nWelcome to Pola And Ramy 2sap Shop")
print("-------------------------------")

#Defining 2sap types of the Pola and Ramy shop
asap = {
	"L":15,
	"M":10,
	"S":5,}
	
		
		
# Defining a txt_file to write the following inside it
f1=open("Shop_2.txt",'w+')
f1.write("-------------------------------------------------")
f1.write("\nWelcome to Pola And Ramy 2sap Shop !!\n")
f1.write("-------------------------------------------------")
f1.write("\nThis file includes all the data about the shop sales\n")
f1.write("-------------------------------------------------\n")
f1.close()


# Defining a loop to choose 3sap type and add it to the txt_file
while True:

	c = input("\nEnter M to open the menu of this shop: ")
	
	# if the user enters M the main menu will be dispalyed
	if c == 'M':
		print("\n***Main Menu***")
		print("\nTo select 2sap size enter S")
		print("To exit enter E ")
		
		choice=input("\nChoose any of the choices above: ")
		
		# E to exit
		if choice == 'E':
			break;
			
		# 1 to display the 2sap sizes
		elif choice == 'S':
			print("\nFor large size enter L")
			print("For Medium size enter M")
			print("For Small size enter S")
		
			t=input("\nChoose a size: ")
			
			# L = large 2sap size 
			if t == 'L':
				key=t
				
				q=input("\nDo you confirm payment (enter y to confirm)? ")
				# if the user confirms the payment information will be added to the file_txt
				if q == 'y':
					f1=open("Shop_2.txt",'a')
					f1.write("\n")
					f1.write(f"Size= {key}, Payment= {asap[key]}.")
					f1.close()
				
				# if paymeny is not confirmed the loop will be terminated
				else:
					break;
			
			# M = Medium 2sap size 
			elif t=='M':
				key=t
				
				q=input("\nDo you confirm payment (enter y to confirm)? ")
				# if the user confirms the payment information will be added to the file.txt
				if q == 'y':
					f1=open("Shop_2.txt",'a')
					f1.write("\n")
					f1.write(f"Size= {key}, Payment= {asap[key]}.")
					f1.close()
				
				# if paymeny is not confirmed the loop will be terminated
				else:
					break;
			
			# S = Small 2sap size 
			elif t=='S':
				key=t
				
				q=input("\nDo you confirm payment (enter y to confirm)? ")
				# if the user confirms the payment information will be added to the file.txt
				if q == 'y':
					f1=open("Shop_2.txt",'a')
					f1.write("\n")
					f1.write(f"Size= {key}, Payment= {asap[key]}.")
					f1.close()
					
				# if paymeny is not confirmed the loop will be terminated
				else:
					break;
			
			# if the user enters a choice not = L or M or S
			else:
				print("\nInvalid choice")
				# Asking the user if he wants to try again in case the choice was wrong
				a=input("\n Do you want to try again (enter y to try again)? ")
				if a == 'y':
					continue;
				else:
					break;
					
		# if the user enters any thing other than 0,1
		else:
			print("\nInvalid choice")
			# Asking the user if he wants to try again in case the choice was wrong
			a=input("\n Do you want to try again (enter y to try again)? ")
			if a == 'y':
				continue;

			else:
				break;
				
	# if the user enters anything other than M for the main menu	
	else:
		print("\nInvalid choice")
		# Asking the user if he wants to try again in case the choice was wrong
		a=input("\n Do you want to try again (enter y to try again)? ")
		if a == 'y':
			continue;

		else:
			break;



