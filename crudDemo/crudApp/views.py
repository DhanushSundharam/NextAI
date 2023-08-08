from django.shortcuts import render
from crudApp.models import Student

def retrieve_view(request):
    student=Student.objects.all()
    result={'student':student}
    return render(request,'crudApp/index.html',context=result)
    
