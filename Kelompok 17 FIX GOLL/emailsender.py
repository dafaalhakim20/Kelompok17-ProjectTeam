import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import csv


def kirim_nomor_antrian(nomor_antrian,emailuser):
    with open('simpandata.csv','r')as file:
            csv_reader = csv.reader(file)
            last_row = list(csv_reader)[-1]
    isi_email = '''
==========================================================

    TERIMA KASIH TELAH MELAKUKAN PENDAFTARAN DI RS UNS
        BERIKUT MERUPAKAN NOMOR ANTREAN ANDA
                    {Nomor}
        BERIKUT MERUPAKAN DETAIL POLI PILIHAN ANDA
        {Detail}

==========================================================
        '''.format(Nomor = nomor_antrian, Detail = last_row )
    ngirim_email(isi_email,emailuser, jenis = 2)

def ngirim_email(body_email,email_user,jenis):
    # Konfigurasi
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'rsunsjaya@gmail.com' #Email Pengirim
    SMTP_PASSWORD = 'angmezfmjrpcavnq' #Password SMTP EMAIL
    SENDER_EMAIL = 'rsunsjaya@gmail.com' # Email Pengirim

    # Membuat pesan email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email_user
    msg['Subject'] = 'RS UNS'

    if jenis == 1:
        body = '''
==========================================================

    TERIMA KASIH TELAH MELAKUKAN PENDAFTARAN DI RS UNS
        BERIKUT MERUPAKAN NOMOR ANTREAN ANDA
                    {}

     JANGAN BERIKAN KODE INI PADA ORANG LAIN!

==========================================================
        '''.format(HASIL = body_email )
    elif jenis == 2:
        body = body_email

    msg.attach(MIMEText(body, 'plain'))
    simple_email_contatcs = ssl.create_default_context()
    try:
        print("\nConnecting to server ... ")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls(context=simple_email_contatcs)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, email_user, text)
        server.quit()
        print('Kode terkirim di email. Silahkan periksa email anda')
    except Exception as e:
        print('Email gagal dikirim:', str(e))
