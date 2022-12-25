from tkinter import *

# defining 2 variables to be used as counters
S_Button =0
F_Button =0

# Defining function for Senegal Goals
def Senegal_goals():
# setting the Senegal counter to global in order to change its value
	global S_Button 
	S_Button=S_Button+1
# Dispalying the golas after incrementing in a label
	label_3.config(text = S_Button)


# Defining function for France Goals
def France_goals():
# setting the France counter to global in order to change its value
	global F_Button
	F_Button =F_Button+1 
# Dispalying the goals after incrementing in a label
	label_4.config(text = F_Button)
	
# ---------------------------------------------------------------------------------------------------
# construct main window through calling TK()
window_1 = Tk() 
# adding title and size to the window 
window_1.title("Match Results")
window_1.geometry('500x300')
# this is to prevent from resizing the window 
window_1.resizable(0, 0)  

# Adding flag pictures to Senegal and France and choosing a suitable sampling for each
photo_1 = PhotoImage(file='sen.png')
photo_2 = PhotoImage(file='fra.png')
photo_1 = photo_1.subsample(18,18)
photo_2 = photo_2.subsample(2,2)

# ---------------------------------------------------------------------------------------------------

# Adding Senegal flag picture to lable_1 and adding a name "Senegal" in label_1_2 
label_1  =Label(window_1 , image=photo_1,highlightbackground="black", highlightthickness=1)
label_1_2  =Label(window_1 , text=("Senegal") , font= ('Verdana', 12))

# using geomertry function to set the lable in a specific place [BOTTOM , LEFT , RIGHT] 
label_1.place(x = 50,y = 50)
label_1_2.place(x = 90,y = 20)


# Adding a button to increment Senegal goals
S_goal  =Button(window_1 , text = "Goal" , bd = '5' , font= ('Verdana', 10) , command = Senegal_goals)
S_goal.place(x = 105,y = 170 )

# ---------------------------------------------------------------------------------------------------

# Adding France flag picture to lable_2 and adding a name "France" in label_2_2
label_2  =Label(window_1 , image=photo_2 , highlightbackground="black", highlightthickness=1)
label_2_2  =Label(window_1 , text=("France"), font= ('Verdana', 12))

# using geomertry function to set the lable in a specific place [BOTTOM , LEFT , RIGHT] 
label_2.place(x = 300,y = 50)
label_2_2.place(x = 340,y = 20)

# Adding a button to increment France goals
F_goal  =Button(window_1 , text = "Goal" , bd = '5' , font= ('Verdana', 10), command = France_goals)
F_goal.place(x=350 , y=170)

# ---------------------------------------------------------------------------------------------------

# Adding a result frame to display the match result 
result_frame = Frame(window_1, width=250,height=50, bd=0, background="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
result_frame.place(x=120,y=220)

# Adding a label_3 to display Senegl goals
label_3  =Label(window_1 , width=5,height=2, bd=0, fg="yellow" , background="grey",  highlightbackground="green", highlightcolor="green", highlightthickness=1)
label_3.place(x= 180 , y= 227)

# Adding a label_4 to display France goals
label_4  =Label(window_1 , width=5,height=2, bd=0, fg="white",background="grey", highlightbackground="blue", highlightcolor="blue", highlightthickness=1)
label_4.place(x= 270 , y= 227)

# Adding a label_5 to display ':' between the goals
label_5  =Label(window_1 , text=(":") ,  background="white", font= ('Verdana', 15))
label_5.place(x=237,y=230)

# ---------------------------------------------------------------------------------------------------

# Adding exit button to close the window
B_1  =Button(window_1 , text = "Exit", font= ('Verdana', 10), fg="red", bd = '5', width=8,height=2,command = window_1.destroy)
B_1.place(x=410 , y=240)

# ---------------------------------------------------------------------------------------------------

# Call the main loop which is used when the application is ready to run to keep the code displaying 
window_1.mainloop()

