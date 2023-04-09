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
        uname = request.POST['uname']
        passw = request.POST['pass'] #hi
        con = psycopg2.connect()
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
                messages.success(request, 'Бүртгэлтэй хэрэглэгч олдсонгүй ! ! !')
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

def forget(request):
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890/$?!', k=4))
    str = random_string
    hasho = hashlib.sha256()
    hasho.update(str.encode('utf8'))
    hex = hasho.hexdigest()
    if request.method == 'POST':
        gmail = request.POST['gmail']
        con = psycopg2.connect(
            host='202.131.254.138', 
            port='5938',
            database='qrEticket',
            user='qreasyTicket',
            password='eba7khulan4'
            )
        cur = con.cursor()
        cur.execute('SELECT count(mail) FROM "user" WHERE mail = %s',[gmail])
        xp = cur.fetchone()
        xp = list(xp)
        print(xp[0])
        if xp[0] == 1:
            subject = 'Нууц үг сэргээх'
            message = 'таны шинэ нууц үг бол '+ hex
            sender_email = 'eticket123@gmail.com'
            receiver_email = request.POST.get('gmail')
            send_mail(
                subject,
                message,
                sender_email,
                [receiver_email],
                fail_silently=False,
            )
            return redirect('forget2'),HttpResponse({'gmail': gmail})
        else:
            messages.error(request, 'Бүртгэлтэй хаяг олдсонгүй ! ! !')
    return render(request,'forget.html')

def forget2(request):
    if request.method == 'POST':
            npass = request.POST['npass']
            rpass = request.POST['rpass']
            gmail = request.GET.get('gmail')
            if npass != rpass:
                messages.error(request, 'Давталт буруу байна. ! ! !')
            con = psycopg2.connect(
                host='202.131.254.138', 
                port='5938',
                database='qrEticket',
                user='qreasyTicket',
                password='eba7khulan4'
                )
            cur = con.cursor()
            cur.execute('UPDATE "user" SET password = %s WHERE mail = %s',[npass,gmail])
            con.commit()
            return redirect('login')
    return render(request,'forget2.html')

def ticket(request):
    if request.method == 'POST':
        loc = request.POST['loc']
        where = request.POST['where']
        type = request.POST['type']
        sex = request.POST['sex']
        ogno = request.POST['ogno']
        num = request.POST['num']
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
        cur.execute('INSERT INTO "ticket" (ID,location,where,ttype,thuis,ogno,num) VALUES (%s,%s,%s,%s,%s,%s,%s)',[uid,loc,where,type,sex,ogno,num])
        con.commit()
        return redirect('dashboard')
    return render(request,'ticket.html')

def my_ticket(request):
    return render(request,'my_ticket.html')