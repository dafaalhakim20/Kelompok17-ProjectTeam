import tkinter as tk 
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
import ast
import csv
import tkinter.font as tkfont

main = tk.Tk()
main.geometry('600x400')
main.title('RS UNS')
main.configure(bg='white')
#Gambar halaman depan
img = tk.PhotoImage(file='1.png')
img2 = Image.open('1.png')
resize = img2.resize((600,400),Image.LANCZOS)
converted = ImageTk.PhotoImage(resize)
#Logo rs uns
logo = tk.PhotoImage(file='2.png')
logo2 = Image.open('2.png')
resize2 = logo2.resize((600,400),Image.LANCZOS)
converted2 = ImageTk.PhotoImage(resize2)
page_check=0
#Logo 2
logo = tk.PhotoImage(file='logo.png')
logo2 = Image.open('logo.png')
resize3 = logo2.resize((65,65),Image.LANCZOS)
converted3 = ImageTk.PhotoImage(resize3)
#Logo 3
resize4 = logo2.resize((100,100),Image.LANCZOS)
converted4 = ImageTk.PhotoImage(resize4)

#Halaman pertama
def halaman1():
    global frame1,page_check
    if page_check == 0:
        pass
    elif page_check == 2:
        frame2.pack_forget()
    page_check = 1
    frame1 = tk.Frame(main,bg='white')
    frame1.pack(expand=True,ipadx=600,ipady=400)
    label = tk.Label(frame1,image=converted)
    label.pack(fill=tk.BOTH, expand=tk.YES)
    font1= tkfont.Font(family='montserrat',size=12,weight='bold')
    home1 = tk.Button(label,text='Next',font=font1,bg='#01458e',fg='white',command=halaman2)
    home1.pack(expand=True,ipadx=30,ipady=5,pady=20,anchor='s',side='right')
    home2 = tk.Button(label,text='Quit',font=font1,bg='#01458e',fg='white',command=quit)
    home2.pack(expand=True,ipadx=30,ipady=5,pady=20,anchor='s',side='left')

#Halaman kedua
def halaman2():
    global frame2,page_check
    frame1.pack_forget()
    page_check = 2
    frame2 = tk.LabelFrame(main,bg='white')
    frame2.pack(expand=True,ipadx=600,ipady=400)
    l = tk.Label(frame2,image=converted2,border=0,bg='white')
    l.pack(fill=tk.BOTH, expand=tk.YES)
    font2= tkfont.Font(family='montserrat',size=20,weight='bold')
    text = tk.Label(l,text='Silahkan pilih jenis pasien :',bg='white',fg='#01458e',font=font2)
    text.pack(expand=True)
    font1= tkfont.Font(family='montserrat',size=12,weight='bold')
    reg1 = tk.Button(l,text='Pasien Baru',font=font1,bg='#01458e',fg='white',command=halaman3)
    reg1.pack(expand=True,ipadx=30,ipady=10,pady=20,anchor='s',side='right')
    reg2 = tk.Button(l,text='Pasien Lama',font=font1,bg='#01458e',fg='white',command=halaman4)
    reg2.pack(expand=True,ipadx=30,ipady=10,pady=20,anchor='s',side='left')

#Halaman ketiga
def halaman3():
    global frame3,page_check
    frame1.pack_forget()
    frame2.pack_forget()
    page_check=3
    frame3 = tk.LabelFrame(main,bg='white')
    frame3.pack(expand=True,ipadx=600,ipady=400)
    l2 = tk.Label(frame3,image=converted3,border=0,bg='white')
    l2.pack()
    heading=tk.Label(frame3,text='SIGN UP',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',14,'bold'))
    heading.pack(ipadx=5,ipady=3,pady=1,side='top')
    def signup():
        nama=ent1.get()
        email=ent2.get()
        nomor=ent3.get()
        password=ent4.get()
        password2=ent5.get()
        if password == password2:
            with open('database.csv','a')as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([nama,email,nomor,password,password2])
                messagebox.showinfo('Sign up','Registration Successful')
                next=tk.Button(frame,text='Next',bg='#57a1f8',fg='white',border=0,command=halaman4)
                next.pack(padx=10,pady=3,ipadx=20,fill='y',expand=True)
        else:
            messagebox.showerror('Invalid','password salah')

    frame = tk.LabelFrame(frame3)
    frame.pack(padx=10,pady=7,fill='y',expand=True)
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
    frame4 = tk.LabelFrame(main,bg='white')
    frame4.pack(expand=True,ipadx=600,ipady=400)
    l3 = tk.Label(frame4,image=converted4,border=0,bg='white')
    l3.pack()
    heading2=tk.Label(frame4,text='SIGN IN',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',14,'bold'))
    heading2.pack(ipadx=5,ipady=3,pady=1,side='top')
    def signin():
        email=ent2.get()
        password=ent4.get()
        with open('database.csv','r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[1]!=email or row[3]!=password:
                    pass
                elif row[1]==email and row[3]==password:
                    messagebox.showinfo('Sign in','Sucess')  
                    next=tk.Button(f2,text='Next',bg='#57a1f8',fg='white',border=0,command=halaman5)
                    next.pack(padx=10,pady=3,ipadx=50,ipady=5,fill='y',expand=True)
                    break

    f2 = tk.LabelFrame(frame4)
    f2.pack(padx=10,pady=7,fill='y',expand=True)
    email = ttk.Label(f2,text='Email : ')
    email.pack(padx=10,fill='x',expand=True)
    ent2 = ttk.Entry(f2,width=100)
    ent2.pack(padx=10,ipady=15,expand=True)

    password = ttk.Label(f2,text='Password : ')
    password.pack(padx=10,fill='x',expand=True)
    ent4 = ttk.Entry(f2,width=100)
    ent4.pack(padx=10,ipady=15,expand=True)

    tombol = tk.Button(f2,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin)
    tombol.pack(padx=10,pady=3,ipadx=50,ipady=5,fill='y',expand=True)

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
        poli = varpoli.get()
        list = ttk.Treeview(frame5, columns=('Poli','Dokter','Jadwal Praktik'),show='headings')
        list.heading('Poli',text='POLI')
        list.heading('Dokter',text='DOKTER')
        list.heading('Jadwal Praktik',text='JADWAL PRAKTIK')
        list.column("Poli", width=150)
        list.column("Dokter", width=250)
        list.column("Jadwal Praktik", width=250)
        with open('data manual.csv','r')as file:
            csv_reader = csv.reader(file)
            if poli == 'POLI ANAK':
                for row in csv_reader:
                    if row[0]== 'POLI ANAK':
                        list.insert('','end',values=row)
            elif poli == 'POLI KANDUNGAN':
                for row in csv_reader:
                    if row[0]== 'POLI KANDUNGAN':
                        list.insert('','end',values=row)
            elif poli == 'POLI KULIT DAN KELAMIN':
                for row in csv_reader:
                    if row[0]== 'POLI KULIT DAN KELAMIN':
                        list.insert('','end',values=row)
            elif poli == 'POLI BEDAH':
                for row in csv_reader:
                    if row[0]== 'POLI BEDAH':
                        list.insert('','end',values=row)
            elif poli == 'POLI MATA':
                for row in csv_reader:
                    if row[0]== 'POLI MATA':
                        list.insert('','end',values=row)
            elif poli == 'POLI THT':
                for row in csv_reader:
                    if row[0]== 'POLI THT':
                        list.insert('','end',values=row)
            elif poli == 'POLI AKUPUNTUR':
                for row in csv_reader:
                    if row[0]== 'POLI AKUPUNTUR':
                        list.insert('','end',values=row)
            elif poli == 'POLI GERIATRI':
                for row in csv_reader:
                    if row[0]== 'POLI GERIATRI':
                        list.insert('','end',values=row)
            elif poli == 'POLI SYARAF':
                for row in csv_reader:
                    if row[0]== 'POLI SYARAF':
                        list.insert('','end',values=row)
            elif poli == 'POLI PARU':
                for row in csv_reader:
                    if row[0]== 'POLI PARU':
                        list.insert('','end',values=row)
            elif poli == 'POLI ORTOPEDI':
                for row in csv_reader:
                    if row[0]== 'POLI ORTOPEDI':
                        list.insert('','end',values=row)
            elif poli == 'POLI JIWA':
                for row in csv_reader:
                    if row[0]== 'POLI JIWA':
                        list.insert('','end',values=row)
            elif poli == 'POLI JANTUNG':
                for row in csv_reader:
                    if row[0]== 'POLI JANTUNG':
                        list.insert('','end',values=row)
            elif poli == 'POLI PENYAKIT DALAM':
                for row in csv_reader:
                    if row[0]== 'POLI PENYAKIT DALAM':
                        list.insert('','end',values=row)
            elif poli == 'POLI KLINIK ETETIKA':
                for row in csv_reader:
                    if row[0]== 'POLI KLINIK ETETIKA':
                        list.insert('','end',values=row)
            elif poli == 'POLI TERAPI WICARA':
                for row in csv_reader:
                    if row[0]== 'POLI TERAPI WICARA':
                        list.insert('','end',values=row)
            elif poli == 'POLI UROLOGI':
                for row in csv_reader:
                    if row[0]== 'POLI UROLOGI':
                        list.insert('','end',values=row)
            elif poli == 'POLI FOTOTERAPI':
                for row in csv_reader:
                    if row[0]== 'POLI FOTOTERAPI':
                        list.insert('','end',values=row)
        list.pack(expand=True,anchor='center')
    button_tampilkan = tk.Button(frame5,text='Lihat Jadwal',command=display_jadwal)
    button_tampilkan.pack(expand=True,ipadx=10,pady=1)    
if __name__=='__main__':
    halaman1()
main.mainloop()