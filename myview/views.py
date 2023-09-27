from django.http import JsonResponse
from django.shortcuts import render

def get_status(request):
    return JsonResponse({"status": True})


def index(request):
    return render(request, 'index.html')