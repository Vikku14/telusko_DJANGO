from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request ,'home.html',{'name':'vivek'})

def add(request):
	val1 = request.POST['num1']	
	val2= request.POST['num2']
	result = int(val2) + int(val1)
	return render(request, 'result.html',{'res': result})