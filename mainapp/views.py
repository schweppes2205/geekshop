import datetime
import json
from django.shortcuts import render


def main(request):
    title = "главная"
    # products = [
    #     {
    #         "name": "Отличный стул",
    #         "desc": "Расположитесь комфортно.",
    #         "image_src": "product-1.jpg",
    #         "image_href": "/product/1/",
    #         "alt": "продукт 1",
    #     },
    #     {
    #         "name": "Стул повышенного качества",
    #         "desc": "Не оторваться.",
    #         "image_src": "product-2.jpg",
    #         "image_href": "/product/2/",
    #         "alt": "продукт 2",
    #     },
    # ]
    with open("static/dbInFile/products.json",encoding="utf-8") as file_descriptor:
        products_raw_data = file_descriptor.read()
    products = json.loads(products_raw_data)
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    with open("static/dbInFile/links_menu.json",encoding="utf-8") as file_descriptor:
        links_menu_raw_data = file_descriptor.read()
    links_menu = json.loads(links_menu_raw_data)
    # links_menu = [
    #     {"href": "products_all", "name": "все"},
    #     {"href": "products_home", "name": "дом"},
    #     {"href": "products_office", "name": "офис"},
    #     {"href": "products_modern", "name": "модерн"},
    #     {"href": "products_classic", "name": "классика"},
    # ]
    with open("static/dbInFile/same_products.json",encoding="utf-8") as file_descriptor:
        same_products_raw_data = file_descriptor.read()
    same_products = json.loads(same_products_raw_data)
    # same_products = [
    #     {"name": "Отличный стул", "desc": "Не оторваться.", "image_src": "product-11.jpg", "alt": "продукт 11"},
    #     {"name": "Стул повышенного качества", "desc": "Комфортно.", "image_src": "product-21.jpg", "alt": "продукт 21"},
    #     {
    #         "name": "Стул премиального качества",
    #         "desc": "Просто попробуйте.",
    #         "image_src": "product-31.jpg",
    #         "alt": "продукт 31",
    #     },
    # ]
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    with open("static/dbInFile/locations.json",encoding="utf-8") as file_descriptor:
        locations_raw_data = file_descriptor.read()
    locations = json.loads(locations_raw_data)
    # locations = [
    #     {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
    #     {
    #         "city": "Екатеринбург",
    #         "phone": "+7-777-777-7777",
    #         "email": "info_yekaterinburg@geekshop.ru",
    #         "address": "Близко к центру",
    #     },
    #     {
    #         "city": "Владивосток",
    #         "phone": "+7-999-999-9999",
    #         "email": "info_vladivostok@geekshop.ru",
    #         "address": "Близко к океану",
    #     },
    # ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)