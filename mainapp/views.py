import datetime
import json
from django.shortcuts import render

from .models import Product, ProductCategory

def main(request):
    title = "главная"
    products = Product.objects.all()
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    with open("static/dbInFile/locations.json",encoding="utf-8") as file_descriptor:
        locations_raw_data = file_descriptor.read()
    locations = json.loads(locations_raw_data)
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)