from django.shortcuts import render,redirect
from hospitalapp.models import Member, appointment, Users

# Create your views here.
def index(request):
  if request.method=='POST':
    appoint = appointment(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'],
                          date=request.POST['date'], department=request.POST['department'],
                          doctor=request.POST['doctor'], message=request.POST['message'])
    appoint.save()
    return redirect('/')
  else:
    return render(request, 'index.html')


def inner(request):
  return render(request, 'inner-page.html')

def register(request):
  if request.method == 'POST':
    member = Member(username= request.POST['username'], email=request.POST['email'], password=request.POST['password'])
    member.save()
    return redirect('/')
  else:
    return render(request, 'register.html')

def login(request):
  return render(request, 'register.html')


def upload(request):
  return render(request, 'upload.html')

def appointmentdetails(request):
  myappoint = appointment.objects.all()

  return render(request, 'appointment-details.html',{'myappoint':myappoint})


def users(request):
  myusers = Users.objects.all()

  return render(request, 'user.html',{'myusers': myusers})
