from tkinter import *
import string

alphalist = string.ascii_lowercase 
Alphalist = string.ascii_uppercase

def encoded(originalmsg,key):
    msg_words = originalmsg.split(" ")
    enc_words = []
    for i in msg_words:
        encw = ""
        for j in i:
            #print(alphalist.find(j)+3,end = " ")
            if j in alphalist:
                enc = alphalist.find(j) + key
            if j in Alphalist:
                enc = Alphalist.find(j) + key
            if enc >= 26:
                enc = enc-26
            #print(alphalist[enc],end="")
            encw = encw + alphalist[enc]
        #print(" ",end="")
        enc_words.append(encw)
    enc_msg = " ".join(enc_words)
    return enc_msg

def decoded(encodedmsg,key):
    enc_msg_list = encodedmsg.split(" ")
    dec_words = []
    for i in enc_msg_list:
        decw = ""
        for j in i:
            #print(alphalist.find(j)+3,end = " ")
            if j in alphalist:
                dec = alphalist.find(j) - key
            if j in Alphalist:
                dec = Alphalist.find(j) - key
            #print(alphalist[dec],end="")
            decw = decw + alphalist[dec]
        #print(" ",end="")
        dec_words.append(decw)
    dec_msg = " ".join(dec_words)
    return dec_msg


def save_info_encode():
    message_info = message.get()
    password_info = int(password.get())
    secret = encoded(message_info,password_info)

    file = open("secret.txt",'w')
    file.write(secret)
    file.close
    print("Secret file successfully generated")

    message_entry.delete(0, END)
    password_entry.delete(0, END)

def save_info_decode():
    message_info = message.get()
    password_info = int(password.get())
    original = decoded(message_info,password_info)

    file = open("original.txt",'w')
    file.write(original)
    file.close
    print("Secret file successfully decrypted")

    message_entry.delete(0, END)
    password_entry.delete(0, END)


screen = Tk()
screen.geometry("500x500")
screen.title("secret messaging")

heading = Label(text = "secret messaging", bg="grey", fg="black", width="500", height="3")
heading.pack()

message_text = Label(text="Message : ",)
password_text = Label(text="Password : ",)

message_text.place(x=15,y=70)
password_text.place(x=15,y=140)

message = StringVar()
password = IntVar()

message_entry = Entry(textvariable=message, width="30")
password_entry = Entry(textvariable=password, show="*", width="30")

message_entry.place(x=15, y=100)
password_entry.place(x=15, y=180)

Encode = Button(screen,text="Encode", width="30", height="3", command=save_info_encode, bg="grey")
Encode.place(x=15, y=240)

Decode = Button(screen,text="Decode", width="30", height="3", command=save_info_decode, bg="grey")
Decode.place(x=200, y=240)

screen.mainloop()
