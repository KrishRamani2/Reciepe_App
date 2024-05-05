from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':'Krish',"age":'18'},
        {'name':'Alex',"age":'22'},
        {'name':'Alexa',"age":'25'},
    ]
    for people in peoples:
     print(people)

    text="""Ok""" 
    return render(request,'index.html',context={'peoples':peoples,'text':text})

def about(request):
   return render(request,"about.jsx")

def contact(request):
    return render(request,"contact.jsx")


def success(request):
    
    return HttpResponse("""<h1>hey You are Successfull...
       <p>Hello<p>
<hr/>""")
    