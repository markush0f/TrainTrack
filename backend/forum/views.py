from django.shortcuts import render
from django.http import JsonResponse


def loadMessages():
    return JsonResponse({"error": ""})


def sendMessage():
    return JsonResponse({"error": ""})
