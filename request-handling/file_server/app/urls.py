from django.urls import path, register_converter
from app.views import file_list, file_content
from app.converter import DataConverter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(DataConverter, 'dtc')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dtc:date>/', file_list, name='file_list'),
    path('file/<str:name>', file_content, name='file_content')
]
