from django.http import HttpResponse

def index(request):
    return HttpResponse("Deployed Django App on AWS EBS Successfully :)")
