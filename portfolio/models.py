from django.db import models

# Create your models here.
class UserData(models.Model):
    title_tab = models.CharField(max_length=100, blank=True)
    image_header = models.ImageField(blank=True, upload_to="images/")
    name = models.CharField(max_length=50, blank=True)
    title_header = models.CharField(max_length=100, blank=True)
    skill_header = models.CharField(max_length=255, blank=True)
    about_me_title = models.CharField(max_length=100, blank=True)
    about_me_text = models.TextField(blank=True)
    cv_file = models.FileField(null=True, upload_to="cv/")
    location = models.CharField(max_length=50, blank=True)
    city_and_country = models.CharField(max_length=50, blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    behance_url = models.URLField(blank=True)

    def __str__(self):
        return f"Portfolio de {self.name}"


class Portfolio(models.Model):
    job_image = models.ImageField(blank=True, upload_to="portfolio-images/")
    job_url = models.URLField(blank=True)

    def __str__(self):
        return f"Portfolio de {self.job_url}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
