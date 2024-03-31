from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'app1/home.html')

from django.contrib.auth.decorators import login_required

@login_required
def java_exams_view(request):
    return render(request,'app1/javaexams.html')

@login_required
def python_exams_view(request):
    return render(request,'app1/pythonexams.html')

@login_required
def aptitude_exams_view(request):
    return render(request,'app1/aptitudeexams.html')

