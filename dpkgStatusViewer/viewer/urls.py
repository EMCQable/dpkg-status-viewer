from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files', views.files, name='files'),
    path('files/<str:file_id>', views.index_of_file, name='index_of_file'),
    path('files/<str:file_id>/', views.index_of_file, name='index_of_file'),
    path('files/<str:file_id>/<str:package_id>', views.packages, name='packages'),
]
