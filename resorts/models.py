from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Resort(models.Model):
    image = CloudinaryField("image", default="placeholder")
    name = models.CharField(null=False, blank=False, unique=True)
    description = models.TextField(max_length=2000, null=False, blank=False)
    location = models.CharField(null=False, blank=False)
    hours = models.CharField(null=False, blank=False)
    opening_season = models.charField(null=False, blank=False)
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


class Contact(models.Model):
    name = models.CharField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)


class Rating(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)  # noqa
    rating = models.IntegerField(default=10, null=False, blank=False)
