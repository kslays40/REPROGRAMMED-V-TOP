from doctest import master
import tkinter
import customtkinter
import webbrowser


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Student Login")

#Main Login page
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

#Username label
userlabel = customtkinter.CTkLabel(master=frame_1, text="Username: ",text_font=("Roboto Medium", -16))
userlabel.grid(row=2,column=2,pady=12,padx=10)
#Password label
passlabel = customtkinter.CTkLabel(master=frame_1, text="Password: ",text_font=("Roboto Medium", -16))
passlabel.grid(row=4,column=2,pady=12,padx=10)




#Submit button
# StringVars
# Possible Login
possible_users = {'q': 'q', '21BHI10047': '21BHI10047'}  # dictionary of corresponding user name and passwords
the_user = tkinter.StringVar()  # used to retrieve input from entry
the_pass = tkinter.StringVar()
bad_pass = customtkinter.CTkLabel(master=frame_1, text="Incorrect Username or Password")
def login(user):
    forget_login_window()
    next_window(user)
def check_login():
    requested_user = the_user.get()
    try:
        if possible_users[requested_user] == the_pass.get():
            login(requested_user)
        else:
            bad_pass.grid(row=2, column=1)
    except KeyError:
        bad_pass.grid(row=2, column=1)

#entry username
usernameentry = customtkinter.CTkEntry(master=frame_1,width=120,textvariable=the_user)
usernameentry.grid(row=2,column=4,pady=12, padx=10)
#entry password
passwordentry = customtkinter.CTkEntry(master=frame_1,width=120,textvariable=the_pass)
passwordentry.grid(row=4,column=4,pady=12, padx=10)

#submit button
button_1 = customtkinter.CTkButton(master=frame_1,text="Submit/Login",command=check_login)
button_1.grid(row=6,column=3,pady=12, padx=10)

def forget_login_window():  # forget all the grid items.
    usernameentry.grid_forget()
    passwordentry.grid_forget()
    userlabel.grid_forget()
    passlabel.grid_forget()
    button_1.grid_forget()
    bad_pass.grid_forget()

def next_window(my_user):
    app.title(my_user)
    frame_right = customtkinter.CTkFrame(master=frame_1)
    frame_right.grid(row=0, column=2, sticky="nswe", padx=20, pady=20)
    leftframe = customtkinter.CTkFrame(master=frame_1)
    leftframe.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)
    cupframe= customtkinter.CTkFrame(master=frame_1)
    cupframe.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    #VIT label
    vitlabel = customtkinter.CTkLabel(master=leftframe, text="VIT",text_font=("Roboto Medium", 54))
    vitlabel.grid(row=2,column=2,pady=12,padx=10)
    #student info
    namelabel = customtkinter.CTkLabel(master=cupframe, text="Name of Student: Kumar Kaustubh",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
    namelabel.grid(row=3,column=4)
    regnolabel = customtkinter.CTkLabel(master=cupframe, text="Registration Number of student: 21BHI10047",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
    regnolabel.grid(row=4,column=4)
    bloodgrouplabel = customtkinter.CTkLabel(master=cupframe, text="Blood Group: A+",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
    bloodgrouplabel.grid(row=5,column=4)
    proglabel = customtkinter.CTkLabel(master=cupframe,text="Course: CSE Specialization in Cloud Computing",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
    proglabel.grid(row=6,column=4)


    #buttons
    def ttcall():
        webbrowser.open_new(r"https://app.powerbi.com/links/bBmgcM23W8?ctid=09bd1956-edda-4e9a-9543-7c7aa2cf4e81&pbi_source=linkShare")
    ttbutton = customtkinter.CTkButton(master=leftframe,text="Time Table",command=ttcall)
    ttbutton.grid(row=10,column=2,pady=12, padx=10)
    def markscall():
        webbrowser.open_new(r"https://app.powerbi.com/groups/me/reports/108bcc12-57e7-46ca-91b9-2e154ab19b8b/ReportSection?bookmarkGuid=Bookmark52b98f730b0e7d70cffe")
    marksbutton = customtkinter.CTkButton(master=leftframe,text="Marks History",command=markscall)
    marksbutton.grid(row=12,column=2,pady=12, padx=10)
    def attcall():
        webbrowser.open_new(r"https://app.powerbi.com/groups/me/reports/85d3eec9-ad74-4d11-a952-2377d361b230/ReportSection")
    attbutton= customtkinter.CTkButton(master=leftframe,text="Attendance",command=attcall)
    attbutton.grid(row=14,column=2,pady=12, padx=10)
    def infocall():
        webbrowser.open_new(r"https://app.powerbi.com/groups/me/reports/e978faa4-5d28-4331-8f14-ac66812e6ced/ReportSection")
    finfobutton= customtkinter.CTkButton(master=leftframe,text="Faculty Information",command=infocall)
    finfobutton.grid(row=16,column=2,pady=12, padx=10)
    def hostelcall():
        hostel = customtkinter.CTkLabel(master=frame_right,text="Block: 1",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        hostelroom = customtkinter.CTkLabel(master=frame_right,text="Room Number: 222",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        hostel.grid(row=40,column=5)
        hostelroom.grid(row=45,column=5)
    hostelbutton= customtkinter.CTkButton(master=leftframe,text="Hostel Information",command=hostelcall)
    hostelbutton.grid(row=20,column=2,pady=12,padx=10)
    def paycall():
        webbrowser.open_new(r"https://www.onlinesbi.sbi/")
    paybutton= customtkinter.CTkButton(master=leftframe,text="Payment",command=paycall)
    paybutton.grid(row=22,column=2,pady=12,padx=10)
    def leavecall():
        leave = customtkinter.CTkLabel(master=frame_right,text="Kindly fill out form",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        leave.grid(row=35,column=5)
        webbrowser.open_new(r"https://docs.google.com/forms/d/e/1FAIpQLSfCQbGVdYU55gkfRNDGdTO1oeKvVHJpuvjfyM7YRFKojo0pAQ/viewform?usp=sf_link")
    leavebutton= customtkinter.CTkButton(master=leftframe,text="Leave Request",command=leavecall)
    leavebutton.grid(row=24,column=2,pady=12,padx=10)
    
    def pinfo():
        named=customtkinter.CTkLabel(master=frame_right,text="Name of proctor: Dr. Pranav Pratyush",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        named.grid(row=30,column=5)
        contact=customtkinter.CTkLabel(master=frame_right,text="Contact Number: +919430370602",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        contact.grid(row=31,column=5)
        email=customtkinter.CTkLabel(master=frame_right,text="Email: abc@gmail.com",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        email.grid(row=32,column=5)
    procbutton= customtkinter.CTkButton(master=leftframe,text="Proctor Information",command=pinfo)
    procbutton.grid(row=18,column=2,pady=12,padx=10)


    def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    optionmenu_1 = customtkinter.CTkOptionMenu(master=leftframe,values=["Light", "Dark", "System"],command=change_appearance_mode)
    optionmenu_1.grid(row=28, column=2, pady=12, padx=10, sticky="w")

    def facultycall():
        faclabel=customtkinter.CTkLabel(master=cupframe,text="Welcome Admin Kindly select an action",text_font=("Roboto Medium", -16),justify=tkinter.LEFT)
        faclabel.grid(row=11,column=4)
        def markscall():
            webbrowser.open_new(r"https://1drv.ms/x/s!Aq0WYWHZH9B9drdpCMvS9FxpdNI?e=wiNCTQ")
        facultyoptions= customtkinter.CTkButton(master=cupframe,text="Marks Updation",command=markscall)
        facultyoptions.grid(row=14, column=4, pady=12, padx=10)
        def attendancecall():
            webbrowser.open_new(r"https://1drv.ms/x/s!Aq0WYWHZH9B9cjDrlXtrcmAbLlc?e=lBrOXu")
        attendancemark= customtkinter.CTkButton(master=cupframe,text="Attendance Updation",command=attendancecall)
        attendancemark.grid(row=18, column=4, pady=12, padx=10)
        
    teacher=customtkinter.CTkButton(master=cupframe,text="Faculty Access",command=facultycall)
    teacher.grid(row=10,column=4, pady=12, padx=10)


    quitbutton = customtkinter.CTkButton(master=leftframe,text="Signout",command=quit)
    quitbutton.grid(row=30,column=2,pady=12,padx=10)


app.mainloop()