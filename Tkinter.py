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

# Melanjutkan Praktikumpertemuan selanjutnya:
# Menambahkan kondisi nilaiyang berbeda untuk setiap pilihan prodi yang diinginkan
# Menambahkanpenyimpanan data keSQLLite
# Buat table nilai_siswa
# Buat atribut yang berisi nama_siswa, biologi, fisika, inggris, prediksi_fakultas
# Buat entry menggunakan tkinter untuk nama siswa, biologi, fisika, dan inggris
# Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran
# Jika nilai Fisika paling tinggi, maka hasil prediksi = Teknik
# Jika nilai Inggris paling tinggi, maka hasil prediksi = Bahasa
# Terdapat button tkinter untuk submit nilai

import tkinter as kint
from tkinter import messagebox, ttk
import sqlite3

# ==============================
#  Database setup
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


# ============================================================
# ===============   WINDOW MENU UTAMA  ========================
# ============================================================
def menu_utama():
    menu = kint.Tk()
    menu.title("Menu Utama")
    menu.geometry("420x380")
    menu.configure(bg="#e8f5e9")

    header = kint.Label(
        menu,
        text="Menu Utama",
        font=("Segoe UI", 20, "bold"),
        bg="#43a047",
        fg="white",
        pady=15
    )
    header.pack(fill="x", pady=10)

    # Tombol Input Nilai
    kint.Button(
        menu,
        text="Input Nilai Siswa",
        font=("Segoe UI", 14, "bold"),
        bg="#1e88e5",
        fg="white",
        relief="flat",
        padx=10, pady=10,
        command=lambda: [menu.destroy(), halaman_input()]
    ).pack(pady=10, fill="x", padx=50)

    # Tombol Cari Data
    kint.Button(
        menu,
        text="Cari Data Siswa",
        font=("Segoe UI", 14, "bold"),
        bg="#6a1b9a",
        fg="white",
        relief="flat",
        padx=10, pady=10,
        command=lambda: [menu.destroy(), halaman_cari()]
    ).pack(pady=10, fill="x", padx=50)

    # Tombol Lihat History
    kint.Button(
        menu,
        text="Lihat History Pencarian",
        font=("Segoe UI", 14, "bold"),
        bg="#00897b",
        fg="white",
        relief="flat",
        padx=10, pady=10,
        command=lambda: [menu.destroy(), lihat_data()]
    ).pack(pady=10, fill="x", padx=50)

    # Tombol Close
    kint.Button(
        menu,
        text="Close Aplikasi",
        font=("Segoe UI", 14, "bold"),
        bg="#e53935",
        fg="white",
        relief="flat",
        padx=10, pady=10,
        command=menu.destroy
    ).pack(pady=10, fill="x", padx=50)

    menu.mainloop()


# ============================================================
# ===============   HALAMAN INPUT NILAI  ======================
# ============================================================
def halaman_input():
    main = kint.Tk()
    main.title("Input Nilai Siswa")
    main.geometry("470x520")
    main.configure(bg="#e8f5e9")

    header = kint.Label(
        main,
        text="Input Nilai Siswa",
        font=("Segoe UI", 20, "bold"),
        bg="#43a047",
        fg="white",
        pady=15
    )
    header.pack(fill="x")

    frame = kint.Frame(main, bg="#ffffff", bd=2, relief="ridge")
    frame.pack(pady=20, padx=20, fill="both")

    def add_label(text):
        kint.Label(frame, text=text, bg="#ffffff",
                   font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=10, pady=(10, 0))

    def add_entry():
        ent = kint.Entry(frame, font=("Segoe UI", 11), bd=2, relief="solid")
        ent.pack(padx=10, pady=5, fill="x")
        return ent

    # INPUT
    add_label("Nama Siswa:")
    entry_nama = add_entry()

    add_label("Nilai Biologi:")
    entry_bio = add_entry()

    add_label("Nilai Fisika:")
    entry_fis = add_entry()

    add_label("Nilai Inggris:")
    entry_ing = add_entry()

    # LOGIKA INPUT
    def submit_nilai():
        nama = entry_nama.get()
        bio = entry_bio.get()
        fis = entry_fis.get()
        ing = entry_ing.get()

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

        tertinggi = max(bio, fis, ing)

        if tertinggi == bio:
            prediksi = "Kedokteran"
        elif tertinggi == fis:
            prediksi = "Teknik"
        else:
            prediksi = "Bahasa"

        cur.execute("""
            INSERT INTO nilai_siswa(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """, (nama, bio, fis, ing, prediksi))
        conn.commit()

        messagebox.showinfo("Hasil", f"Nama: {nama}\nPrediksi: {prediksi}")

        entry_nama.delete(0, kint.END)
        entry_bio.delete(0, kint.END)
        entry_fis.delete(0, kint.END)
        entry_ing.delete(0, kint.END)

    # Tombol Submit
    kint.Button(
        main, text="Submit Nilai",
        font=("Segoe UI", 14, "bold"),
        bg="#43a047", fg="white",
        relief="flat", padx=10, pady=10,
        command=submit_nilai
    ).pack(pady=10)

    # Tombol kembali ke menu
    kint.Button(
        main, text="Kembali ke Menu",
        font=("Segoe UI", 12, "bold"),
        bg="#1e88e5", fg="white",
        relief="flat", padx=10, pady=5,
        command=lambda: [main.destroy(), menu_utama()]
    ).pack(pady=5)

    main.mainloop()


# ============================================================
# ===============   FITUR CARI DATA SISWA  ===================
# ============================================================
def halaman_cari():
    cari = kint.Tk()
    cari.title("Cari Data Siswa")
    cari.geometry("450x320")
    cari.configure(bg="#fafafa")

    kint.Label(
        cari, text="Cari Data Siswa",
        font=("Segoe UI", 18, "bold"),
        bg="#6a1b9a", fg="white", pady=10
    ).pack(fill="x")

    # Input nama
    kint.Label(cari, text="Masukkan Nama Siswa:",
               font=("Segoe UI", 12, "bold"), bg="#fafafa").pack(pady=10)
    entry = kint.Entry(cari, font=("Segoe UI", 12), bd=2, relief="solid")
    entry.pack(pady=5, fill="x", padx=20)

    def cari_data():
        nama = entry.get()

        if nama == "":
            messagebox.showerror("Error", "Nama tidak boleh kosong!")
            return

        cur.execute(
            "SELECT * FROM nilai_siswa WHERE nama_siswa LIKE ?", ('%' + nama + '%',))
        rows = cur.fetchall()

        if not rows:
            messagebox.showinfo("Hasil", "Data tidak ditemukan.")
            return

        # tampilkan hasil dalam tabel
        tampilkan_tabel("Hasil Pencarian", rows)

    # Tombol cari
    kint.Button(
        cari, text="Cari",
        font=("Segoe UI", 14, "bold"),
        bg="#6a1b9a", fg="white",
        relief="flat", padx=10, pady=10,
        command=cari_data
    ).pack(pady=10)

    kint.Button(
        cari, text="Kembali ke Menu",
        font=("Segoe UI", 12, "bold"),
        bg="#1e88e5", fg="white",
        relief="flat", padx=10, pady=5,
        command=lambda: [cari.destroy(), menu_utama()]
    ).pack(pady=10)

    cari.mainloop()


# ============================================================
# ===============   TAMPILKAN TABEL (UMUM)  ==================
# ============================================================
def tampilkan_tabel(judul, data):
    win = kint.Toplevel()
    win.title(judul)
    win.geometry("700x400")

    kint.Label(
        win, text=judul, font=("Segoe UI", 14, "bold"),
        bg="#00897b", fg="white", pady=10
    ).pack(fill="x")

    cols = ("ID", "Nama", "Biologi", "Fisika", "Inggris", "Fakultas")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, anchor="center")

    for row in data:
        tree.insert("", kint.END, values=row)

    tree.pack(fill="both", expand=True)


# ============================================================
# ===============   FITUR HISTORY DATA  =======================
# ============================================================
def lihat_data():
    cur.execute("SELECT * FROM nilai_siswa")
    data = cur.fetchall()
    tampilkan_tabel("History Data Siswa", data)
    menu_utama()


# ============================================================
#  JALANKAN APLIKASI
# ============================================================
menu_utama()