#CAPTCHA CREATOR
import random
from tkinter import messagebox
from tkinter import *
#Captcha Creator function	
def create_captcha():
  try:
    repeat = int(repeat_entry.get())
    length = int(length_entry.get())
  except:
    messagebox.showerror(message="Please key in the required inputs")
    return
  #Check if user allows repeation of characters
  if repeat == 1:
    captcha = random.sample(character_string,length)
  elif repeat ==2:
    captcha = random.choices(character_string,k=length)

  #Since the returned value is a list, we convert to a sting using join
  captcha=''.join(captcha)
  #Declare a string variable
  captcha_v = StringVar()
  captcha="Created captcha: "+str(captcha)
  #Assign the captcha to the declared string variables
  captcha_v.set(captcha)
  #Create a read only entry box to view the output, position using place
  captcha_label = Entry(captcha_gen, bd=0, bg="gray85", textvariable=captcha_v, state="readonly")
  captcha_label.place(x=10, y=140, height=50, width=320)

#Define a string containing letters, symbols and numbers
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#Define the user interface
captcha_gen  = Tk()
captcha_gen.geometry("350x200")
captcha_gen.title(" Hemanth's Captcha Generator")
captcha_gen.configure(bg="#3D3C3A")

#Mention the title of the app
title_label = Label(captcha_gen, text="Captcha Generator", font=('Timesnewroman',12))
title_label.pack()

#Read length 
length_label = Label(captcha_gen, text="Enter length of captcha: ")
length_label.place(x=20,y=30)
length_entry = Entry(captcha_gen, width=5)
length_entry.place(x=190,y=30)
#Read repetition
repeat_label = Label(captcha_gen, text="Repatition? 1: YES 2: NO: ")
repeat_label.place(x=20,y=60)
repeat_entry = Entry(captcha_gen, width=5)
repeat_entry.place(x=190,y=60)
#Generate captcha
captcha_button = Button(captcha_gen, text="Generate Captcha", command=create_captcha)
captcha_button.place(x=100,y=100)
#Exit and close the app
captcha_gen.mainloop()
