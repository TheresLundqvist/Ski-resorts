from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from django.db.models import Avg

STATUS = ((0, 'Draft'), (1, 'Published'))


class Resort(models.Model):
    image = CloudinaryField("image", default="placeholder")
    resort = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=False)  # noqa
    description = models.TextField(null=False, blank=False)
    location_address = models.CharField(max_length=200, null=False, blank=False)  # noqa
    country = CountryField(blank_label="(select country)", default=True, max_length=80)  # noqa
    hours = models.CharField(max_length=200, null=False, blank=False)
    opening_season = models.CharField(max_length=300, null=False, blank=False)  # noqa
    has_ski_rentals = models.BooleanField(default=True, null=False, blank=False)  # noqa
    has_ski_lessons = models.BooleanField(default=False, null=False, blank=False)  # noqa
    offers_accommodation = models.BooleanField(default=False, null=False, blank=False)  # noqa
    restaurants = models.IntegerField(default=0, null=False, blank=False)
    adults_ski_pass_price = models.CharField(max_length=80, null=False, blank=False)  # noqa
    children_ski_pass_price = models.CharField(max_length=80, null=False, blank=False)  # noqa
    gondola_lifts = models.BooleanField(default=True, null=False, blank=False)
    chair_lifts = models.BooleanField(default=True, null=False, blank=False)
    button_lifts = models.BooleanField(default=True, null=False, blank=False)
    moving_carpet_lifts = models.BooleanField(default=True, null=False, blank=False)  # noqa
    easy_slopes = models.IntegerField(default=0, null=False, blank=False)
    intermediate_slopes = models.IntegerField(default=0, null=False, blank=False)  # noqa
    difficult_slopes = models.IntegerField(default=0, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.resort

    def average_rating(self) -> float:
        return Rating.objects.filter(resort=self).aggregate(Avg("star_rating"))["star_rating__avg"] or 0  # noqa


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)


class Rating(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    star_rating = models.IntegerField(User, default=0)  # noqa

    def __str__(self):
        return f"{self.resort}: {self.rating}"


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
