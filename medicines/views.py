from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Medicine, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



class MedicineListView(ListView):
    model = Medicine
    template_name = 'list.html'


class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Medicine
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Medicine.objects.filter(
		Q(title__icontains=query)
		)

class MedicineCheckoutView(LoginRequiredMixin, DetailView):
    model = Medicine
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Medicine.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

