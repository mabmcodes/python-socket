
import socket
import threading
from tkinter import *
from tkinter.filedialog import askopenfilename





nickName = input('choose nickname !')
HOST = '127.0.0.1'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

window = Tk()
window.title(nickName)
window.geometry('1080x720')
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41B77f')



def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'nick':
                client.send(nickName.encode('utf-8'))
            else:
                print(message)
                txtMessages.insert(END,"\n" + message)
        except:
            print("an error occured !")
            txtMessages.insert(END, "an error occured !")
            client.close()
            break

txtMessages = Text(window, width=100)
txtMessages.grid(row=0, column=3, padx=150, pady=10 )

txtYourMessage = Entry(window, width=75)
txtYourMessage.grid(row=1, column=3, padx=175, pady=10)

def write():
    
    msg = txtYourMessage.get()
    message = f'{nickName}: {msg}'
    client.send(message.encode('utf-8'))


    



btnsend = Button(window, text='send', width=20, command=write)
btnsend.grid(row=2, column=3, padx=10, pady=10)

quit = Button(window, text='Quit', width=20 ,command=window.quit)
quit.grid(row=5, column=3, padx=10, pady=10)


rec_thread = threading.Thread(target=receive)
rec_thread.daemon = True
rec_thread.start()
# wri_thread = threading.Thread(target=write)
# wri_thread.start()


window.mainloop()
