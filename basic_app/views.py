from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( View,TemplateView, ListView, DetailView,
                                 CreateView,UpdateView,DeleteView)
from basic_app import models

class IndexView(TemplateView):
    template_name = 'index.html'
"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

""" 
class SchoolListView(ListView): # ListView actuall by default returns the model lowercase_list 
    context_object_name = 'schools' #But You can define your own context object Name 
    model = models.School # What it does , it takes the model I called . Lower cases everything . And then add _list
    #paginate_by = 10  # Also have to work in template for this 

    #school_list 

class SchoolDetailView(DetailView):  # DetailView actually by default returns the model lower case 
    context_object_name = 'school_detail' # But You can define your own context object Name
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal') #In which fields I'm gonna update
    model = models.School    # Connection to the model


class SchoolDeleteView(DeleteView):   
    model = models.School # DeletelView actually by default returns the model lowercase 
    success_url = reverse_lazy("basic_app:list")

    # This success_url means is once successfully deleted a school I want you to go back to the list page 
    # of the basic_app and show all the schools .
    # The reason we use reverse_lazy is that we don't want it to evaluated completely by running py file
    # we only wanted it to wait until it actually called as success .