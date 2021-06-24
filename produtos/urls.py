from django.urls import path
from .views import list_produtos, create_produtos, update_produtos, delete_produtos

urlpatterns = [
    path('', list_produtos, name= 'list_products'),
    path('new', create_produtos, name= 'create_produtos'),
    path('update/<int:id>/', update_produtos, name= 'update_produtos'),
    path('delete/<int:id>/', delete_produtos, name= 'delete_produtos'),

]