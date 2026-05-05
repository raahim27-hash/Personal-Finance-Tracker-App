from django.contrib import admin
from .models import Category, Income, Expense   


# Register your models here.
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
    "user", "amount", "source", "category", "description", "date_received", 
    "created_at", "updated_at",
    )

    search_fields = ("user", "amount", "category")

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
    "user", "amount", "category", "date_incurred", "description", "receipt_image",
    "created_at", "updated_at",
    )

    search_fields = ("user", "amount", "category", "description", "date_incurred")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
    "name", "type",
    )
    
    search_fields = ("name", "type")
