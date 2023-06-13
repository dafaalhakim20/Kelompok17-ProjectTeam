import tkinter as tk 
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
import csv
import tkinter.font as tkfont
import datetime

main = tk.Tk()
main.state('zoomed')
main.title('RS UNS')
main.resizable(False,False)
#Gambar halaman depan
utama = Image.open('1.png')
resize = utama.resize((1920,1080),Image.LANCZOS)
utama2 = ImageTk.PhotoImage(resize)
#Bg halaman 2
bg = Image.open('3.png')
resize2 = bg.resize((1920,850),Image.LANCZOS)
bg2 = ImageTk.PhotoImage(resize2)
#Sign up
hal_signup = Image.open('signup.png')
resize3 = hal_signup.resize((1920,850),Image.LANCZOS)
hal_signup2 = ImageTk.PhotoImage(resize3)
#Sign in
hal_signin = Image.open('signin.png')
resize4 = hal_signin.resize((1920,850),Image.LANCZOS)
hal_signin2=ImageTk.PhotoImage(resize4)


nextt = Image.open('Next.png')
resizee = nextt.resize((130,40),Image.LANCZOS)
next2= ImageTk.PhotoImage(resizee)

quitt = Image.open('quit.png')
resizeee = quitt.resize((130,40),Image.LANCZOS)
quit2= ImageTk.PhotoImage(resizeee)

page_check=0
#Halaman pertama
def halaman1():
    global frame1,page_check
    if page_check == 0:
        pass
    elif page_check == 2:
        frame2.pack_forget()
    page_check = 1
    frame1 = tk.Frame(main,bg='white')
    frame1.pack(expand=True,ipadx=1920,ipady=1080)
    label = tk.Label(frame1,image=utama2)
    label.pack(fill=tk.BOTH, expand=tk.YES)
    home1 = tk.Button(label,image=next2,cursor='hand2',relief='sunken',border=0,command=halaman2)
    home1.pack(padx=300,pady=100,anchor='s',side='right')
    home2 = tk.Button(label,image=quit2,cursor='hand2',relief='sunken',border=0,command=quit)
    home2.pack(padx=300,pady=100,anchor='s',side='left')

#Halaman kedua
def halaman2():
    global frame2,page_check
    frame1.pack_forget()
    page_check = 2
    frame2 = tk.LabelFrame(main)
    frame2.pack(expand=True,ipadx=1920,ipady=1080)
    l = tk.Label(frame2,image=bg2)
    l.pack(fill=tk.BOTH, expand=tk.YES)
    font1= tkfont.Font(family='montserrat',size=12,weight='bold')
    reg1 = tk.Button(l,text='Pasien Baru',font=font1,bg='#01458e',fg='white',command=halaman3)
    reg1.pack(expand=True,ipadx=30,padx=250,ipady=10,pady=100,anchor='s',side='right')
    reg2 = tk.Button(l,text='Pasien Lama',font=font1,bg='#01458e',fg='white',command=halaman4)
    reg2.pack(expand=True,ipadx=30,ipady=10,padx=250,pady=100,anchor='s',side='left')

#Halaman ketiga
def halaman3():
    global frame3,page_check
    frame1.pack_forget()
    frame2.pack_forget()
    page_check=3
    frame3 = tk.LabelFrame(main)
    frame3.pack(expand=True,ipadx=1920,ipady=1080)
    l2 = tk.Label(frame3,image=hal_signup2,border=0)
    l2.pack(fill=tk.BOTH, expand=tk.YES)
    def signup():
        nama=ent1.get()
        email=ent2.get()
        nomor=ent3.get()
        password=ent4.get()
        password2=ent5.get()
        if ent1.get()=='' or ent2.get()=='' or ent3.get()=='' or ent4.get()=='' or ent5.get()=='':
            messagebox.showerror('Error','Mohon isi semua bidang!')
        elif password == password2:
            with open('database.csv','a',newline='')as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([nama,email,nomor,password,password2])
                messagebox.showinfo('Sign up','Registration Successful')
                next_button=tk.Button(frame,text='Next',bg='#57a1f8',fg='white',border=0,command=halaman4)
                next_button.pack(padx=10,pady=3,ipadx=20,fill='y',expand=True)
        else:
            messagebox.showerror('Invalid','password salah')

    frame = tk.LabelFrame(l2)
    frame.pack(ipadx=300,ipady=150,pady=30,side='bottom')
    nama = ttk.Label(frame,text='Nama : ')
    nama.pack(padx=10,fill='x',expand=True)
    ent1 = ttk.Entry(frame,width=100)
    ent1.pack(padx=10,fill='y',expand=True)

    email = ttk.Label(frame,text='Email : ')
    email.pack(padx=10,fill='x',expand=True)
    ent2 = ttk.Entry(frame,width=100)
    ent2.pack(padx=10,fill='y',expand=True)

    nomor = ttk.Label(frame,text='Nomor Telepon : ')
    nomor.pack(padx=10,fill='x',expand=True)
    ent3 = ttk.Entry(frame,width=100)
    ent3.pack(padx=10,fill='y',expand=True)

    password = ttk.Label(frame,text='Password : ')
    password.pack(padx=10,fill='x',expand=True)
    ent4 = ttk.Entry(frame,width=100)
    ent4.pack(padx=10,fill='y',expand=True)

    password2 = ttk.Label(frame,text='Confirm Password : ')
    password2.pack(padx=10,fill='x',expand=True)
    ent5 = ttk.Entry(frame,width=100)
    ent5.pack(padx=10,fill='y',expand=True)

    tombol = tk.Button(frame,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup)
    tombol.pack(padx=10,pady=3,ipadx=20,fill='y',expand=True)

#Halaman keempat
def halaman4():
    global frame4,page_check
    frame1.pack_forget()
    frame2.pack_forget()
    if page_check == 3:
        frame3.pack_forget()
    elif page_check == 5:
        frame5.pack_forget()
    page_check=4
    frame4 = tk.LabelFrame(main)
    frame4.pack(expand=True,ipadx=1920,ipady=1080)
    l3 = tk.Label(frame4,image=hal_signin2,border=0)
    l3.pack(fill=tk.BOTH, expand=tk.YES)
    def signin():
        email = ent2.get()
        password = ent4.get()
        email_found = False
        pass_found = False
        if ent2.get()=='' or ent4.get()=='':
            messagebox.showerror('Error','Mohon isi semua bidang!')
        else:
            with open('database.csv', 'r') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)  # Mengabaikan baris header
                for row in reader:
                    if row[1] == email:
                        email_found = True
                        if row[3] == password:
                            pass_found = True
                        break

            if email_found:
                if pass_found:
                    messagebox.showinfo('Sign in', 'Success')
                    next_button = tk.Button(f2, text='Next', bg='#57a1f8', fg='white', border=0, command=halaman5)
                    next_button.pack(padx=10, pady=3, ipadx=50, ipady=5, fill='y', expand=True)
                else:
                    messagebox.showinfo('Sign in', 'Invalid')
                
    f2 = tk.LabelFrame(l3)
    f2.pack(ipadx=300,ipady=150,pady=30,side='bottom')
    email = ttk.Label(f2,text='Email : ')
    email.pack(padx=10,fill='x',expand=True)
    ent2 = ttk.Entry(f2,width=100)
    ent2.pack(padx=10,ipady=15,expand=True)

    password = ttk.Label(f2,text='Password : ')
    password.pack(padx=10,fill='x',expand=True)
    ent4 = ttk.Entry(f2,width=100)
    ent4.pack(padx=10,ipady=15,expand=True)

    tombol = tk.Button(f2,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin)
    tombol.pack(padx=10,pady=3,ipadx=200,ipady=5,fill='y',expand=True)

#Halaman kelima
def halaman5():
    global frame5,page_check
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    page_check=5
    frame5 = tk.LabelFrame(main,bg='white')
    frame5.pack(expand=True,ipadx=600,ipady=400)
    #Label poli
    p = tk.Label(frame5, text='PEMILIHAN POLI',bg='white')
    p.config(justify='center',font='bold')
    p.pack(fill='x',ipadx=30)
    varpoli = tk.StringVar(frame5)
    varpoli.set('Pilih Poli')
    dropdown_poli = tk.OptionMenu(frame5, varpoli,'POLI ANAK','POLI KANDUNGAN','POLI KULIT DAN KELAMIN','POLI BEDAH','POLI MATA','POLI THT',
                                  'POLI AKUPUNTUR','POLI GERIATRI','POLI SYARAF','POLI PARU','POLI ORTOPEDI','POLI JIWA',
                                  'POLI JANTUNG','POLI PENYAKIT DALAM','POLI KLINIK ETETIKA','POLI TERAPI WICARA','POLI UROLOGI','POLI FOTOTERAPI')
    dropdown_poli.pack()
    #Dokter
    def display_jadwal():
        def simpan():
            pilih = tabel.focus()
            item = tabel.item(pilih)
            data = item['values']
            with open('simpandata.csv','a',newline='')as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([data])
                    messagebox.showinfo('Save','Selection Successful')
            lanjut=tk.Button(frame5,text='Next',command=halaman6)
            lanjut.pack()
        poli = varpoli.get()
        tabel = ttk.Treeview(frame5, columns=('Poli','Dokter','Jadwal Praktik'),show='headings')
        tabel.heading('Poli',text='POLI')
        tabel.heading('Dokter',text='DOKTER')
        tabel.heading('Jadwal Praktik',text='JADWAL PRAKTIK')
        tabel.column("Poli", width=150)
        tabel.column("Dokter", width=250)
        tabel.column("Jadwal Praktik", width=250)
        with open('data manual.csv','r')as file:
            csv_reader = csv.reader(file)
            if poli == 'POLI ANAK':
                for row in csv_reader:
                    if row[0]== 'POLI ANAK':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI KANDUNGAN':
                for row in csv_reader:
                    if row[0]== 'POLI KANDUNGAN':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI KULIT DAN KELAMIN':
                for row in csv_reader:
                    if row[0]== 'POLI KULIT DAN KELAMIN':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI BEDAH':
                for row in csv_reader:
                    if row[0]== 'POLI BEDAH':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI MATA':
                for row in csv_reader:
                    if row[0]== 'POLI MATA':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI THT':
                for row in csv_reader:
                    if row[0]== 'POLI THT':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI AKUPUNTUR':
                for row in csv_reader:
                    if row[0]== 'POLI AKUPUNTUR':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI GERIATRI':
                for row in csv_reader:
                    if row[0]== 'POLI GERIATRI':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI SYARAF':
                for row in csv_reader:
                    if row[0]== 'POLI SYARAF':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI PARU':
                for row in csv_reader:
                    if row[0]== 'POLI PARU':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI ORTOPEDI':
                for row in csv_reader:
                    if row[0]== 'POLI ORTOPEDI':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI JIWA':
                for row in csv_reader:
                    if row[0]== 'POLI JIWA':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI JANTUNG':
                for row in csv_reader:
                    if row[0]== 'POLI JANTUNG':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI PENYAKIT DALAM':
                for row in csv_reader:
                    if row[0]== 'POLI PENYAKIT DALAM':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI KLINIK ETETIKA':
                for row in csv_reader:
                    if row[0]== 'POLI KLINIK ETETIKA':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI TERAPI WICARA':
                for row in csv_reader:
                    if row[0]== 'POLI TERAPI WICARA':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI UROLOGI':
                for row in csv_reader:
                    if row[0]== 'POLI UROLOGI':
                        tabel.insert('','end',values=row)
            elif poli == 'POLI FOTOTERAPI':
                for row in csv_reader:
                    if row[0]== 'POLI FOTOTERAPI':
                        tabel.insert('','end',values=row)
        tabel.pack(expand=True,anchor='center')
        button_save = tk.Button(frame5,text='Save',command=simpan)
        button_save.pack(expand=True)
    button_tampilkan = tk.Button(frame5,text='Lihat Jadwal',command=display_jadwal)
    button_tampilkan.pack(expand=True,ipadx=10,pady=1)    

#Halaman 6
def halaman6():
    global frame6,page_check
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    page_check=6
    frame6 = tk.LabelFrame(main,bg='white')
    frame6.pack(expand=True,ipadx=1920,ipady=1080)
# Fungsi untuk mendapatkan nomor antrean terakhir
    def nomor_terakhir():
        with open('antrean.csv', mode='r') as file:
            next(file)
            reader = csv.reader(file)
            last_row = list(reader)[-1]
            if last_row and last_row[0].isdigit():  # Check if first element is a valid integer
                return int(last_row[0])
            else:
                return 0

    # Fungsi untuk mendapatkan perkiraan jam kedatangan
    def mendapatkan_waktu():
        last_queue_number = nomor_terakhir()
        current_time = datetime.datetime.now()
        estimated_time = current_time + datetime.timedelta(minutes=last_queue_number)
        return estimated_time.strftime("%H:%M:%S")

    # Fungsi untuk menyimpan nomor antrean ke file CSV
    def menyimpan_antrean(nomor_baru):
        waktu = mendapatkan_waktu()
        with open('antrean.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nomor_baru, waktu])
        messagebox.showinfo('Nomor Antrean','Berhasil mendapat antrean')

    # Fungsi yang akan dipanggil saat tombol "Ambil Nomor Antrean" ditekan
    def mendapatkan_antrean():
        nomor_akhir = nomor_terakhir()
        nomor_baru = nomor_akhir + 1
        menyimpan_antrean(nomor_baru)
        queue_number_label.config(text="Nomor Antrean: " + str(nomor_baru))

    # Membuat tombol "Ambil Nomor Antrean"
    button_get_queue_number = ttk.Button(frame6, text="Ambil Nomor Antrean", command=mendapatkan_antrean)
    button_get_queue_number.pack(padx=10,expand=True)

    # Membuat label untuk menampilkan nomor antrean
    queue_number_label = ttk.Label(frame6, text="Nomor Antrean: ")
    queue_number_label.pack(padx=10,expand=True)

    # Membuat label untuk menampilkan perkiraan jam kedatangan
    estimated_arrival_time_label = ttk.Label(frame6, text="Perkiraan Jam Kedatangan: ")
    estimated_arrival_time_label.pack(padx=10,expand=True)

if __name__=='__main__':
    halaman1()
main.mainloop()