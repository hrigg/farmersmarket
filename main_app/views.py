from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Market, Vendor
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class Home(TemplateView):
    template_name= 'home.html'

class About(TemplateView):
    template_name= 'about.html'

class MarketList(TemplateView):
    template_name= 'market_list.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        name=self.request.GET.get('name')
        if name != None:
            context['markets']= Market.objects.filter(name__icontains=name)
        else: 
            context['markets']=Market.objects.all()
        return context

class MarketDetail(DetailView):
    model=Market
    template_name= 'market_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['vendors']= Vendor.objects.all()
        return context

class VendorDetail(DetailView):
    model=Vendor
    template_name= 'vendor_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['markets']= Market.objects.all()
        return context

class MarketCreate(CreateView):
    model= Market
    fields=['name', 'day','times','season', 'location','image','state','county']
    template_name='market_create.html'
    def get_success_url(self):
        return reverse('market_detail', kwargs={'pk': self.object.pk})

class MarketUpdate(UpdateView):
    model = Market
    fields = ['name', 'day', 'times', 'season', 'location', 'image', 'state', 'county']
    template_name = "market_update.html"
    def get_success_url(self):
        return reverse('market_detail', kwargs={'pk': self.object.pk})

class MarketDelete(DeleteView):
    model = Market
    template_name = "market_delete_confirmation.html"
    success_url = "/markets/"

class VendorCreate(CreateView, View):
    model= Vendor
    fields=['name', 'description','image','website']
    template_name='vendor_create.html'
    success_url='/vendors/'
    def _get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['markets']=Market.objects.all()
        return context

class MarketVendorAssoc(View):

    def get(self, request, pk, vendor_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playMarket by the id and
            # remove from the join table the given vendor_id
            Market.objects.get(pk=pk).vendors.remove(vendor_pk)
        if assoc == "add":
            # get the playMarket by the id and
            # add to the join table the given vendor_id
            Market.objects.get(pk=pk).vendors.add(vendor_pk)
        return redirect('/')