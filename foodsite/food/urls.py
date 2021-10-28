from . import views
from django.urls import path

app_name='food'
urlpatterns = [
     path('', views.IndexClassView.as_view(),name='index'),
     path('add/', views.CreateItem.as_view(),name='add'),
     path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
     path('update/<int:id>/',views.update_item,name='update'),
     path('delete/<int:id>/',views.delete_item,name='delete')
]