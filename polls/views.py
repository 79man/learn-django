from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse("Hello World. Polls /index")
    #HttpResponse()
    #return JsonResponse([1,2,3], safe=False)

# Sample route added just to familiarize myself - #ToBeRemoved
def show(request) :
    return HttpResponse("Hello World. polls/1 : Details")