from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.mail import send_mail
from django.conf import settings
# from .filters import StudentFilter
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'hostelapp/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inform')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'hostelapp/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def dashboardPage(request):
    students = Student.objects.order_by('room')
    # if req.method == "POST" and req.FILES:
    #     # print(req.FILES)
    #     noticefile = req.FILES['Notice']
    #     fs = FileSystemStorage()
    #     furl = fs.save(noticefile.name, noticefile)
    #     print("Data Inserted")
    #     return redirect("/inform")
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(student_name__icontains=query) | Q(enrollment_no__icontains=query) | Q(student_mail__icontains=query) | Q(student_contact__icontains=query) | Q(room__icontains=query) | Q(dob__icontains=query) | Q(student_address__icontains=query) | Q(course__icontains=query) | Q(curr_year__icontains=query))
    else:
        students = Student.objects.order_by('room')
    # myFilter = StudentFilter()
    context={
        'students':students, 
    }
    return render(request,'hostelapp/dashboard.html',context)

@login_required(login_url='login')
def roomPage(request):
    room = Room.objects.all()
    total_room = room.count()
    # btech_room = room.filter(course='Btech').count()
    # mca_room = room.filter(course='MCA').count()
    context={
        'room':room, 'total_room':total_room, 
    }
    return render(request,'hostelapp/rooms.html', context)

def home(request):
    return render(request,'hostelapp/main.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['students'])
def userPage(request):
	context = {}
	return render(request, 'hostelapp/user.html', context)

@login_required(login_url='login')
def infoPage(request):
    data = Notice.objects.all()
    students = Student.objects.all()
    total_students = students.count()
    btech_students = students.filter(course='BTECH').count()
    mca_students = students.filter(course='MCA').count()
    mba_students = students.filter(course='MBA').count()
    mtech_students = students.filter(course='MTECH').count()
    context={
        'data':data,
        'students':students,
        'total_students':total_students,
        'btech_students':btech_students,
        'mca_students':mca_students,
        'mba_students':mba_students,
        'mtech_students':mtech_students, 
        # 'myFilter':myFilter,
    }
    return render(request, 'hostelapp/inform.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def allot(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allot')
    context ={'form':form}
    return render(request,'hostelapp/allotment_form.html',context)    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateStudent(request, pk):

	student = Student.objects.get(id=pk)
	form = StudentForm(instance=student)

	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES, instance=student)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'hostelapp/allotment_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteStudent(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == "POST":
		student.delete()
		return redirect('dashboard')

	context = {'item':student}
	return render(request, 'hostelapp/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['students'])
def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            room_n = form.cleaned_data['room']
            mail = form.cleaned_data['student_mail']
            form.save()
            rooms = Room.objects.get(no=room_n)
            Room.Claimroom(rooms)
            subject = 'Send Mail Testing'
            message = 'Account made'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [mail]
            res = send_mail(subject, message, email_from, recipient_list)
            # messages.info(request, " new account added")        
    
    context = {'form':form}
    return render(request, 'hostelapp/account_settings.html', context)