from django.shortcuts import render,redirect
from app1.models import Table1
# Create your views here.


def index(request):
    try:
     id1data = Table1.objects.get(id=1)
    except Table1.DoesNotExist:
      None
    return render(request,'app/index.html',locals())

def page1(request):
    return render(request,'app/page1.html',{})


def Addtext(request):
    abc = request.POST['text1'] # 從 html 來 
    try:
      Table1.objects.create(Text1 = abc,id=1)  
      #Table1.objects.filter(id=1).update(Text1 = abc) # 寫進資料庫
    except: 
        #None
        Table1.objects.filter(id=1).update(Text1 = abc) # 寫進資料庫
     # Table1.objects.create(Text1 = abc,id=1)
    return redirect('app/index.html')
'''
    result = Table1.objects.filter(id=1)
    if not result:
      result = Table1.objects.create(Text1=abc,id=1)
      return result
    
    Table1.objects.filter(id=1).update(Text1 = abc) # 寫進資料庫
    # Text2 = request.POST['text1']
    return redirect('app/index.html')
'''