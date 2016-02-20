from django.shortcuts import render
from django.http import HttpResponseRedirect



def homeview(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/accounts/login/')

def testview(request):
    import pdb; pdb.set_trace()
    return render(request, 'test.html')
