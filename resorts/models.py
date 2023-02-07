from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Resort(models.Model):
    image = CloudinaryField("image", default="placeholder")
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    hours = models.CharField(max_length=200, null=False, blank=False)
    opening_season = models.CharField(max_length=300, null=False, blank=False)  # noqa
    has_ski_rentals = models.BooleanField(default=True, null=False, blank=False)  # noqa
    has_ski_lessons = models.BooleanField(default=False, null=False, blank=False)  # noqa
    offers_accommodation = models.BooleanField(default=False, null=False, blank=False)  # noqa
    restaurants = models.IntegerField(default=0, null=False, blank=False)
    adults_ski_pass_price = models.IntegerField(default=0, null=False, blank=False)  # noqa
    children_ski_pass_price = models.IntegerField(default=0, null=False, blank=False)  # noqa
    gondola_lifts = models.BooleanField(default=True, null=False, blank=False)
    chair_lifts = models.BooleanField(default=True, null=False, blank=False)
    button_lifts = models.BooleanField(default=True, null=False, blank=False)
    moving_carpet_lifts = models.BooleanField(default=True, null=False, blank=False)  # noqa
    easy_slopes = models.IntegerField(default=0, null=False, blank=False)
    intermediate_slopes = models.IntegerField(default=0, null=False, blank=False)  # noqa
    difficult_slopes = models.IntegerField(default=0, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def ___str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)


class Rating(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    rating = models.IntegerField(default=10, null=False, blank=False)


class Comment(models.Model):
    post = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='comments')  # noqa
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
