from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *


def homeview(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/accounts/login/')

def testview(request):
    #import pdb; pdb.set_trace()
    return render(request, 'test.html')

def addTimeline(request):
    if request.method == 'POST':
        file = request.FILES['pic']
        name = request.POST['name']
        color = request.POST['color']
        user = request.user
        import pdb; pdb.set_trace()
        Timeline.objects.create(user=user,title=name,color=color,icon=file)
    return render(request, 'test.html')