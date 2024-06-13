from django.contrib import admin
from .models import Medicine, Order



@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
	list_display=['title', 'description', 'price', 'image', 'medicine_available']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display=['product', 'created']