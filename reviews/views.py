from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CommentForm

class CommentCreateView(CreateView):
    form_class = CommentForm
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
            
    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url(), status=400)