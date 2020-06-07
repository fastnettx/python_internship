from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver
from locations_api.tasks import send_email_when_creating, send_email_when_changing


class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "flag"
        verbose_name_plural = "flags"


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    cities_count = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"


class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.ForeignKey(Country, related_name='country_name', on_delete=models.CASCADE)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def print_name(self):
        return self.name


@receiver(signal=pre_save, sender=City)
def display_message_about_adding_a_city(sender, instance, **kwargs):
    print("City " + instance.name + " will be added")


@receiver(signal=post_save, sender=City)
def increase_counter(sender, instance, **kwargs):
    instance.country.cities_count += 1
    instance.country.save()


@receiver(signal=pre_delete, sender=City)
def decrease_counter(sender, instance, **kwargs):
    instance.country.cities_count -= 1
    instance.country.save()


@receiver(signal=post_delete, sender=City)
def show_remote_city(sender, instance, **kwargs):
    print("City " + instance.name + " has been deleted")


@receiver(signal=post_save, sender=Country)
def save_country_send_email(sender, instance, **kwargs):
    if kwargs['created']:
        for user_country in instance.users.all():
            send_email_when_creating.delay(user_country.email, instance.name)
    else:
        for user_country in instance.users.all():
            send_email_when_changing.delay(user_country.email, instance.name, instance.id)
