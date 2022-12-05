#Defining the elements of the grocery shop
grocery = {
    "apple": [40,15],
    "banana": [30,10],
    "cherry":[70,20],
}
#Defining variables relates to the user bill
bill=[]
total=0

print("Welcome to ITI shop!\n")

while True:
	# selecting the mode 
	mode=int(input("Select mode, for customer press 1, for owner press 2, to exit press 0 : "))
    #customer mode
	if mode == 1:
		while True:
			print()
			print("To show our products press 1")
			print("To buy from our products press 2")
			print("To print the bill press 3")
			print("To exit press 0")
			choice=int(input())
			#showing the products
			if choice == 1 :
				for i in grocery:
					print(i, " costs ", grocery[i][1], " remaining ", grocery[i][0])
			#buying from the products
			elif choice == 2 :
				for i in grocery:
					print("How many "+i+"s do you want? " )
					quantity = int(input())
					grocery[i][0] = grocery[i][0] - quantity 
					bill.append(i)
					bill.append(grocery[i][1])
					bill.append(quantity)
					total += quantity*grocery[i][1]
				print("Products were purchased successfully")
             #printing the bill
			elif choice == 3 :
				print(bill, "Total=", total)
			#exit
			else:
				break
     # owner mode     
	elif mode == 2:
		while True:
			print()
			print("To add new products press 1")
			print("To show products press 2")
			print("To change cost press 3")
			print("To delete a product press 4")
			print("To exit press 0")
			choice=int(input())
			#showing products
			if choice == 2 :
				for i in grocery:
					print(i, " quantity: ", grocery[i][0], " cost: ", grocery[i][1])
			#adding new products
			elif choice == 1 :
				name = input("Enter product name : ")
				quantity = int(input("Enter product quantity : "))
				price = int(input("Enter product price : "))
				grocery[name]=[quantity,price]
				print("Product was added successfully")
			#changing the cost of any product
			elif choice == 3 :
				name = input("Enter the product name : ")
				new_price = int(input("Enter the new price : "))
				grocery[name][1]=new_price
				print("Cost changed successfully")
			#deleting a product
			elif choice == 4 :
				name = input("Enter the product name : ")
				del grocery[name]
				print("Product was deleted successfully")
			else:
				break
	else:
		break
