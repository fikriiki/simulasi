import tkinter as tk
from tkinter import messagebox, simpledialog
import csv

# Global variable to store history and passing score
history = []
passing_score = 60

def toggle_fullscreen(event=None):
    window.attributes("-fullscreen", True)

def end_fullscreen(event=None):
    window.attributes("-fullscreen", False)

def hitung_hasil():
    try:
        nilai1 = float(entry_nilai1.get())
        nilai2 = float(entry_nilai2.get())
        nilai3 = float(entry_nilai3.get())
        
        # Validasi nilai
        if not (0 <= nilai1 <= 100 and 0 <= nilai2 <= 100 and 0 <= nilai3 <= 100):
            raise ValueError("Nilai harus antara 0 dan 100.")

        # Menghitung rata-rata
        rata_rata = (nilai1 + nilai2 + nilai3) / 3

        # Menentukan lulus atau gagal
        if rata_rata >= passing_score:
            hasil = f"Rata-rata: {rata_rata:.2f}. BERARTI LU LULUS!!!."
        else:
            hasil = f"Rata-rata: {rata_rata:.2f}. BERARTI LU GAGAL!!!."

        # Menyimpan ke riwayat
        history.append(rata_rata)

        # Menampilkan hasil dalam messagebox
        messagebox.showinfo("Hasil", hasil)
   
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    entry_nilai1.delete(0, tk.END)
    entry_nilai2.delete(0, tk.END)
    entry_nilai3.delete(0, tk.END)

def reset_history():
    global history
    history = []
    messagebox.showinfo("Reset", "Riwayat nilai telah direset.")

def show_history():
    if history:
        history_str = "\n".join(f"Rata-rata: {rata:.2f}" for rata in history)
        messagebox.showinfo("Riwayat Nilai", history_str)
    else:
        messagebox.showinfo("Riwayat Nilai", "Tidak ada riwayat nilai.")

def set_passing_score():
    global passing_score
    new_score = simpledialog.askfloat("Set Batas Lulus", "Masukkan batas lulus (0-100):", minvalue=0, maxvalue=100)
    if new_score is not None:
        passing_score = new_score
        messagebox.showinfo("Batas Lulus", f"Batas lulus telah diatur menjadi {passing_score:.2f}")

def export_history():
    if history:
        with open("riwayat_nilai.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Percobaan", "Rata-rata"])
            for i, rata in enumerate(history, 1):
                writer.writerow([i, rata])
        messagebox.showinfo("Ekspor", "Riwayat nilai berhasil diekspor ke riwayat_nilai.csv")
    else:
        messagebox.showinfo("Ekspor", "Tidak ada data untuk diekspor.")

def show_help():
    help_message = "Petunjuk Penggunaan:\n" \
                   "- Masukkan tiga nilai dalam rentang 0-100.\n" \
                   "- Klik 'Hitung' untuk mendapatkan hasil.\n" \
                   "- Anda dapat melihat riwayat nilai dan mengekspornya ke file CSV."
    messagebox.showinfo("Bantuan", help_message)

def go_back():
    window.destroy()  # Close the window

# Membuat jendela aplikasi
window = tk.Tk()
window.title("~Penentuan nilai lu~")
window.geometry("600x600")

# Mengatur font untuk label dan entry
label_font = ("Arial", 16)
entry_font = ("Arial", 16)

# Membuat frame untuk menampung semua widget
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Label dan Entry untuk Nilai 1
label_nilai1 = tk.Label(window, text="Masukkan nilai1:", font=label_font)
label_nilai1.grid(row=0, column=0, padx=30, pady=30)
entry_nilai1 = tk.Entry(window, font=entry_font, borderwidth=10)
entry_nilai1.grid(row=0, column=1, padx=30, pady=30)

# Label dan Entry untuk Nilai 2
label_nilai2 = tk.Label(window, text="Masukkan nilai2:", font=label_font)
label_nilai2.grid(row=1, column=0, padx=30, pady=30)
entry_nilai2 = tk.Entry(window, font=entry_font, borderwidth=10)
entry_nilai2.grid(row=1, column=1, padx=30, pady=30)

# Label dan Entry untuk Nilai 3
label_nilai3 = tk.Label(window, text="Masukkan nilai3:", font=label_font)
label_nilai3.grid(row=2, column=0, padx=30, pady=30)
entry_nilai3 = tk.Entry(window, font=entry_font, borderwidth=10)
entry_nilai3.grid(row=2, column=1, padx=30, pady=30)

# Tombol untuk menghitung hasil
button_hitung = tk.Button(window, text="Hitung", command=hitung_hasil, font=label_font, bg="lightblue")
button_hitung.grid(row=3, column=0, columnspan=2, padx=30, pady=20)

# Tombol untuk membersihkan input
button_clear = tk.Button(window, text="Hapus", command=clear_fields, font=label_font, bg="orange")
button_clear.grid(row=4, column=0, columnspan=2, padx=30, pady=20)

# Tombol untuk menampilkan riwayat nilai
button_history = tk.Button(window, text="Riwayat Nilai", command=show_history, font=label_font, bg="lightblue")
button_history.grid(row=5, column=0, padx=30, pady=20)

# Tombol untuk reset riwayat nilai
button_reset = tk.Button(window, text="Reset Riwayat", command=reset_history, font=label_font, bg="orange")
button_reset.grid(row=5, column=1, padx=30, pady=20)

# Tombol untuk mengatur batas lulus
button_set_score = tk.Button(window, text="Atur Batas Lulus", command=set_passing_score, font=label_font, bg="lightgray")
button_set_score.grid(row=7, column=0, columnspan=2, padx=30, pady=20)

# Tombol untuk mengekspor riwayat nilai
button_export = tk.Button(window, text="Ekspor Riwayat", command=export_history, font=label_font, bg="lightgray")
button_export.grid(row=8, column=0, columnspan=2, padx=30, pady=20)

# Menjalankan aplikasi
window.mainloop()
