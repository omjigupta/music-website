from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is omji first django project</h1>")
