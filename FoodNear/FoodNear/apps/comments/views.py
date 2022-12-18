from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Place, Comment
def index(request):

    return render(request, 'rate1.html', {'comments': Comment.objects.all()[::-1]})

def leave_comment(request):
    try:
        a = Place.objects.get(id=1)
    except:
        raise Http404()

    a.comment_set.create(author=request.POST['name'], comment_text=request.POST['text'])
    return render(request, 'rate1.html', {'comments': Comment.objects.all()[::-1]})