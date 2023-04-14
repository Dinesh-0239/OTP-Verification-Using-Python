"""
OTP Verification Using Python
Created by Dinesh Singh BCA Sem-6

"""
from tkinter import *
from tkinter import messagebox
import random
import smtplib

#Method to push time limit
def timer():
    """This method push the time limit to the otp verification"""
    global temp_otp,email_var,otp,response
    if temp_otp != otp or response != "ok":
        window.title("OTP Verification------Verification Failed")
        messagebox.showerror("Verification Failed","Time Out----You need to Resend OTP")
        window.title("OTP Verification")
        otp_var.set("")
        otp = None

#Method to send the email via gmail
def send_otp():
    """Method to send email via gmail"""
    global email_var,otp,timer_id
    #generating 6-digit otp
    otp = str(random.randint(100000,1000000))
    send_otp_btn.config(text="Resend OTP")

    #Kindly provide a valid emailid and its password for send email for verification
    sender_email_address = "example@gmail.com"
    sender_email_password = "your password"
    
    try:
        message = f"Your OTP for verification is {otp}"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email_address,sender_email_password)
        server.sendmail(sender_email_address,email_var.get(),message)
        server.quit()
        window.title("OTP Verification------OTP Sent")
        window.after_cancel(timer_id)
        timer_id = window.after(60000,timer)
    except:
        messagebox.showerror("Sent Failed","Message can't be sent")
        email_var.set("")

#Method to verify through otp
def verify_otp():
    """Method to verify through otp"""
    global email_var,otp_var,otp,response,temp_otp
    temp_otp = otp_var.get()
    if otp_var.get()==otp:
        response = messagebox.showinfo("OTP Verification","OTP VERIFIED : Click on 'OK' for Confirmation") 
        window.title("OTP Verification------OTP Verified")
        if response == "ok":
            email_var.set("")
            otp_var.set("")
    else:
        window.title("OTP Verification------OTP Verification")
        messagebox.showerror("OTP Verification","OTP NOT VERIFIED: Resend the otp for verification")
        otp_var.set("")
        otp = None

#Initializing window
window = Tk()
window.title("OTP Verification")
window.geometry("400x300")
window.resizable(False,False)
window.iconbitmap("appicon.ico")
window.config(bg="light green")

#Label for GUI title
Label(window,text="VERIFY FROM OTP",font=("timesnewroman",18,"bold","underline"),bg="Crimson",fg="white",relief=RAISED).place(x=90,y=20)

#frame for all widgets
frame = Frame(window,bg="linen",height=200,width=300,relief=RAISED,highlightbackground="silver",highlightthickness=5)
frame.place(x=50,y=70)

#Label for email 
Label(frame,text="Email :-",bg="snow",fg="black",font=("timesnewroman",12,"bold"),relief=FLAT).place(x=10,y=20)

#Variable for accepting email address of the user
email_var = StringVar()

#Entry for email
Entry(frame,textvariable=email_var,font=("timesnewroman",12),bg="snow",fg="black",relief=RAISED).place(x=100,y=20)

#timer_id
timer_id  = window.after(60000,quit)
#Button to send OTP
send_otp_btn = Button(frame,text="Send OTP",fg="white",bg="grey",font=("timesnewroman",12,"bold"),relief=RAISED,command=send_otp)
send_otp_btn.place(x=100,y=60)

#Label for OTP
Label(frame,text="Enter OTP:-",bg="snow",fg="black",font=("timesnewroman",12,"bold"),relief=FLAT).place(x=10,y=100)

#variable for accepting 6-digit otp number from the user
otp_var = StringVar()

#Entry for email
Entry(frame,textvariable=otp_var,font=("timesnewroman",12),bg="snow",fg="black",relief=RAISED,width=18).place(x=120,y=100)

#Variable for storing 6-digit otp
otp = None
#Variable to store the response after verification
response = None
temp_otp = None

#Button for verify OTP
Button(frame,text="Verify OTP",fg="white",bg="grey",font=("timesnewroman",12,"bold"),relief=RAISED,command=verify_otp).place(x=100,y=140)

window.mainloop()
