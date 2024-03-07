from django.shortcuts import render , HttpResponse , redirect
from .models import Input

# Create your views here.

def home(request):
    
    AllInputs=Input.objects.all()
    # print(allPosts)
    # Where allPosts will be there in html file of blog/Bloghome.html it will be replace by allPosts
    params = {'AllInputs':AllInputs}
    return render(request,"enroll/home.html",params)


def Takeinput(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # params = {'name':name , 'email':email , 'password':password}
        context = Input(name = name , email = email , password = password)
        context.save()
        return redirect('home')
        
    
def DeleteData(request,id):
    if request.method == 'POST':
        delete_id = Input.objects.get(sno=id)
        delete_id.delete()
        return redirect('home')
    
def Update(request,id):
    if request.method == 'POST':
        Id_update = Input.objects.get(sno=id)
        context = {'Id_update':Id_update}
        return render(request,'enroll/Update.html',context)
    
def EditData(request,id):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # params = {'name':name , 'email':email , 'password':password}
        context = Input(name = name , email = email , password = password , sno = id)
        context.save()
        return redirect('home')