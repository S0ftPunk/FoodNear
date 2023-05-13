from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Place, Comment, Picture
from  django.views.generic import  DetailView
from django.contrib.auth.decorators import login_required


def index(request,place_id):

    try:
        a = Place.objects.get(id = place_id)
    except:
        raise Http404()

    data = {'comments': Comment.objects.filter(place = a )[::-1],
            "place" : a,
            "ind" : place_id,
            "pictures": Picture.objects.filter(place = a),
            }
    return render(request, 'comments/rate1.html',data)


class CommentsOfPlace(DetailView):
    model = Comment
    template_name = 'comments/rate1.html'
    context_object_name = "comments"

@login_required
def leave_comment(request,ind):
    try:
        a = Place.objects.get(id = ind)
    except:
        raise Http404()
    #
    if request.POST['text'] != "" and not(Comment.objects.filter(place=a, author=request.user).exists()):
        a.comment_set.create(author=request.user, comment_text=request.POST['text'])
        return redirect(f"/comments/{ind}")
    else:
        return HttpResponse(status=204)
    # return render(request, 'comments/rate1.html', data)