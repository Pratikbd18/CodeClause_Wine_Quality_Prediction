from django.shortcuts import render
from django.http import HttpResponse
import pickle

def home(request):
    return render(request,'index.html')

def result(request):
    result=0
    data={}
    if request.method=='POST':
        num1=eval(request.POST.get('num1'))
        num2=eval(request.POST.get('num2'))
        num3=eval(request.POST.get('num3'))
        num4=eval(request.POST.get('num4'))
        num5=eval(request.POST.get('num5'))
        num6=eval(request.POST.get('num6'))
        num7=eval(request.POST.get('num7'))
        num8=eval(request.POST.get('num8'))
        num9=eval(request.POST.get('num9'))
        num10=eval(request.POST.get('num10'))

        saved_model=pickle.load(open('model.sav','rb'))

        result=saved_model.predict([[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]])
        print(result)
        data={
            'result':result[0]
        }
        

    return render(request,'result.html',data)