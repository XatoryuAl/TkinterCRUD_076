import tkinter as kint
from tkinter import messagebox


main = kint.Tk()
var = kint.StringVar()
label = kint.Message(main, textvariable=var, relief=kint.RIDGE, width=300, font=(30))
var.set("Aplikasi Prediksi")
label.pack()

for i in range(10):
   E = kint.Label(main, text=(f"Nilai {i+1}: "))
   E.pack()
   
   Marks = kint.Entry(main, bd=10, width=30)
   Marks.pack()

def HasilPrek():
    kint.messagebox.showinfo("Hasil Prediksi","Prodi Teknologi Informasi")

press = kint.Button(font=(20),bg="#52bf90",fg="#000000",text="Hasil",command=HasilPrek)
press.pack()
   

main.mainloop()

