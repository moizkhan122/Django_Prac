from django.http import HttpResponse

def name(request):
    return HttpResponse("Hello moiz cham")

def namedetail(request,detail):
    return HttpResponse(detail)