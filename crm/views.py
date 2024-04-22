from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from . models import Record
# Create your views here.

@login_required(login_url='login')
def index(request):

    return render(request,'pages/index.html')

@login_required(login_url='login')
def dashboard(request):
    my_record = Record.objects.all()
    context ={'records':my_record}
    return render(request,'pages/dashboard.html',context=context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={'form': form}
    return render(request,'pages/register.html', context)



class login(LoginView):
   form_class = LoginForm
   template_name = 'pages/login.html'
    
   def form_valid(self, form):
        super().form_valid(form)
        return redirect('dashboard')

def logout(request):
    django_logout(request)
    return redirect('index')



#create record

@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
        
    context = {'form': form}

    return render(request, 'pages/create-record.html',context)



#update record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateRecordForm(instance=record)
        
    context = {'form': form}
    return render(request, 'pages/update-record.html', context)  


#delete record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    return redirect('dashboard')