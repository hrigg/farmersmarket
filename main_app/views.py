from re import template
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Market, Vendor, Product
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required



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

class VendorList(TemplateView):
    template_name= 'vendor_list.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        name=self.request.GET.get('name')
        if name != None:
            context['vendors']= Vendor.objects.filter(name__icontains=name)
        else: 
            context['vendors']=Vendor.objects.all()
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

class ProductDetail(DetailView):
    model=Product
    template_name= 'product_detail.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['vendor']= Vendor.objects.all()
        return context

@method_decorator(staff_member_required, name='dispatch')
class MarketCreate(CreateView):
    model= Market
    fields=['name', 'day','times','season', 'location','image','state','county']
    template_name='market_create.html'
    def get_success_url(self):
        return reverse('market_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ProductCreate(View):
     def post(self, request, pk):
        name=request.POST.get('name')
        image=request.POST.get('image')
        description=request.POST.get('description')
        price=request.POST.get('price')
        vendor=Vendor.objects.get(pk=pk)
        Product.objects.create(name=name, image=image, description=description, vendor=vendor, price=price)
        return redirect('vendor_detail', pk=pk)

class AddNew(TemplateView):
    template_name = "addnew.html"

@method_decorator(login_required, name='dispatch')
class MarketUpdate(UpdateView):
    model = Market
    fields = ['name', 'day', 'times', 'season', 'location', 'image', 'state', 'county']
    template_name = "market_update.html"
    def get_success_url(self):
        return reverse('market_detail', kwargs={'pk': self.object.pk})


@method_decorator(staff_member_required, name='dispatch')
# @user_passes_test(lambda u: u.groups.filter(name='Vendor').exists()
class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['name', 'website', 'description', 'image']
    template_name = "vendor_update.html"
    def get_success_url(self):
        return reverse('vendor_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class MarketDelete(DeleteView):
    model = Market
    template_name = "market_delete_confirmation.html"
    success_url = "/markets/"

@method_decorator(staff_member_required, name='dispatch')
class VendorCreate(CreateView):
    model= Vendor
    fields=['name', 'description','image','website']
    template_name='vendor_create.html'
    success_url='/markets/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VendorCreate, self).form_valid(form)


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


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/markets/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
