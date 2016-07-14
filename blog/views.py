from django.shortcuts import render


def post_list(request):
    return render(request, "main/home.html")


def post_detail(request):
    return render(request, "post_detail")