from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Dhina Rotua Mutiara',
    'student_ID': '2106702182'
}