from django.shortcuts import render

from shop.models import Category, Group, Product


def index(request):
    # queryset = (
    #     Category.objects
    #     # .prefetch_related("group")
    #     .all()
    # )
    queryset_group = (
        Group.objects
        .prefetch_related("category")
        .order_by("category")
    )

    category_dict = dict()
    for qr in queryset_group:
        category_dict.setdefault(qr.category, [])
        group_list = category_dict[qr.category]
        group_list.append(qr.name)
        category_dict[qr.category] = group_list

    # queryset_top_products = []

    queryset_top_products = (
        Product.objects
        .filter(archived=False)
        .order_by("rating")[10:]
        # .prefetch_related("group")
        # .all()
    )

    print(queryset_top_products)


    data = {"category_dict": category_dict, "message": "Welcome to Python", "top_products": queryset_top_products}
    return render(request, "index.html", context=data)
    # return render(request, "index.html", context=data)
