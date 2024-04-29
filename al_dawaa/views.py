from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from services.models import service
from news.models import News
from about.models import About
from contact.models import Contact
from doctors.models import Doctors
from django.core.paginator import Paginator
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
                aboutData=About.objects.all()
                doctorsData=Doctors.objects.all()

                data={
                    'title':'Al-Dawaa',
                    'aboutData':aboutData,
                    'doctorsData':doctorsData,
                  
                }
                return render(request, "about.html",data) 

# def doctors(request):
#                 doctorsData=About.objects.all()

#                 data={
#                     'title':'Al-Dawaa',
#                     'doctorsData':doctorsData
                  
#                 }
#                 return render(request, "about.html",data)
def contactNum(request,ph):                
                    return HttpResponse(ph)
                    

def contact(request):
                    data={
                        'title':'Al-Dawaa',
                    }
                    return render(request,"contact.html",data)
def contactSave(request):
                 
                if request.method == "POST":
                                     contact_name=request.POST.get('contact_name');
                                     contact_email=request.POST.get('contact_email');
                                     contact_message=request.POST.get('contact_message');
                                     saveContact=Contact(contact_name=contact_name,contact_email=contact_email,contact_message=contact_message)
                                     saveContact.save() 
                                    

                return render(request,"contact.html")

def services(request):
                    serviceData=service.objects.all()
                    paginator=Paginator(serviceData,3)
                    page_number = request.GET.get('page')
                    serviceDataFinal = paginator.get_page(page_number)
                    totalPages=serviceDataFinal.paginator.num_pages


                    if request.method == "GET":
                        st=request.GET.get('servicename')
                        if st != None:
                            serviceData=service.objects.filter(service_title__icontains=st)

                    
                    data={
                        'title':'Al-Dawaa',
                        'serviceData':serviceDataFinal,
                        'lastpage':totalPages,
                        'totalpageList':[n+1 for n in range(totalPages)],
                    }
                    return render(request,"services.html",data)
def news(request):
                    newsData=News.objects.all()

                    data={
                        'title':'Al-Dawaa',
                        'newsData':newsData,
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
def onlineOppointment(request):

                data={
                    'title':'Al-Dawaa',
                  
                }
                return render(request, "onlineOppointment.html") 