from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>welcome to the project</h1>')
def hainame(request,name):
    return HttpResponse('<h1>Hello{}</h1>'.format(name))
def add(request,a,b):
    return HttpResponse('The sum of {} and {} is {}'.format(a,b,int(a)+int(b)))
def tempdemo(request):
    fruits=["Mango","Apple","Banana"]
    return render(request,'template1.html',context={'name':'harsh mangal','age':'20','fruits':fruits})
def tempo(request):
    return render(request,'template2.html')
def ind(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def myhome(request):
    return render(request,'home.html')
from django.core.files.storage import FileSystemStorage
def register(request):
    if request.method=="POST":
        email=request.POST.get('email')
       
        if request.FILES:
            file=request.FILES['profilepic']
            fs=FileSystemStorage()
            savedfile=fs.save(file.name,file)
            file_url=fs.url(savedfile)
        return HttpResponse("submitted succesfully !<br>{},<img src='{}'>".format(email,file_url))
    return render(request,'register.html')
