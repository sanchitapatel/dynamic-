from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def home(request):
   # id=pk
   # return render(request,'home.html')

#def home(request,pk):
    #id=pk
    #return render(request,'home.html',{'key':id})
def combination(request,pk,id,pkid,idpk):
            data={
                  'data1':pk,
                  'data2':id,
                  'data3':pkid,
                  'data4':idpk,
   
                 }
            return render(request,'home.html',{'key':data})