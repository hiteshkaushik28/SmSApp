# IMPORTING TKINTER PACKAGE AND TWILIO API


from tkinter import *




root = Tk()

root.geometry("400x300")
root.title("SmSApp")
root.config()
v1=IntVar()
v2=IntVar()




def register():
    from twilio.rest import TwilioRestClient
    accSid = 'your id'
    authToken = 'your token'
    twilioClient = TwilioRestClient(accSid, authToken)
    twilioClient.messages.create(body="Hi this message was delivered to you using TWILIO-API as a part of python project",
                                 to="recipient number", from_="twilio number")
    print("message sent")


def call():
    from twilio.rest import TwilioRestClient
    account_sid = 'your id'
    auth_token  = 'your token'
    client = TwilioRestClient(account_sid, auth_token)

    calls = client.calls.create(to="recipient number",from_="sender number",
                                url="http://foo.com/call.xml")
    print(calls.to)
    print("CALL CONNECTED")
#  CREATING THE REGISTRATION FORM


L1 = Label(root,text=" YOUR MOBILE:",fg="blue",pady=2)
L2 = Label(root,text="TWILIO NUMBER:",fg="blue",pady=6)





E1 = Entry(root)
E2 = Entry(root)








b = Button(root, text="SEND MESSAGE", bg="white", fg="black", command=register,width=15)
b1 = Button(root,text="CALL", bg="white", fg="black",command=call,width=15)
L1.grid(row = 0,column = 0,sticky=S)
L2.grid(row = 1,column = 0,sticky=S)

E1.grid(row = 0,column = 1,sticky=S)
E2.grid(row = 1,column = 1,sticky=S)



b.grid(columnspan = 6,column=0,pady=5)
b1.grid(columnspan=6)
L5 = Label(root,text="FILL THE DETAILS TO RECEIVE A CONFIRMATION MESSAGE",fg="red")
L5.grid(row = 7,column=0,columnspan = 7,ipady = "40",sticky=E)




root.mainloop()
