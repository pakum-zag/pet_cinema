from django.contrib import admin
from .models import Genre, Filmwork, GenreFilmwork, PersonFilmwork, Person


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork
    extra = 0


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    extra = 0


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    list_display = (
        "title",
        "type",
        "release_date",
        "rating",
    )
    list_filter = ("type",)
    search_fields = ("title", "description", "id")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name", "id")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "id")
