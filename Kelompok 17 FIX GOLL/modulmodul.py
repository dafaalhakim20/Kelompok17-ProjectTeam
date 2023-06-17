import tkinter as tk 
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
import csv
import datetime
from customtkinter import *
from reportlab.pdfgen import canvas
import emailsender as es
# main = tk.Tk()
# main.state('zoomed')
# main.title('RS UNS')
# main.resizable(False,False)

# page_check=0
#Halaman pertama
def halaman1(main,page_check):
    global utama,gambar_next2
    if page_check == 0:
        pass
    elif page_check == 2:
        frame2.pack_forget()
    page_check = 1
    utama = ImageTk.PhotoImage(Image.open('1 baru lagi.png'))
    frame1 = tk.Frame(main,bg='white')
    frame1.pack(expand=True,ipadx=1920,ipady=1080)
    label = tk.Label(frame1,image=utama)
    label.pack(fill=tk.BOTH, expand=tk.YES)
    gambar_quit = Image.open('quit.png')
    resize1 = gambar_quit.resize((300,60),Image.LANCZOS)
    gambar_quit2= ImageTk.PhotoImage(resize1)
    tombolquit = CTkButton(label,text="", image=gambar_quit2,cursor='hand2',border_spacing=0,command=quit, fg_color="transparent")
    tombolquit.pack(padx=240,pady=100,anchor='s',side='left')
    gambar_next = Image.open('Next.png')
    resize2 = gambar_next.resize((300,60),Image.LANCZOS)
    gambar_next2= ImageTk.PhotoImage(resize2)
    tommbolnext = CTkButton(label,text="", image=gambar_next2,cursor='hand2',border_spacing=0,command=lambda:halaman2(frame1,main,page_check), fg_color="transparent")
    tommbolnext.pack(padx=180,pady=100,anchor='s',side='right')

#Halaman kedua
def halaman2(frame,main,page_check):
    global frame2,bg
    frame.pack_forget()
    page_check = 2
    frame2 = tk.LabelFrame(main)
    frame2.pack(expand=True,ipadx=1920,ipady=1080)
    bg = ImageTk.PhotoImage(Image.open('2 baru.png'))
    l = tk.Label(frame2,image=bg)
    l.pack(fill=tk.BOTH, expand=tk.YES)
    pasien_lama = Image.open('pasien lama.png')
    size1 = pasien_lama.resize((350,64),Image.LANCZOS)
    pasien_lama2= ImageTk.PhotoImage(size1)
    tombol_pasienlama = CTkButton(l,text='',image=pasien_lama2,cursor='hand2',border_spacing=0,command=lambda:halaman4(main,page_check), fg_color="transparent")
    tombol_pasienlama.pack(padx=200,pady=380,anchor='s',side='left')
    pasien_baru = Image.open('pasien baru.png')
    size2 = pasien_baru.resize((350,64),Image.LANCZOS)
    pasien_baru2= ImageTk.PhotoImage(size2)
    tombol_pasienbaru= CTkButton(l,text='',image=pasien_baru2,cursor='hand2',border_spacing=0,command=lambda:halaman3(main,page_check), fg_color="transparent")
    tombol_pasienbaru.pack(padx=180,pady=380,anchor='s',side='right')

def signup(username, email_user, user_number, user_password, pw2,main,page_check):
    nama=username.get()
    email=email_user.get()
    nomor=user_number.get()
    password=user_password.get()
    password2=pw2.get()
    if nama==' 'or email==' ' :
        messagebox.showerror('Error','Mohon isi semua bidang!')
    elif password == password2:
        with open('abc.csv','a',newline='')as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([nama,email,nomor,password,password2])
            messagebox.showinfo('Sign up','Registration Successful')
            halaman4(main,page_check)
    else:
        messagebox.showerror('Invalid','password salah')

def signin(email_user,pw_user,main,frame,page_check):
    email = email_user.get()
    password = pw_user.get()
    email_found = False
    pass_found = False
    if email_user.get()=='' or pw_user.get()=='':
        messagebox.showerror('Error','Mohon isi semua bidang!')
    else:
        with open('abc.csv', 'r') as file:
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
                halaman5(frame,main,page_check,email)
            else:
                messagebox.showerror('Sign in', 'Invalid')


#Halaman ketiga
def halaman3(main,page_check):
    global frame3,hal_signup
    frame2.pack_forget()
    page_check=3
    frame3 = tk.LabelFrame(main)
    frame3.pack(expand=True,ipadx=1920,ipady=1080)
    hal_signup = ImageTk.PhotoImage(Image.open('b3 baru.png'))
    l2 = tk.Label(frame3,image=hal_signup,border=0)
    l2.pack(fill=tk.BOTH, expand=tk.YES)
    

    def on_enter(e):
        enter1.delete(0,'end')
    def on_leave(e):
        if enter1.get=='':
            enter1.insert(0,'Username')
    enter1 = ttk.Entry(l2,width=70)
    enter1.place(x=910,y=325)
    enter1.insert(0,'Username')
    enter1.bind('<FocusIn>',on_enter)
    enter1.bind('<FocusOut>',on_leave)

    def on_enter(e):
        enter2.delete(0,'end')
    def on_leave(e):
        if enter2.get=='':
            enter2.insert(0,'Email')
    enter2 = ttk.Entry(l2,width=70)
    enter2.place(x=910,y=375)
    enter2.insert(0,'Email')
    enter2.bind('<FocusIn>',on_enter)
    enter2.bind('<FocusOut>',on_leave)

    def on_enter(e):
        enter3.delete(0,'end')
    def on_leave(e):
        if enter3.get=='':
            enter3.insert(0,'Nomor Telepon')
    enter3 = ttk.Entry(l2,width=70)
    enter3.place(x=910,y=425)
    enter3.insert(0,'Nomor Telepon')
    enter3.bind('<FocusIn>',on_enter)
    enter3.bind('<FocusOut>',on_leave)

    def on_enter(e):
        enter4.delete(0,'end')
    def on_leave(e):
        if enter4.get=='':
            enter4.insert(0,'Password')
    enter4 = ttk.Entry(l2,width=70)
    enter4.place(x=910,y=475)
    enter4.insert(0,'Password')
    enter4.bind('<FocusIn>',on_enter)
    enter4.bind('<FocusOut>',on_leave)

    def on_enter(e):
        enter5.delete(0,'end')
    def on_leave(e):
        if enter5.get=='':
            enter5.insert(0,'Confirm Password')
    enter5 = ttk.Entry(l2,width=70)
    enter5.place(x=910,y=525)
    enter5.insert(0,'Confirm Password')
    enter5.bind('<FocusIn>',on_enter)
    enter5.bind('<FocusOut>',on_leave)

    sign_up = Image.open('Sign up.png')
    size3 = sign_up.resize((186,38),Image.LANCZOS)
    sign_up2= ImageTk.PhotoImage(size3)
    tombol_signup= CTkButton(l2,text='',image=sign_up2,cursor='hand2',border_spacing=0,command=lambda:signup(enter1,enter2,enter3,enter4,enter5,main,page_check), fg_color="transparent",bg_color='#5568B6')
    tombol_signup.pack(padx=310,pady=200,anchor='s',side='right')



#Halaman keempat
def halaman4(main,page_check):
    global frame4,hal_signin
    frame2.pack_forget()
    if page_check == 3:
        frame3.pack_forget()
    elif page_check == 5:
        frame5.pack_forget()
    page_check=4
    frame4 = tk.LabelFrame(main)
    frame4.pack(expand=True,ipadx=1920,ipady=1080)
    hal_signin = ImageTk.PhotoImage(Image.open('4 baru.png'))
    l3 = tk.Label(frame4,image=hal_signin,border=0)
    l3.pack(fill=tk.BOTH, expand=tk.YES)
    

    def on_enter(e):
        enter2.delete(0,'end')
    def on_leave(e):
        if enter2.get=='':
           enter2.insert(0,'Email')
    enter2 = ttk.Entry(l3,width=70)
    enter2.place(x=185,y=335)
    enter2.insert(0,'Email')
    enter2.bind('<FocusIn>',on_enter)
    enter2.bind('<FocusOut>',on_leave)
    def on_enter(e):
        enter4.delete(0,'end')
    def on_leave(e):
        if enter4.get=='':
            enter4.insert(0,'Password')
    enter4 = ttk.Entry(l3,width=70)
    enter4.place(x=185,y=385)
    enter4.insert(0,'Password')
    enter4.bind('<FocusIn>',on_enter)
    enter4.bind('<FocusOut>',on_leave)
    sign_in = Image.open('Sign in.png')
    size4 = sign_in.resize((186,38),Image.LANCZOS)
    sign_in2= ImageTk.PhotoImage(size4)
    tombol_signin= CTkButton(l3,text='',image=sign_in2,cursor='hand2',border_spacing=0,command=lambda: signin(enter2,enter4,main,frame4,page_check), fg_color="transparent",bg_color='#5568B6')
    tombol_signin.pack(padx=290,pady=350,anchor='s',side='left')
    

#Halaman kelima
def halaman5(frame,main,page_check,email):
    global frame5,hal_5,gambar_jadwal2,tombol_jadwal
    page_check=5
    frame.pack_forget()
    frame5 = tk.LabelFrame(main)
    frame5.pack(expand=True,ipadx=1920,ipady=1080)
    hal_5 = ImageTk.PhotoImage(Image.open('5.png'))
    hal5 = tk.Label(frame5,image=hal_5)
    hal5.pack(fill=tk.BOTH, expand=tk.YES)
    #Label poli
    varpoli = tk.StringVar(hal5)
    varpoli.set('Pilih Poli')
    dropdown_poli = tk.OptionMenu(hal5, varpoli,'POLI ANAK','POLI KANDUNGAN','POLI KULIT DAN KELAMIN','POLI BEDAH','POLI MATA','POLI THT',
                                  'POLI AKUPUNTUR','POLI GERIATRI','POLI SYARAF','POLI PARU','POLI ORTOPEDI','POLI JIWA',
                                  'POLI JANTUNG','POLI PENYAKIT DALAM','POLI KLINIK ETETIKA','POLI TERAPI WICARA','POLI UROLOGI','POLI FOTOTERAPI')
    dropdown_poli.pack(side='top', padx=660, pady=205, ipadx=28, ipady=10)
    #Dokter
    def display_jadwal(email):
        global gambar_save2,tombol_save
        def simpan(main,page_check,email):
            pilih = tabel.focus()
            item = tabel.item(pilih)
            data = item['values']
            with open('simpandata.csv','a',newline='')as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([data])
                    if data == '':
                        messagebox.showerror('Invalid','Pilih Dokter')
                    else:
                        messagebox.showinfo('Save','Selection Successful')
                        halaman6(main,page_check,email)
        poli = varpoli.get()
        tabel = ttk.Treeview(hal5, columns=('Poli','Dokter','Jadwal Praktik'),show='headings')
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
        tabel.place(x=465,y=303,width=600,height=300)
        gambar_save = Image.open('save.png')
        size6 = gambar_save.resize((170,50),Image.LANCZOS)
        gambar_save2= ImageTk.PhotoImage(size6)
        tombol_save= CTkButton(hal5,text='',image=gambar_save2,cursor='hand2',border_spacing=0,command=lambda:simpan(main,page_check,email),fg_color="transparent")
        tombol_save.pack(padx=250,pady=20,anchor='s',side='left')
    gambar_jadwal = Image.open('Jadwal.png')
    size5 = gambar_jadwal.resize((264,50),Image.LANCZOS)
    gambar_jadwal2= ImageTk.PhotoImage(size5)
    tombol_jadwal= CTkButton(hal5,text='',image=gambar_jadwal2,cursor='hand2',border_spacing=0,command=lambda:display_jadwal(email),fg_color="transparent")
    tombol_jadwal.pack(padx=266,pady=20,anchor='s',side='left')  

def help(frame, fungsi):
    frame.pack_forget()
    fungsi()

#Halaman 6
def halaman6(main,page_check,email):
    global frame6,hal_6,nomor_antrean,perkiraan_waktu
    frame4.pack_forget()
    frame5.pack_forget()
    page_check=6
    frame6 = tk.LabelFrame(main,bg='white')
    frame6.pack(expand=True,ipadx=1920,ipady=1080)
    hal_6 = ImageTk.PhotoImage(Image.open('antrian.png'))
    hal6 = tk.Label(frame6,image=hal_6)
    hal6.pack(fill=tk.BOTH, expand=tk.YES)
    def nomor_terakhir():
        global last_row
        with open('antrean.csv', mode='r') as file:
            next(file)
            reader = csv.reader(file)
            last_row = list(reader)[-1]
            if last_row and last_row[0].isdigit():  # Check if first element is a valid integer
                return int(last_row[0])
            else:
                return 0
    def menyimpan_antrean(nomor_baru):
        global jam
        waktu = datetime.datetime.now()
        jam = waktu.strftime("%H:%M:%S")
        with open('antrean.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nomor_baru, jam])
        pdf()
        messagebox.showinfo('Antrean','Berhasil mendapat antrean!')
        return nomor_antrean,perkiraan_waktu,waktu.strftime("%H:%M:%S")
    
    def mendapatkan_antrean(email):
        global nomor_baru
        nomor_akhir = nomor_terakhir()
        nomor_baru = nomor_akhir + 1
        menyimpan_antrean(nomor_baru)
        estimated_arrival_time = jam 
        nomor_baru = str(nomor_baru)
        nomor_antrean.config(text="Nomor Antrean: " + nomor_baru)
        perkiraan_waktu.config(text='Jam Pendaftaran: ' + str(estimated_arrival_time))
        es.kirim_nomor_antrian(nomor_baru,email)

    def pdf():
        with open('simpandata.csv','r')as file:
            csv_reader = csv.reader(file)
            last_row = list(csv_reader)[-1]
        c= canvas.Canvas('Antrean.pdf')
        c.drawString(100,750,f'Nomor Antrean : {str(nomor_baru)}')
        c.drawString(100,700,str(last_row))
        c.save()
        
    nomor_antrean = tk.Label(hal6,bg='#5568B6',text="Nomor Antrean: ",fg="white")
    nomor_antrean.place(x=610,y=620,width=300,height=100)
    perkiraan_waktu = tk.Label(hal6,bg='#5568B6',text="Jam Pendaftaran: ",fg="white")
    perkiraan_waktu.place(x=610,y=410,width=300,height=100)
    gambar_antrean = Image.open('ambil no antrean.png')
    size7 = gambar_antrean.resize((443,48),Image.LANCZOS)
    gambar_antrean2= ImageTk.PhotoImage(size7)
    tombol_antrean= CTkButton(hal6,text='',image=gambar_antrean2,cursor='hand2',border_spacing=0,command=lambda:mendapatkan_antrean(email), fg_color="transparent",bg_color='transparent')
    tombol_antrean.pack(padx=250,pady=200)
    gambar_keluar = Image.open('quit2.png')
    resize = gambar_keluar.resize((192,51),Image.LANCZOS)
    gambar_keluar2= ImageTk.PhotoImage(resize)
    tombol_keluar= CTkButton(hal6,text='',image=gambar_keluar2,cursor='hand2',border_spacing=0,command=quit, fg_color="transparent")
    tombol_keluar.pack(padx=70,pady=20,anchor='s',side='right')
    gambar_kembali = Image.open('back.png')
    resize = gambar_kembali.resize((192,51),Image.LANCZOS)
    gambar_kembali2= ImageTk.PhotoImage(resize)
    tombol_kembali= CTkButton(hal6,text='',image=gambar_kembali2,cursor='hand2',border_spacing=0,command=lambda: halaman5(frame6,main,page_check,email),fg_color="transparent")
    tombol_kembali.pack(padx=50,pady=20,anchor='s',side='left')

# if __name__=='__main__':
#     halaman1()
# main.mainloop()