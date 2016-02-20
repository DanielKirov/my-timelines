from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .models import Timeline

@login_required
def timelineview(request, slug):
    timeline = get_object_or_404(id=slug, user=request.user)
    context = {
        'timeline': timeline,
    }
    return render(request, "timeline.html", context)



def homeview(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/accounts/login/')

def testview(request):
    import pdb; pdb.set_trace()
    return render(request, 'test.html')
