from django.shortcuts import render

pics_last_prod = [
    {
        "article": "Shoes",
        "description": "sdfgsdgdfghdfgdfg",
        "pic": "images/product_01.jpg",
        "price": 25.75,
        "reviews": 24,
    },
    {"article": "Jacket", "description": "sdfsdfsdfss", "pic": "images/product_02.jpg", "price": 30.25, "reviews": 21},
    {
        "article": "Scarf",
        "description": "dsfsdasfasfsdfsadasd",
        "pic": "images/product_03.jpg",
        "price": 20.45,
        "reviews": 36,
    },
    {"article": "Toys", "description": "sdfgsdfsdfsdf", "pic": "images/product_04.jpg", "price": 15.25, "reviews": 48},
    {
        "article": "Pullover",
        "description": "dgfdsfgsddfsdfsdf",
        "pic": "images/product_05.jpg",
        "price": 12.50,
        "reviews": 16,
    },
    {
        "article": "Toy",
        "description": "dsfsdfsdfsdzfsdfsdfsfs",
        "pic": "images/product_06.jpg",
        "price": 22.50,
        "reviews": 32,
    },
]


def home(request):
    return render(request, "home.html", {"items": pics_last_prod, "page_tag": "home"})
