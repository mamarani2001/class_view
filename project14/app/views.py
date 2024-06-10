from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from .forms import *
# Create your views here.


def fbv_string(request):
    return HttpResponse('Hello Welcome to the project')


class cbv_string(View):
    def get(self, request):
        return HttpResponse('Hello theis is Home Page')
    

def insert_school_fbv(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == "POST":
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school is done')
        return HttpResponse('invalid data')
    return render(request, 'insert_school_fbv.html', d)


class insert_school_cbv(View):
    def get(self, request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request, 'insert_school_fbv.html', d)


    def post(self, request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school is done')
        return HttpResponse('invalid data')
    

class template_view(TemplateView):
    template_name='template_view.html'
