from django.shortcuts import render,redirect
from django.contrib import messages
import psycopg2
from django.http import HttpResponse
import random ,hashlib
from django.core.mail import send_mail

def dashboard(request):
    return render(request, 'dashboard.html')
def login(request):
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890/$?!', k=4))
    str = random_string
    hasho = hashlib.sha256()
    hasho.update(str.encode('utf8'))
    hex = hasho.hexdigest()
    if request.method == 'POST':
        if request.POST['user'] and request.POST['mail']:
            subject = 'Бүртгэл баталгаажлаа'
            message = 'таны нууц үг бол '+ hex
            sender_email = 'eticket123@gmail.com'
            receiver_email = request.POST.get('mail')
            send_mail(
                subject,
                message,
                sender_email,
                [receiver_email],
                fail_silently=False,
            )
            username = request.POST['user']
            password = hex
            email = request.POST['mail']
            nickname = request.POST['nick']
            con = psycopg2.connect(
            host='202.131.254.138', 
            port='5938',
            database='qrEticket',
            user='qreasyTicket',
            password='eba7khulan4'
            )
            cur = con.cursor()
            cur.execute("SELECT nextval('mid')")
            uid = cur.fetchone()[0]
            cur.execute('INSERT INTO "user" (id,username, password,mail,nickname) VALUES (%s,%s, %s,%s,%s)',[uid,username, password,email,nickname])
            con.commit()
            return redirect('login')
        elif request.POST['uname']:
            uname = request.POST['uname']
            passw = request.POST['pass']
            con = psycopg2.connect(
            host='202.131.254.138', 
            port='5938',
            database='qrEticket',
            user='qreasyTicket',
            password='eba7khulan4'
            )
            cur = con.cursor()
            cur.execute('SELECT count(username) FROM "user" WHERE username = %s AND password = %s',[uname, passw])
            xp = cur.fetchone()
            xp = list(xp)
            print(xp[0])
            if xp[0] == 1:
                return redirect('dashboard')
            else:
                messages.success(request, 'Бүртгэлтэй хэрэглэгч олдсонгүй.')
                return redirect('login')
    return render(request,'index.html')

       

def user(request):
    if request.method == 'GET':
        con = psycopg2.connect(
            host='202.131.254.138', 
            port='5938',
            database='qrEticket',
            user='qreasyTicket',
            password='eba7khulan4'
            )
        cur = con.cursor()
        cur.execute('SELECT * FROM "user" ORDER BY ID ASC')
        colum = [d[0] for d in cur.description]
        users = [dict(zip(colum,users)) for users in cur.fetchall()]
        con.close()
        return render(request,'user.html', context={'users':users})

def teller(request):
    if request.method == 'GET':
        con = psycopg2.connect(
            host='202.131.254.138', 
            port='5938',
            database='qrEticket',
            user='qreasyTicket',
            password='eba7khulan4'
            )
        cur = con.cursor()
        cur.execute('SELECT * FROM "user" ORDER BY ID ASC')
        colum = [d[0] for d in cur.description]
        users = [dict(zip(colum,users)) for users in cur.fetchall()]
        # con.commit()
        con.close()
        print(users)
        return render(request,'admin.html', context={'users':users})
    
def contact(request):
    return render(request,'contact.html')