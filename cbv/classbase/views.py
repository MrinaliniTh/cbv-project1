from django.shortcuts import render
from classbase.models import School,Student
from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class Index(TemplateView):
    template_name='index.html'

class SchoolView(ListView):
    model=School
    template_name='classbase/school.html'

class StudentView(DetailView):
    #context_object_name='school'
    model=School
    template_name='classbase/student.html'    

class SchoolCreateView(CreateView):
     fields=('name','principal','location')
     model=School   
     #template_name='classbase/school_form.html'

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=School

class SchoolDeleteView(DeleteView):
    model=School
    success_url=reverse_lazy('classbase:SchoolView')         