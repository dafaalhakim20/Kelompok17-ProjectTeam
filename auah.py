import tkinter as tk 
from PIL import Image,ImageTk
from tkinter import messagebox,ttk
import ast
import csv

main = tk.Tk()
main.geometry('600x400')
main.title('RS UNS')
main.configure(bg='white')
#Gambar halaman depan
img = tk.PhotoImage(file='uns.png')
img2 = Image.open('uns.png')
resize = img2.resize((600,330),Image.LANCZOS)
converted = ImageTk.PhotoImage(resize)
#Logo rs uns
logo = tk.PhotoImage(file='logo.png')
logo2 = Image.open('logo.png')
resize2 = logo2.resize((200,200),Image.LANCZOS)
converted2 = ImageTk.PhotoImage(resize2)
page_check=0
#Logo 2
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
    label.pack()
    home1 = tk.Button(frame1,text='Next',font=('arial',12),bg='#082B59',fg='white',command=halaman2)
    home1.pack(expand=True,ipadx=30,ipady=5,side='right')
    home2 = tk.Button(frame1,text='Quit',font=('arial',12),bg='#082B59',fg='white',command=quit)
    home2.pack(expand=True,ipadx=30,ipady=5,side='left')

#Halaman kedua
def halaman2():
    global frame2,page_check
    frame1.pack_forget()
    page_check = 2
    frame2 = tk.LabelFrame(main,bg='white')
    frame2.pack(expand=True,ipadx=600,ipady=400)
    l = tk.Label(frame2,image=converted2,border=0,bg='white')
    l.pack(pady=20)
    text = tk.Label(frame2,text='Silahkan pilih jenis pasien :',bg='white',fg='#57a1f8',font=('Microsoft Yahei UI Light',20,'bold'))
    text.pack(expand=True)
    reg1 = tk.Button(frame2,text='Pasien Baru',bg='#57a1f8',fg='white',command=halaman3)
    reg1.pack(expand=True,ipadx=30,ipady=10,pady=20,side='right')
    reg2 = tk.Button(frame2,text='Pasien Lama',bg='#57a1f8',fg='white',command=halaman4)
    reg2.pack(expand=True,ipadx=30,ipady=10,pady=20,side='left')

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
                next=tk.Button(f1,text='Next',bg='#57a1f8',fg='white',border=0,command=halaman5)
                next.pack(padx=10,pady=3,ipadx=20,fill='y',expand=True)
        else:
            messagebox.showerror('Invalid','password salah')

    f1 = tk.LabelFrame(frame3)
    f1.pack(padx=10,pady=7,fill='y',expand=True)
    nama = ttk.Label(f1,text='Nama : ')
    nama.pack(padx=10,fill='x',expand=True)
    ent1 = ttk.Entry(f1,width=100)
    ent1.pack(padx=10,fill='y',expand=True)

    email = ttk.Label(f1,text='Email : ')
    email.pack(padx=10,fill='x',expand=True)
    ent2 = ttk.Entry(f1,width=100)
    ent2.pack(padx=10,fill='y',expand=True)

    nomor = ttk.Label(f1,text='Nomor Telepon : ')
    nomor.pack(padx=10,fill='x',expand=True)
    ent3 = ttk.Entry(f1,width=100)
    ent3.pack(padx=10,fill='y',expand=True)

    password = ttk.Label(f1,text='Password : ')
    password.pack(padx=10,fill='x',expand=True)
    ent4 = ttk.Entry(f1,width=100)
    ent4.pack(padx=10,fill='y',expand=True)

    password2 = ttk.Label(f1,text='Confirm Password : ')
    password2.pack(padx=10,fill='x',expand=True)
    ent5 = ttk.Entry(f1,width=100)
    ent5.pack(padx=10,fill='y',expand=True)

    tombol = tk.Button(f1,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup)
    tombol.pack(padx=10,pady=3,ipadx=20,fill='y',expand=True)

#Halaman keempat
def halaman4():
    global frame4,page_check
    frame1.pack_forget()
    frame2.pack_forget()
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
                if row[1]==email and row[3]==password:
                    messagebox.showinfo('Sign in','Sucess')  
                    next=tk.Button(f2,text='Next',bg='#57a1f8',fg='white',border=0,command=halaman5)
                    next.pack(padx=10,pady=3,ipadx=50,ipady=5,fill='y',expand=True)
                    return
                else:
                    messagebox.showerror('Invalid','Invalid email or password')
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
    dropdown_poli = tk.OptionMenu(frame5, varpoli,'Poli Umum','Poli Jantung','Poli Kandungan')
    dropdown_poli.pack()
    
    #Dokter
    def display_jadwal():
        list = ttk.Treeview(frame5, columns=('Nomor','Dokter','Hari','Waktu'),show='headings')
        list.heading('Nomor',text='No.')
        list.heading('Dokter',text='Dokter')
        list.heading('Hari',text='Hari')
        list.heading('Waktu',text='Jam Praktik')
        list.column("Nomor", width=50)
        list.column("Dokter", width=150)
        list.column("Hari", width=80)
        list.column("Waktu", width=100)
        poli = varpoli.get()
        with open('nyobadata.csv','r')as file:
            csv_reader = csv.reader(file)
            if poli == 'Poli Umum':
                for row in csv_reader:
                    if row[0]== 'umum':
                        list.insert('','end',values=row)
        list.pack(expand=True,anchor='center')
    button_tampilkan = tk.Button(frame5,text='Lihat Jadwal',command=display_jadwal)
    button_tampilkan.pack(expand=True,ipadx=10,pady=1)    
if __name__=='__main__':
    halaman1()
main.mainloop()