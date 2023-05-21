from django.shortcuts import render
from library.models import customer

# Create your views here.

def register(request):
    return render(request, 'library/register.html', {})

def adduser(request):
    first_name = request.POST['firt_name']
    last_name = request.POST['last_name']
    email_id = request.POST['email_id']
    user_name = request.POST['user_name']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if(password==re_password):
        cus = customer(first_name='first_name', last_name='last_name', email_id='email_id', user_name='user_name', password='password', re_password='re_password')
        cus.save()
        return render(request, 'library/login.html', {})
    else:
        message = "Passwords do not match."

def login(request):
    return render(request, 'library/login.html', {})

def checkuser(request):
    try:
        n1 = request.POST['user_name']
        n2 = request.POST['password']
        cus = customer.objects.get(user_name=n1, password=n2)
        request.session['id'] = cus.id
        request.session['name'] = cus.user_name
        print("CHECK 2 DONE!")
        return userhomepage(request)

    except Exception as e:
        print(e)
        return render(request, 'library/login.html', {'error': 'Invalid username/password'})

def userhomepage(request):
    return render(request, 'library/userhomepage.html')


