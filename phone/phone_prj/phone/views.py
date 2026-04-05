from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

class IndexView(ListView):
    queryset = Contact.objects.all().order_by('name')
    template_name = 'phone/result.html'
    context_object_name = 'results'

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword', '')
        
        if keyword:
            return queryset.filter(name__contains=keyword)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.request.GET.get('keyword', '')
        return context