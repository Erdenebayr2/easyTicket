from django.shortcuts import render,redirect
from django.contrib import messages
import psycopg2
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    if request.method == 'POST':
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
    return render(request,'login.html')

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

def signup(request):
    if request.method == 'POST':
        # id = request.POST['id']
        username = request.POST['username']
        password = request.POST['password']
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
        cur.execute('INSERT INTO "user" (id,username, password) VALUES (%s,%s, %s)',[uid,username, password])
        con.commit()
        return redirect('login')
    return render(request, 'signup.html')

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