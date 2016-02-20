from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Timeline

@login_required
class TimelineListView(ListView):

    model = Timeline
    template_name = "timeline/list.html"

    def get_queryset(self):
        return Timeline.objects.filter(user=self.request.user)


@login_required
def timelineview(request, slug):
    timeline = get_object_or_404(Timeline, id=slug, user=request.user)
    context = {
        'timeline': timeline,
    }
    return render(request, "timeline/detail.html", context)



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
        Timeline.objects.create(user=user,title=name,color=color,icon=file)
    return render(request, 'test.html')
