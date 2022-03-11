from django.http import HttpResponse

def index(request):
    return HttpResponse("You are at the root of User Module")

def login(request):
    return HttpResponse("You are at the login")


def signup(request):
    return HttpResponse("You are at the signup")


def recovery(request):
    return HttpResponse("You are at the recovery")


def verify(request):
    return HttpResponse("You are at the verify")
