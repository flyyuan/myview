import json

from django.http import JsonResponse
from django.shortcuts import render


def get_status(request):
    return JsonResponse({"status": True})


def index(request):
    data = {
        'name': 'hhhhhh',
        'age': 30,
        'hobbies': ['reading', 'traveling', 'cooking']
    }
    return render(request, 'index.html', {"status": True, 'data_json': json.dumps(data)})
