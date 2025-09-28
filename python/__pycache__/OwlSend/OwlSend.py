import json
from datetime import datetime
import os
import tkinter as tk
from OwlSend.leet import leet_translate, string_translate
from OwlSend.simple_encrypt import encrypt, decrypt


# window = tk.Tk()Committing to GitHub Using Python
# bckg = tk.Label(text="Download will begin shortly", bg='orange', fg='blue', width=211, height=59, font='TimesNewRoman')
# button = tk.Button(text="Click if it didn't...", bg='blue', fg='white')
# bckg.pack()
# #button.pack()
# window.mainloop()
def message():
    with open('Owlsend/user.txt', 'w') as login:
        login.seek(0) 
        if not login.read(1):
            new = True
        else:
            new = False
        
        user = input("Username: ")
        password = encrypt(input("Password: "))
        login_split = login.read().split()
        if new == True:
            login.write(f'{user, password} SUCCESS')
        else:
            if login_split[0] == user and login_split[1] == password:
                login.write(f'{user, password} SUCCESS')
            else:
                login.write(f'{user} FAIL')

    action = input("Send, view, or add contacts: ").lower()
    if action in ['send', 'deliver']:
        recepient = input("Recepient: ")
        data = {input("Message: "), str(datetime.now()), recepient, login}
        with open('Owlsend/messages.json', 'r+') as msg:
            messages = json.loads(msg)
            messages = dict(messages["sent"], sent=data)
            json.dumps(messages, msg, indent=4)
response = requests.get(f"https://{domain}/{path}")
data = response.json()