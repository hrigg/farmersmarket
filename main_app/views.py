from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name= 'home.html'

class About(TemplateView):
    template_name= 'about.html'

class Market: 
    def __init__(self, place, date):
        self.date=date
        self.place=place

markets=[Market('Arlington', 'Saturdays'),
Market('Ballston', 'Saturdays')]

class MarketList(TemplateView):
    template_name= 'market_list.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['markets']=markets
        return context