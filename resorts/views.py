from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Resort, Rating, Comment, Contact


class ResortList(generic.ListView):
    model = Resort
    queryset = Resort.objects.filter(status=1).order_by('country')
    template_name = 'index.html'
    paginate_by = 6


class ResortDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Resort.objects.filter(status=1)
        resort = get_object_or_404(queryset, slug=slug)
        comments = resort.comments.filter(approved=True).order_by("-created_on")  # noqa

        return render(
            request,
            "resort_detail.html",
            {
                "resort": resort,
                "comments": comments
            },
        )


class RatingDetail(View):
    def get(self, request, *args, **kwargs):
        rating = Rating.number_of_stars
        return render(
            request,
            "resort_detail.html",
            {
                "rating": rating
            },
        )
