from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from pytube import YouTube
import os
import random


folder_path = "E:\\DJANGO_PYTHON\\JNCT\\static\\student_profile"
try:
    os.makedirs(folder_path)
except OSError as e:
    print("Already Exist!")

hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
year = int(datetime.datetime.now().year)


if hour >= 0 and hour < 12:
    wish="Good Morning! "

elif hour >= 12 and hour < 18:
    wish="Good Afternoon!"
else:
    wish="Good Evening!"


def login(request):
    issue = request.GET.get('issue', 'default')
    email = request.GET.get('email', 'default')
    return render(request,'admin.html')


def index(request):
    return render(request,'index.html')


def owner(request):
    name = request.POST.get('name','default')
    email = request.POST.get('email','default')
    phone = request.POST.get('phone','default')
    address = request.POST.get('address','Not mentioned')
    form_group = request.POST.get('course','default')


    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'
    to_email = "sauravpathak24072003@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = f"Admission {name}"

    body = f"Name: {name} choose for {form_group}\n\nContact info:\nPhone Number:{phone}\nEmail-Id:{email}\n\nAddress:\n{address}\n\nsubmission time:{hour}:{minute}\nsubmission date:{day}/{month}/{year}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {str(e)}")
def coaching(request):
    global name,email,address,phone,form_group,rollnumber
    name = request.POST.get('name','default')
    email = request.POST.get('email','default')
    phone = request.POST.get('phone','default')
    address = request.POST.get('address','you do not mention your Address')
    form_group = request.POST.get('course','default')
    params = {'purpose': 'capital text', 'analyzed_text': f'Hello {name}', 'wish':f"{wish}"}
 #create roll number
    pass_start = 306
    pass_end = 200
    pass_end_2 = 900
    password_rand = random.randint(pass_end, pass_end_2)
    pass_rand = random.randint(pass_start, password_rand)
    rollnumber=f"0{pass_start}CS{pass_rand}{password_rand}"
    file_name = f'{phone}.csv'


            #Pandas
    try:
        df = pd.read_csv(f"E:\\DJANGO_PYTHON\\JNCT\\static\\student_profile\\{file_name}")
        check_phone = df[['phone']]
        print(check_phone)
        if check_phone == phone:
            return render(request, 'error.html')

    except:
        access = ['Row1']
        dff = pd.DataFrame()
        data = {'name': name, 'cource': form_group, 'address': address, 'phone': phone, 'email': email,'rollnumber':rollnumber}
        df = pd.DataFrame(data, index=access)
        dff = pd.concat([dff, df])
        df.to_csv(f'E:\\DJANGO_PYTHON\\JNCT\\static\\student_profile\\{file_name}', index=True)

    #GMAIL___AREA
    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'
    to_email = email
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = f"Submit {name}"
    body = f"Hello {name}\n.JNCT (JawaharLal Nehru College of Technolog) welcomes you..You choose for {form_group}\n.We recieved your request.\n\nYour Roll number is \n{rollnumber}.\n\nThank you for visiting our Website.We will contact you soon.\nContact info:\nPhone Number:{phone}\nEmail-Id:{email}\n\nsubmission time:{hour}:{minute}\nsubmission date:{day}/{month}{year}\nAddress:\n{address}\n\nYou can contact us given below number:\ncontact number:- 9752249543\nE-mail:- sauravpathak24072003@gmail.com"
    msg.attach(MIMEText(body, "plain"))
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to_email, msg.as_string())
    server.quit()
    owner(request)


    return render(request, 'confirm.html', params)

def notes(request):
    return render(request, 'notes.html')



def report(request):
    issue = request.GET.get('issue', 'default')
    email = request.GET.get('email', 'default')
    phone = request.GET.get('phone', 'default')

    params = {'purpose': 'Contact Us', 'analyzed_text': f'An{issue} has issued on {email}. Contact number:{phone}'}

    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'

    to_email = "sauravpathak24072003@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = " Report message JNCT"

    body = f"An issue has organised in {email}.\nISSUE:\n{issue}\n\nReport time:{hour}:{minute}\nReport date:{day}/{month}{year}\n\n\nDiscription:\nAn{issue} has issued on {email}. Contact number:{phone}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()


    except Exception as e:
        print(f"Error: {str(e)}")
        return render(request, 'error.html')


    return render(request, 'contact.html')

def contact(request):
    return render(request, 'contact.html')

def error(request):
    return render(request, 'error.html')
def download_link(request):
    link = request.GET.get('link','default')
    video_url = link
    try:
        download_path = "C:/"
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        return render(request, 'notes.html')
    except Exception as e:
        print(f"Error: {str(e)}")
        return render(request, 'error.html')

def student_login(request):
    return render(request, 'student_login.html')


def student_information(request):
    global name,roll_num,phone_,Address,email,cource
    phone = request.POST.get('phone', 'default')
    df = pd.read_csv(f"E:\\DJANGO_PYTHON\\JNCT\static\\student_profile\\{phone}.csv")


    name = df[['name']]
    # name_=len(name)
    # name__ =name[2:name_]
    #
    phone_ = df[['phone']]
    # phone__=len(phone_)
    # phone___ =phone_[2:phone__]
    #
    roll_num = df[['rollnumber']]
    # rollnumber=len(roll_num)
    # roll_num__ =roll_num[2:rollnumber]
    #
    email = df[['email']]
    # email_=len(email)
    # email__ =email[2:email_]
    #
    cource = df[['cource']]
    # cource_=len(cource)
    # cource__ =name[2:cource_]
    #
    Address = df[['address']]
    # address=len(Address)
    # Address__ =Address[2:address]


    param={'name':name,'roll':roll_num,'father':email,'Mother':'Mother','phone':phone_,'cource':cource,'Address':Address}
    return render(request, 'student_information.html',param)

def Apply_now(request):
    return render(request,"Apply_now.html")

def fee_cource(request):
    return render(request,"fee_cource.html")

def submit(request):
    name = request.GET.get('name', 'default')
    email = request.GET.get('email', 'default')
    phone = request.GET.get('phone', 'default')

    gmail_user = "sauravpathak24072003@gmail.com"
    gmail_password = 'icosvozenepunwpb'
    to_email = "sauravpathak24072003@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = "Submit to know more"

    body = f"Name: {name} want to knw more.\n\nContact info:\nPhone Number:{phone}\nEmail-Id:{email}\n\nsubmission time:{hour}:{minute}\nsubmission date:{day}/{month}/{year}"
    msg.attach(MIMEText(body, "plain"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {str(e)}")
    return render(request, 'index.html')


def pictures(request):
    return render(request,'gallery.html')
