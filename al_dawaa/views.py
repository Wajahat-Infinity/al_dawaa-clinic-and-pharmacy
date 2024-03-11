from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from services.models import service
def homePage(request):
                data={
                    'title':'Al-Dawaa',
                    'overview':'Our mission is to diagnose of disease and its treatment like other hospitals along these, our HOSPITAL gives free treatment and medicine for needy and helpless people.We also keep medical-camps along with our team and well qualified doctors and experts in differnt hard and remote areas ,where normally basic medical facilities are not available. We feel pleasure by doing our work',
                    'deptList':[{'name':'General Physician' , 'icon':'bi bi-capsule'},
                                {'name':'Ophthalmologist' , 'icon':'bi bi-eye'},
                                {'name':'Cardiologist' , 'icon':'bi bi-heart-pulse-fill'},
                                {'name':'Online appointment' , 'icon':'bi bi-calendar2-plus-fill'},],
                }
                return render(request,"index.html",data)
def aboutUs(request):
                data={
                    'title':'Al-Dawaa',
                    'overview':'Our mission is to diagnose of disease and its treatment like other hospitals along these, our HOSPITAL gives free treatment and medicine for needy and helpless people.We also keep medical-camps along with our team and well qualified doctors and experts in differnt hard and remote areas ,where normally basic medical facilities are not available. We feel pleasure by doing our work',
                    'deptList':[{'name':'General Physician' , 'icon':'bi bi-capsule'},
                                {'name':'Ophthalmologist' , 'icon':'bi bi-eye'},
                                {'name':'Cardiologist' , 'icon':'bi bi-heart-pulse-fill'},
                                {'name':'Online appointment' , 'icon':'bi bi-calendar2-plus-fill'},],
                }
                return render(request, "about.html",data) 
def contact(request):
                return HttpResponse("<b>contact page</b>")

def contactNum(request,ph):                
                    return HttpResponse(ph)
                    

def contact(request):
                    data={
                        'title':'Al-Dawaa',
                    }
                    return render(request,"contact.html",data)
def services(request):
                    serviceData=service.objects.all()[:6]
                    
                    data={
                        'title':'Al-Dawaa',
                        'serviceData':serviceData,

                    }
                    return render(request,"services.html",data)
def news(request):
                    data={
                        'title':'Al-Dawaa',
                    }
                    return render(request,"news.html",data)
def freeTreatment(request):
                    
                    data={},
                    try:
                            if(request.method == "POST"):
                                     name=request.POST.get('name');
                                     email=request.POST.get('email');
                                     if name == "":
                                                    return render(request,"freetreatment.html",{'error' : True})
                                     else:    
                                                    url="subFreeTreatmentform/?name={}".format(name)

                            return HttpResponseRedirect(url)  
                            data={
                                                'title':'Al-Dawaa',
                                                'name':name,
                                                'email':email

                                    } 
                            
                                               
                    except:
                                    pass

                   
                    return render(request,"freetreatment.html")


def subFreeTreatmentform(request):
                   
                    if request.method == 'GET':
                        name=request.GET.get('name')
                    data={
                        'title':'Al-Dawaa',
                        'name':name,
                    }
                    return render(request,"subFreeTreatmentform.html",data)