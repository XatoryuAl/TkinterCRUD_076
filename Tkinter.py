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

import tkinter as kint
from tkinter import messagebox
import sqlite3

# ==============================
#  Database Setup (SQLite)
# ==============================
conn = sqlite3.connect("nilai_siswa.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS nilai_siswa(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT,
        biologi INTEGER,
        fisika INTEGER,
        inggris INTEGER,
        prediksi_fakultas TEXT
    )
""")
conn.commit()

# ==============================
#  GUI TKINTER
# ==============================
main = kint.Tk()
main.title("Aplikasi Prediksi Fakultas")

var = kint.StringVar()
label = kint.Message(main, textvariable=var, relief=kint.RIDGE, width=300, font=(30))
var.set("Aplikasi Prediksi")
label.pack()

# ==============================
#  ENTRY NAMA + NILAI
# ==============================
#  Nama siswa
kint.Label(main, text="Nama Siswa:").pack()
entry_nama = kint.Entry(main, bd=10, width=30)
entry_nama.pack()

# Entry Biologi
kint.Label(main, text="Nilai Biologi:").pack()
entry_bio = kint.Entry(main, bd=10, width=30)
entry_bio.pack()

# Entry Fisika
kint.Label(main, text="Nilai Fisika:").pack()
entry_fis = kint.Entry(main, bd=10, width=30)
entry_fis.pack()

# Entry Inggris
kint.Label(main, text="Nilai Inggris:").pack()
entry_ing = kint.Entry(main, bd=10, width=30)
entry_ing.pack()

# ==============================
#  Logika Prediksi
# ==============================
def submit_nilai():
    nama = entry_nama.get()
    bio = entry_bio.get()
    fis = entry_fis.get()
    ing = entry_ing.get()

    # Validasi input
    if nama == "" or bio == "" or fis == "" or ing == "":
        messagebox.showerror("Error", "Semua field harus diisi!")
        return

    try:
        bio = int(bio)
        fis = int(fis)
        ing = int(ing)
    except:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    # Logika prediksi fakultas
    nilai_tertinggi = max(bio, fis, ing)

    if nilai_tertinggi == bio:
        prediksi = "Kedokteran"
    elif nilai_tertinggi == fis:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # Simpan ke database
    cur.execute("""
        INSERT INTO nilai_siswa(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, prediksi))

    conn.commit()

    # Tampilkan hasil prediksi
    messagebox.showinfo("Hasil Prediksi",
                        f"Nama: {nama}\nPrediksi Fakultas: {prediksi}")

    # Kosongkan field setelah submit
    entry_nama.delete(0, kint.END)
    entry_bio.delete(0, kint.END)
    entry_fis.delete(0, kint.END)
    entry_ing.delete(0, kint.END)


# ==============================
# Tombol Submit
# ==============================
press = kint.Button(main,
                    font=(20),
                    bg="#47c991",
                    fg="#000000",
                    text="Submit Nilai",
                    command=submit_nilai)
press.pack()

main.mainloop()


