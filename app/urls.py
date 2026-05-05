from django.urls import path
from .views import (index, dashboard, register, user_login, user_logout, create_category, delete_category, update_record, 
                    create_expense, delete_expense, create_income, delete_income)

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/update/<slug:record_type>/<int:record_id>/', update_record, name='update_record'),

    path('sign-up/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

    path('income/create/', create_income, name='create_income'),
    path('income/delete/<int:income_id>/', delete_income, name='delete_income'),

    path('expense/create/', create_expense, name='create_expense'),
    path('expense/delete/<int:expense_id>/', delete_expense, name='delete_expense'),

    path('category/create/', create_category, name='create_category'),
    path('category/delete/<int:category_id>/', delete_category, name='delete_category'),
]