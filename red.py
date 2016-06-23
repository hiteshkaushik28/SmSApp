# IMPORTING TKINTER PACKAGE


from tkinter import *

from twilio.rest import TwilioRestClient



root = Tk()
root.geometry("400x200")
root.title("SmSApp")
frame = Frame(width=800,height=500)
frame.pack()



def register():

    accSid = 'AC303a272ce3a1ce130c85f39f30a13484'
    authToken = 'febe70dfe0c603fa840b788dfbbf3b3c'
    twilioClient = TwilioRestClient(accSid, authToken)
    twilioClient.messages.create(body="Hi this message was delivered to you using TWILIO-API configured by HITESH",
                                 to="+918699006213", from_="18572541981")
    print("message sent")






#  CREATING THE REGISTRATION FORM


L1 = Label(frame,text=" YOUR MOBILE:",fg="blue",pady=2)
L2 = Label(frame,text="TWILIO NUMBER:",fg="blue",pady=6)





E1 = Entry(frame)
E2 = Entry(frame)




c = Checkbutton(frame,text="Keep me Logged in")





b = Button(frame, text="SAVE", bg="grey", fg="black", command=register)

L1.grid(row = 0,column = 0,sticky=S)
L2.grid(row = 1,column = 0,sticky=S)

E1.grid(row = 0,column = 1,sticky=S)
E2.grid(row = 1,column = 1,sticky=S)


c.grid(row = 2,column = 1,columnspan = 2)
b.grid(columnspan = 5,column=0)

L5 = Label(frame,text="FILL THE DETAILS TO RECIEVE A CONFIRMATION MESSAGE",fg="red")
L5.grid(row = 7,columnspan = 5,ipady = "40")




root.mainloop()
