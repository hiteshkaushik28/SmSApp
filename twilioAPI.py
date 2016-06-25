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
    accSid = 'ACbcd368b4d27719178249339671a5e967'
    authToken = '467640f44532fb348c3efa5f8fe03c70'
    twilioClient = TwilioRestClient(accSid, authToken)
    twilioClient.messages.create(body="Hi this message was delivered to you using TWILIO-API as a part of python project",
                                 to="+917508337709", from_="+12404363599")
    print("message sent")


def call():
    from twilio.rest import TwilioRestClient
    account_sid = 'AC303a272ce3a1ce130c85f39f30a13484'
    auth_token  = 'febe70dfe0c603fa840b788dfbbf3b3c'
    client = TwilioRestClient(account_sid, auth_token)

    calls = client.calls.create(to="+918699006213",from_="+18572541981",
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
