from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
import uuid
from django.db import models


class CreatedMixin(models.Model):
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta:
        abstract = True


class ModifiedMixin(models.Model):
    modified = models.DateTimeField(_("Modification date"), auto_now=True)

    class Meta:
        abstract = True


class TimeStampedMixin(CreatedMixin, ModifiedMixin):
    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'content"."genre'
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")


class FilmWorkType(TextChoices):
    MOVIE = "movie"
    TV_SHOW = "tv_show"


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_("Full name"), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'content"."person'
        verbose_name = _("Actor")
        verbose_name_plural = _("Actors")


class Filmwork(UUIDMixin, TimeStampedMixin):
    title = models.TextField(_("Title"))
    description = models.TextField(_("Description"), default="", blank=True)
    release_date = models.DateTimeField(_("Release date"), null=True)
    rating = models.FloatField(
        _("Rating"),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.CharField(_("Film type"), max_length=50, choices=FilmWorkType.choices)
    genres = models.ManyToManyField(
        Genre, verbose_name=_("Genres"), through="GenreFilmwork"
    )
    actors = models.ManyToManyField(
        Person, verbose_name=_("Actors"), through="PersonFilmwork"
    )
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'content"."film_work'
        verbose_name = _("Film work")
        verbose_name_plural = _("Film works")


class GenreFilmwork(UUIDMixin, CreatedMixin):
    film_work = models.ForeignKey(
        Filmwork, verbose_name=_("Film"), on_delete=models.PROTECT
    )
    genre = models.ForeignKey(Genre, verbose_name=_("Genre"), on_delete=models.PROTECT)

    class Meta:
        db_table = 'content"."genre_film_work'
        unique_together = [["film_work", "genre"]]
        verbose_name = _("Film Genre")
        verbose_name_plural = _("Film genres")


class PersonFilmwork(UUIDMixin, CreatedMixin):
    film_work = models.ForeignKey(
        Filmwork, verbose_name=_("Film"), on_delete=models.PROTECT
    )
    person = models.ForeignKey(
        Person, verbose_name=_("Actor"), on_delete=models.PROTECT
    )
    role = models.TextField(_("Role"), null=True)

    class Meta:
        db_table = 'content"."person_film_work'
        unique_together = [["film_work", "person", "role"]]
        verbose_name = _("Film actor")
        verbose_name_plural = _("Movie actors")
