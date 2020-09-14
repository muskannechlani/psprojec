from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os 
import subprocess
# Create your views here.
def print(request):
   
      process = subprocess.Popen('ls', 
      shell=True, 
      stdout=subprocess.PIPE, 
      stderr=subprocess.PIPE )
      # print(process.stdout)
      return HttpResponse((process.stdout))
    
def showhtml(request):
   
      return render(request,'todo.html')