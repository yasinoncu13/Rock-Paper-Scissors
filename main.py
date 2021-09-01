import tkinter
from random import randint
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Taş,Kağıt,Makas')
root.iconbitmap('icon.jpg')
root.geometry('500x600')

root.config(bg="white")

tas = PhotoImage(file='')
kagit = PhotoImage(file='')
makas = PhotoImage(file='')

image_list = [tas, kagit, makas]

pick_number = randint(0, 2)

image_label = tkinter.Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=10)


def spin():
    pick_number = randint(0, 2)
    image_label.config(image=image_list[pick_number])


    if user_choice.get()=="Taş":
        user_choice_value=0
    elif user_choice.get()=="Kağıt":
        user_choice_value = 1
    elif user_choice.get()=="Makas":
        user_choice_value = 2

    if user_choice_value==0:
        if pick_number==0:
            win_lose_label.config(text="Taş geldi,Berabere !")
        elif pick_number==1:
            win_lose_label.config(text="Kağıt geldi,yenildiniz ! Bir daha deneyin.")
        elif pick_number==2:
            win_lose_label.config(text="Makas geldi tebrikler kazandınız.Bir daha oynayın lütfen.")
    elif user_choice_value==1:
        if pick_number==0:
            win_lose_label.config(text="Taş geldi.Tebrikler Kazandınız.Bir daha oynayın lütfen.")
        elif pick_number==1:
            win_lose_label.config(text="Kağıt geldi,Berabere,bir daha oynayın.")
        elif pick_number==2:
            win_lose_label.config(text="Makas geldi,Yenildiniz ! Bir daha deneyin.")
    elif user_choice_value==2:
        if pick_number==0:
            win_lose_label.config(text="Taş geldi Yenildiniz ! Bir daha deneyin.")
        elif pick_number==1:
            win_lose_label.config(text="Kağıt geldi,Kazandınız.Bir daha oynayın lütfen.")
        elif pick_number==2:
            win_lose_label.config(text="Makas geldi,Berabere,bir daha oynayın.")

user_choice = ttk.Combobox(root, value=("Taş", "Kağıt", "Makas"))
user_choice.current(0)
user_choice.pack(pady=20)

spin_button = tkinter.Button(root, text="spin!", command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(root,text="",font=("Helvetica",18),bg="white")
win_lose_label.pack(pady=50)

root.mainloop()
