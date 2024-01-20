from django.shortcuts import render

# Create your views here.


def getAllProduct():
  products = Product.objects.all()