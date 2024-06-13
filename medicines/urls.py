
from django.urls import path
from .views import MedicineListView, MedicineDetailView, MedicineCheckoutView, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', MedicineListView.as_view(), name = 'list'),
    path('<int:pk>/', MedicineDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', MedicineCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]