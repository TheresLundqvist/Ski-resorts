from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from .models import Resort, Rating, Comment, Contact
from .forms import CommentForm


class ResortList(generic.ListView):
    model = Resort
    queryset = Resort.objects.filter(status=1).order_by('country')
    template_name = 'index.html'
    paginate_by = 6


class ResortDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Resort.objects.filter(status=1)
        resort = get_object_or_404(queryset, slug=slug)
        comments = resort.comments.filter(approved=True).order_by("created_on")  # noqa
        rating = resort.average_rating

        return render(
            request,
            "resort_detail.html",
            {
                "resort": resort,
                "comments": comments,
                "commented": False,
                "rating": rating,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Resort.objects.filter(status=1)
        resort = get_object_or_404(queryset, slug=slug)
        comments = resort.comments.filter(approved=True).order_by("created_on")  # noqa
        rating = resort.average_rating

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = resort
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "resort_detail.html",
            {
                "resort": resort,
                "comments": comments,
                "commented": True,
                "rating": rating,
                "comment_form": CommentForm()
            },
        )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        query = Contact(name=name, email=email, phone=phone, subject=subject, body=desc)  # noqa
        query.save()
        messages.success(request, "Thank's for sharing!")
        return redirect('/contact')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def edit_comment(request, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.user == request.user:
        messages.error(request, 'You dont have access to edit this comment')
        return redirect('resort_detail', slug)
    form = CommentForm(request.POST or None, instance=comment)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.approved = False
            form.save()
            messages.success(request, 'Comment updated. Awaiting approval')
            return redirect('resort_detail', slug)
        messages.error(request, 'Error occured. Please try again')
    context = {
        'comment': comment,
        'form': form,
    }
    template = 'edit_comment.html'
    return render(request, template, context)


def delete_comment(request, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.user == request.user:
        messages.error(request, 'You dont have access to delete this comment')
        return redirect('resort_detail', slug)
    comment.delete()
    messages.success(request, 'Comment successfully deleted')
    return redirect('resort_detail', slug)
