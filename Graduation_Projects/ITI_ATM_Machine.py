# This program is an ATM Machine implemented using tkinter


# importing the libraries needed in the program
import tkinter as tk
import time

# defining current balance variable
current_balance = 2000

class SampleApp(tk.Tk):
	
	# init function is used to define the container used in the program
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# Defining shared data between the container as input from user 
		self.shared_data = {'Balance':tk.IntVar()}
		# Defining the container and its specifications
		container = tk.Frame(self,width='250',height='250')
		self.resizable(0,0)
		container.pack(side="top", fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		#Defining the frames/ windows inside the container
		self.frames = {}
		for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
            # put all of the pages in the same location the one on the top of the stacking order will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
		# always start the program with the start page
		self.show_frame("StartPage")
	
	# show frame function is used to display a specific frame 
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):
	
	# Defining the init function for start page window 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='#f3f3f3')
		self.controller = controller
		
		# Adding characteristics to the frame such as title, state, and photo icon 
		self.controller.title('ITI ATM Machine')
		self.controller.state('zoomed')
		self.controller.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))

		# Adding heading label inside the frame which include text, font, foreground, background and packing 
		heading_label = tk.Label(self,
													text='  ATM Machine',
                                                    font=('orbitron',40,'bold'),
													foreground='#990000',
													background='#f3f3f3')
		heading_label.pack(pady=50)
		# adding a photo and sampling it 
		ITI_photo = tk.PhotoImage(file='ITI.png')
		ITI_photo=ITI_photo.subsample(5,5)
		# defining a label to the photo and placing it
		ITI_label = tk.Label(image=ITI_photo)
		ITI_label.place(x=420,y=5)
		# adding the photo to the label
		ITI_label.image = ITI_photo

		# adding a password label with a specified text, font, background color, foreground color, and packing 
		password_label = tk.Label(self,
													text='Enter your password:',
													font=('orbitron',15),
													bg='#cccccc',
													fg='black')
		password_label.pack(fill='x')
		# adding a password frame with a background color and packing
		password_frame = tk.Frame(self,bg='#666666')
		password_frame.pack(fill='both',expand=True)
		
		# defining a variable to take the input from user
		my_password = tk.StringVar()
		# adding a password entry box with specified font, width and packing
		password_entry_box = tk.Entry(password_frame,
													textvariable=my_password,
													font=('orbitron',12),
													width=25)								  
		password_entry_box.focus_set()
		password_entry_box.pack(pady=15,ipady=10)
		# this function is used to hide the password and show it as '***'
		def handle_focus_in(_):
			password_entry_box.configure(fg='black',show='*')
		# binding the entry box with handle_focus_in function
		password_entry_box.bind('<FocusIn>',handle_focus_in)
		# this function is used to check the password and print a message in incorrect_password label
		def check_password():
			if my_password.get() == '123':
				my_password.set('')
				incorrect_password_label['text']=''
				controller.show_frame('MenuPage')
			else:
				incorrect_password_label['text']='Incorrect Password'
		# adding enter button to confirm the password. The button has a sepcified text, command, releif, boardwith etc
		enter_button = tk.Button(password_frame,
													text='Confirm',
													command=check_password,
													relief='ridge',
													borderwidth = 3,
													width=25,
													height=2)
		enter_button.pack(pady=15)
		# adding incorrect password label with sepcified text, font, fg, bg, anchor and packing
		incorrect_password_label = tk.Label(self,
													text='',
													font=('orbitron',13),
													fg='Black',
													bg='#666666',
													anchor='n')
													
		incorrect_password_label.pack(fill='both',expand=True)


		# adding a bottom frame with specific releif, boardwith, bg, and packing
		bottom_frame = tk.Frame(self,relief='raised',borderwidth=3,bg='black')
		bottom_frame.pack(fill='x',side='bottom')
		# adding visa photo to the bottom frame
		visa_photo = tk.PhotoImage(file='visa.png')
		visa_photo = visa_photo.subsample(15,15)
		visa_label = tk.Label(bottom_frame,image=visa_photo,bg='black')
		visa_label.pack(side='left')
		visa_label.image = visa_photo
		# adding mastercard photo to the bottom frame
		mastercard_photo = tk.PhotoImage(file='credit-card.png')
		mastercard_photo = mastercard_photo.subsample(15,15)
		mastercard_label = tk.Label(bottom_frame,image=mastercard_photo,bg='black')
		mastercard_label.pack(side='left')
		mastercard_label.image = mastercard_photo
		# adding american_express photo to the bottom frame
		american_express_photo = tk.PhotoImage(file='american-express.png')
		american_express_photo = american_express_photo.subsample(15,15)
		american_express_label = tk.Label(bottom_frame,image=american_express_photo,bg='black')
		american_express_label.pack(side='left')
		american_express_label.image = american_express_photo
		# adding paypal photo to the bottom frame
		paypal_photo = tk.PhotoImage(file='paypal.png')
		paypal_photo = paypal_photo.subsample(15,15)
		paypal_label = tk.Label(bottom_frame,image=paypal_photo,bg='black')
		paypal_label.pack(side='left')
		paypal_label.image = paypal_photo
		# tick function is used to display time 
		def tick():
			current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
			time_label.config(text=current_time)
			time_label.after(200,tick)
        # adding a time label to show time inside the bottom frame
		time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='white',bg='black')
		time_label.pack(side='right')
		# calling tick function to display time
		tick()
      
	  
class MenuPage(tk.Frame):
	
	# Defining the init function for main menu page window 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='#f3f3f3')
		self.controller = controller
		# Adding heading label inside the frame which include text, font, foreground, background and packing 
		heading_label = tk.Label(self,
													text='  ATM Machine',
                                                    font=('orbitron',40,'bold'),
													foreground='#990000',
													background='#f3f3f3')
		heading_label.pack(pady=50)
		# adding a photo and sampling it 
		ITI_photo = tk.PhotoImage(file='ITI.png')
		ITI_photo=ITI_photo.subsample(5,5)
		# defining a label to the photo and placing it
		ITI_label = tk.Label(image=ITI_photo)
		ITI_label.place(x=420,y=5)
		# adding the photo to the label
		ITI_label.image = ITI_photo
		# adding main menu label with a specified text, font, fg, bg color, and packing 
		main_menu_label = tk.Label(self,
													text='Make a selection:',
													font=('orbitron',15),
													fg='Black',
													bg='#cccccc')
		main_menu_label.pack(fill= 'x')
		
		
		# adding a middle frame with a background color and packing 
		middle_frame = tk.Frame(self,bg='#666666')
		middle_frame.pack(fill='both',expand=True)
		# withdraw function is used to display WithdrawPage 
		def withdraw():
			controller.show_frame('WithdrawPage')

        # adding withdraw button (to middle frame) with specific text,command,releif,boarderwidth,width etc ...
		withdraw_button = tk.Button(middle_frame,
													text='Withdraw',
													command=withdraw,
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)								
		withdraw_button.grid(row=0,column=0,pady=15)
		# deposit function is used to display DepositPage 
		def deposit():
			controller.show_frame('DepositPage')
        # adding deposit button (to middle frame) with specific text,command,releif,boarderwidth,width etc ...  
		deposit_button = tk.Button(middle_frame,
													text='Deposit',
													command=deposit,
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)							
		deposit_button.grid(row=1,column=1,pady=15)
		# balance function is used to display BalancePage
		def balance():
			controller.show_frame('BalancePage')
        # adding balance button (to middle frame) with specific text,command,releif,boarderwidth,width etc ...  
		balance_button = tk.Button(middle_frame,
													text='Balance',
													command=balance,
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)						
		balance_button.grid(row=2,column=2,pady=15)
		# exit function is used to display StartPage
		def exit():
			controller.show_frame('StartPage')
        # adding exit button (to middle frame) with specific text,command,releif,boarderwidth,width etc ...  
		exit_button = tk.Button(middle_frame,
													text='Exit',
													command=controller.destroy,
													relief='raised',
													borderwidth=3,
													width=35,
													height=5)
		exit_button.grid(row=3,column=3,pady=15)
		
		
		# adding a buttom frame with a background color and packing
		bottom_frame = tk.Frame(self,relief='raised',borderwidth=3,bg='black')
		bottom_frame.pack(fill='x',side='bottom')
		# adding visa photo to the bottom frame
		visa_photo = tk.PhotoImage(file='visa.png')
		visa_photo = visa_photo.subsample(15,15)
		visa_label = tk.Label(bottom_frame,image=visa_photo,bg='black')
		visa_label.pack(side='left')
		visa_label.image = visa_photo
		# adding mastercard photo to the bottom frame
		mastercard_photo = tk.PhotoImage(file='credit-card.png')
		mastercard_photo = mastercard_photo.subsample(15,15)
		mastercard_label = tk.Label(bottom_frame,image=mastercard_photo,bg='black')
		mastercard_label.pack(side='left')
		mastercard_label.image = mastercard_photo
		# adding american_express photo to the bottom frame
		american_express_photo = tk.PhotoImage(file='american-express.png')
		american_express_photo = american_express_photo.subsample(15,15)
		american_express_label = tk.Label(bottom_frame,image=american_express_photo,bg='black')
		american_express_label.pack(side='left')
		american_express_label.image = american_express_photo
		# adding paypal photo to the bottom frame
		paypal_photo = tk.PhotoImage(file='paypal.png')
		paypal_photo = paypal_photo.subsample(15,15)
		paypal_label = tk.Label(bottom_frame,image=paypal_photo,bg='black')
		paypal_label.pack(side='left')# adding american_express photo to the bottom frame
		paypal_label.image = paypal_photo
		# tick function is used to display time
		def tick():
			current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
			time_label.config(text=current_time)
			time_label.after(200,tick)
        # adding a time label to show time inside the bottom frame   
		time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='white',bg='black')
		time_label.pack(side='right')
		# calling tick function to display time
		tick()


class WithdrawPage(tk.Frame):
    
	# Defining the init function for Withdraw page window
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='#f3f3f3')
		self.controller = controller
		# Adding heading label inside the frame which include text, font, foreground, background and packing 
		heading_label = tk.Label(self,
													text='  ATM Machine',
                                                    font=('orbitron',40,'bold'),
													foreground='#990000',
													background='#f3f3f3')
		heading_label.pack(pady=50)
		# adding a photo and sampling it 
		ITI_photo = tk.PhotoImage(file='ITI.png')
		ITI_photo=ITI_photo.subsample(5,5)
		# adding the photo to the label
		ITI_label = tk.Label(image=ITI_photo)
		ITI_label.place(x=420,y=5)
		# adding the photo to the label
		ITI_label.image = ITI_photo
		# adding choose amount label with a specified text, fonr, bg, fg and packing
		choose_amount_label = tk.Label(self,
													text='Choose the amount of money you want to withdraw',
													font=('orbitron',15),
													fg='Black',
													bg='#cccccc')
		choose_amount_label.pack(fill='x')
		# adding a middle frame with a background color and packing 
		middle_frame = tk.Frame(self,bg='#666666')
		middle_frame.pack(fill='both',expand=True)
		# withdraw function is used to decrement the balance with amount variable
		def withdraw(amount):
			# Using the current balance vriable as global to change its value
			global current_balance
			# checking if the balance is enough to make withdraw 
			if amount <= current_balance:
				current_balance -= amount
				controller.shared_data['Balance'].set(current_balance)
				balance_label['text']='Withdraw is done successfully !'
			# in case if it wasn't enough dispaly that to user
			else:	
				balance_label['text']='Balance is not enough!'
		# adding 100 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		one_hundred_button = tk.Button(middle_frame,
													text='100',
													command=lambda:withdraw(100),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)				
		one_hundred_button.place(x=10,y=25)
		# adding 200 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		two_hundred_button = tk.Button(middle_frame,
													text='200',
													command=lambda:withdraw(200),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)		
		two_hundred_button.place(x=500,y=25)
		# adding 300 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		three_hundred_button = tk.Button(middle_frame,
													text='300',
													command=lambda:withdraw(300),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)
		three_hundred_button.place(x=990,y=25)
		# adding 400 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		four_hundred_button = tk.Button(middle_frame,
													text='400',
													command=lambda:withdraw(400),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)
		four_hundred_button.place(x=10,y=160)
		# adding 500 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		five_hundred_button = tk.Button(middle_frame,
													text='500',
													command=lambda:withdraw(500),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)				
		five_hundred_button.place(x=500,y=160)
		# adding 1000 hundred withdraw button (to middle frame) with specified text,command,releif,boarderwidth etc ...
		one_thousand_button = tk.Button(middle_frame,
													text='1000',
													command=lambda:withdraw(1000),
													relief='raised',
													borderwidth=3,
													width=50,
													height=5)		
		one_thousand_button.place(x=990,y=160)
		# defining cash variable to take the input from user
		cash = tk.StringVar()
		
		cash_label=tk.Label(self,text="Enter any another amount of money:",width=40,font=('orbitron',13),fg='Black',height=4)
		cash_label.place(x=10,y=494)
		# adding other amount label with a specified text, font, background color, foreground color, and packing 
		other_amount_entry = tk.Entry(middle_frame,
													textvariable=cash,
													borderwidth=3,
													width=59,
													justify='right')	
		other_amount_entry.place(x=500,y=300,height=80)
		# other amount function is used to define any other cash amount and increment balance with it
		def other_amount(_):
			# Using the current balance vriable as global to chanrge its value
			global current_balance
			if cash.get().isdigit():
			# checking if the balance is enough to make withdraw 
				if int(cash.get()) <= current_balance:
					current_balance -= int(cash.get())
					controller.shared_data['Balance'].set(current_balance)
					balance_label['text']='Withdraw is done successfully!'
					cash.set('')
				# in case if it wasn't enough dispaly that to user
				else:	
					balance_label['text']='Balance is not enough!'
					cash.set('')
			else:
				cash.set('')
				balance_label['text']='Invalid amount value!!'
		other_amount_entry.bind('<Return>',other_amount)
		# adding balance label to display messages to user with specified text,font,fg,bg,anchor and packing
		balance_label = tk.Label(self,
													text='',
													font=('orbitron',13),
													fg='#990000',
													bg='#666666',
													anchor='n')
		balance_label.place(x=580,y=600)
		# exit function is used to display MenuPage
		def exit():
			balance_label['text']=''
			controller.show_frame('MenuPage')
		# adding exit button with specific text,command,releif,boarderwidth,width etc ... 
		exit_button = tk.Button(middle_frame,
													text='Main Menu',
													command=exit,
													relief='raised',
													borderwidth=3,
													width=35,
													height=5)
		exit_button.place(x=1100,y=400)
		
		
		# adding a buttom frame with a background color and packing
		bottom_frame = tk.Frame(self,relief='raised',borderwidth=3,bg='black')
		bottom_frame.pack(fill='x',side='bottom')
		# adding visa photo to the bottom frame
		visa_photo = tk.PhotoImage(file='visa.png')
		visa_photo = visa_photo.subsample(15,15)
		visa_label = tk.Label(bottom_frame,image=visa_photo,bg='black')
		visa_label.pack(side='left')
		visa_label.image = visa_photo
		# adding mastercard photo to the bottom frame
		mastercard_photo = tk.PhotoImage(file='credit-card.png')
		mastercard_photo = mastercard_photo.subsample(15,15)
		mastercard_label = tk.Label(bottom_frame,image=mastercard_photo,bg='black')
		mastercard_label.pack(side='left')
		mastercard_label.image = mastercard_photo
		# adding american_express photo to the bottom frame
		american_express_photo = tk.PhotoImage(file='american-express.png')
		american_express_photo = american_express_photo.subsample(15,15)
		american_express_label = tk.Label(bottom_frame,image=american_express_photo,bg='black')
		american_express_label.pack(side='left')
		american_express_label.image = american_express_photo
		# adding paypal photo to the bottom frame
		paypal_photo = tk.PhotoImage(file='paypal.png')
		paypal_photo = paypal_photo.subsample(15,15)
		paypal_label = tk.Label(bottom_frame,image=paypal_photo,bg='black')
		paypal_label.pack(side='left')
		paypal_label.image = paypal_photo
		# tick function is used to display time
		def tick():
			current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
			time_label.config(text=current_time)
			time_label.after(200,tick)
        # adding a time label to show time inside the bottom frame
		time_label = tk.Label(bottom_frame,font=('orbitron',12),fg='white',bg='black')
		time_label.pack(side='right')
		# calling tick function to display time
		tick()
   

class DepositPage(tk.Frame):
    
	# Defining the init function for deposit page window
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='#f3f3f3')
		self.controller = controller
		# Adding heading label inside the frame which include text, font, foreground, background and packing 
		heading_label = tk.Label(self,
													text='  ATM Machine',
                                                    font=('orbitron',40,'bold'),
													foreground='#990000',
													background='#f3f3f3')
		heading_label.pack(pady=50)
		# adding a photo and sampling it 
		ITI_photo = tk.PhotoImage(file='ITI.png')
		ITI_photo=ITI_photo.subsample(5,5)
		# defining a label to the photo and placing it
		ITI_label = tk.Label(image=ITI_photo)
		ITI_label.place(x=420,y=5)
		# adding the photo to the label
		ITI_label.image = ITI_photo
		# adding enter amount label with a specified text, fonr, bg, fg and packing
		enter_amount_label = tk.Label(self,
													text='Enter the amount of money you want to deposit:',
													font=('orbitron',15),
													bg='#cccccc',
													fg='black')
		enter_amount_label.pack(fill= 'x')
		
		
		# adding a middle frame with a background color and packing 
		middle_frame = tk.Frame(self,bg='#666666')
		middle_frame.pack(fill='both',expand=True)
		# defining cash variable to take input from user
		cash = tk.StringVar()
		# adding deposit entry to the middle frame with specified font, width, and placing
		deposit_entry = tk.Entry(middle_frame,
													textvariable=cash,
													font=('orbitron',12),
													width=30)
		deposit_entry.place(x=540,y=20,height=40)
		# deposit cash function is used to increment the cash by the amount entered by the user
		def deposit_cash():
			global current_balance
			if cash.get().isdigit():
				current_balance += int(cash.get())
				controller.shared_data['Balance'].set(current_balance)
				cash.set('')
				deposit_label['text']='Deposit is done successfully !'
			# in case if cash was invalid
			else:
				deposit_label['text']='      This deposit is invalid!'
				cash.set('')
        # adding enter button to confirm deposit. The button has a sepcified text, command, releif, boardwith etc
		enter_button = tk.Button(middle_frame,
													text='Confirm',
													command=deposit_cash,
													relief='raised',
													borderwidth=3,
													width=30)
		enter_button.place(x=565,y=80,height=45)
		# adding deposit label to display messages to user with specified text,font,fg,bg,anchor and packing
		deposit_label = tk.Label(self,
													text='',
													font=('orbitron',13),
													fg='#990000',
													bg='#666666',
													anchor='n')
		deposit_label.place(x=580,y=600)
		# exit function is used to display MenuPage
		def exit():
			deposit_label['text']=''
			controller.show_frame('MenuPage')
		# adding exit button with specific text,command,releif,boarderwidth,width etc ... 
		exit_button = tk.Button(self,
													text='Main Menu',
													command=exit,
													relief='raised',
													borderwidth=3,
													width=35,
													height=5)
		exit_button.place(x=1100,y=600)
		
		
		# adding a buttom frame with a background color and packing
		bottom_frame = tk.Frame(self,relief='raised',borderwidth=3,bg='black')
		bottom_frame.pack(fill='x',side='bottom')
		# adding visa photo to the bottom frame
		visa_photo = tk.PhotoImage(file='visa.png')
		visa_photo = visa_photo.subsample(15,15)
		visa_label = tk.Label(bottom_frame,image=visa_photo,bg='black')
		visa_label.pack(side='left')
		visa_label.image = visa_photo
		# adding mastercard photo to the bottom frame
		mastercard_photo = tk.PhotoImage(file='credit-card.png')
		mastercard_photo = mastercard_photo.subsample(15,15)
		mastercard_label = tk.Label(bottom_frame,image=mastercard_photo , bg='black')
		mastercard_label.pack(side='left')
		mastercard_label.image = mastercard_photo
		# adding american_express photo to the bottom frame
		american_express_photo = tk.PhotoImage(file='american-express.png')
		american_express_photo = american_express_photo.subsample(15,15)
		american_express_label = tk.Label(bottom_frame,image=american_express_photo,bg='black')
		american_express_label.pack(side='left')
		american_express_label.image = american_express_photo
		# adding paypal photo to the bottom frame
		paypal_photo = tk.PhotoImage(file='paypal.png')
		paypal_photo = paypal_photo.subsample(15,15)
		paypal_label = tk.Label(bottom_frame,image=paypal_photo,bg='black')
		paypal_label.pack(side='left')
		paypal_label.image = paypal_photo
		# tick function is used to display time
		def tick():
			current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
			time_label.config(text=current_time)
			time_label.after(200,tick)
        # adding a time label to show time inside the bottom frame  
		time_label = tk.Label(bottom_frame,font=('orbitron',12),fg = 'white' , bg='black')
		time_label.pack(side='right')
		# calling tick function to display time
		tick()


class BalancePage(tk.Frame):
    
	# Defining the init function for balance page window
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent,bg='#f3f3f3')
		self.controller = controller
        # Adding heading label inside the frame which include text, font, foreground, background and packing 
		heading_label = tk.Label(self,
												text='  ATM Machine',
												font=('orbitron',40,'bold'),
												foreground='#990000',
												background='#f3f3f3')
		heading_label.pack(pady=50)
		# adding a photo and sampling it 
		ITI_photo = tk.PhotoImage(file='ITI.png')
		ITI_photo=ITI_photo.subsample(5,5)
		# adding the photo to the label
		ITI_label = tk.Label(image=ITI_photo)
		ITI_label.place(x=420,y=5)
		# adding the photo to the label
		ITI_label.image = ITI_photo
		# adding balance label disp with a specified text, fonr, bg, fg and packing
		balance_label_disp = tk.Label(self,
												text='Current Balance: ',
												font=('orbitron',15),
												bg='#cccccc',
												fg='black')
													
		
		balance_label_disp.pack(fill= 'x')
		
		
		# adding a middle frame with a background color and packing
		middle_frame= tk.Frame(self,bg='#666666')
		middle_frame.pack(fill='both',expand=True)
		# taking the vaule of balance 
		global current_balance
		controller.shared_data['Balance'].set(current_balance)
		# adding balance label to display the value of balance
		balance_label = tk.Label(self,			
												textvariable=controller.shared_data['Balance'],
												font=('orbitron',15),
												fg='#990000',
												bg='#666666')
		balance_label.place(x=650,y=230)
		# menu function is used to display MenuPage 
		def menu():
			controller.show_frame('MenuPage')
        # adding menu button with specific text,command,releif,boarderwidth,width etc ... 
		menu_button = tk.Button(middle_frame,
												command=menu,
												text='Main Menu',
												relief='raised',
												borderwidth=3,
												width=35,
												height=5)
		menu_button.place(x=1100,y=400)

		# adding a buttom frame with a background color and packing
		bottom_frame = tk.Frame(self,relief='raised',borderwidth=3,bg='black')
		bottom_frame.pack(fill='x',side='bottom')
		# adding visa photo to the bottom frame
		visa_photo = tk.PhotoImage(file='visa.png')
		visa_photo = visa_photo.subsample(15,15)
		visa_label = tk.Label(bottom_frame,image=visa_photo,bg='black')
		visa_label.pack(side='left')
		visa_label.image = visa_photo
		# adding mastercard photo to the bottom frame
		mastercard_photo = tk.PhotoImage(file='credit-card.png')
		mastercard_photo = mastercard_photo.subsample(15,15)
		mastercard_label = tk.Label(bottom_frame,image=mastercard_photo,bg='black')
		mastercard_label.pack(side='left')
		mastercard_label.image = mastercard_photo
		# adding american_express photo to the bottom frame
		american_express_photo = tk.PhotoImage(file='american-express.png')
		american_express_photo = american_express_photo.subsample(15,15)
		american_express_label = tk.Label(bottom_frame,image=american_express_photo,bg='black')
		american_express_label.pack(side='left')
		american_express_label.image = american_express_photo
		# adding paypal photo to the bottom frame
		paypal_photo = tk.PhotoImage(file='paypal.png')
		paypal_photo = paypal_photo.subsample(15,15)
		paypal_label = tk.Label(bottom_frame,image=paypal_photo,bg='black')
		paypal_label.pack(side='left')
		paypal_label.image = paypal_photo
		# tick function is used to display time
		def tick():
			current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
			time_label.config(text=current_time)
			time_label.after(200,tick)
        # adding a time label to show time inside the bottom frame    
		time_label = tk.Label(bottom_frame,font=('orbitron',12),fg = 'white',bg='black')
		time_label.pack(side='right')
		# calling tick function to display time
		tick()


# Calling the sample app function with app main loop to run tkinter
if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()