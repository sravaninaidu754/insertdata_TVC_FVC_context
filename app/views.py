from django.shortcuts import render
from django.views.generic import *
from app.forms import * 
from app.models import *
from django.http import HttpResponse
# Create your views here.
class TempDataRender(TemplateView):
    template_name='TempDataRender.html'
    def get_context_data(self,**kwargs):
       context=super().get_context_data(**kwargs)
       context['name']='SRAVANI MUKKAM'
       return context


class inserttemplateviewdata(TemplateView):
    template_name='inserttemplateviewdata.html'
    def get_context_data(self,**kwargs): 
        ECDO=super().get_context_data(**kwargs)
        SFO=studentform()
        ECDO['SFO']=SFO 
        return ECDO 
    def post(self,request):
        SFD=studentform(request.POST) 
        if SFD.is_valid():
            SFD.save() 
            return HttpResponse('data inserted')


class insertformviewdata(FormView):
    template_name='insertformviewdata.html'
    form_class=studentform
    def form_valid(self,form):
        form.save()
        return HttpResponse('Data inserted') 



