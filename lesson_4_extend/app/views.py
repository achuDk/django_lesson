from django.shortcuts import render

# Create your views here.


def backend(request):

    return render(request,'index.html')

def student(request):
    student = ['alex','tom','jerry','obama']
    return render(request,'student.html',locals())