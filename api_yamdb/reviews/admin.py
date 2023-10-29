from django.contrib import admin
from itertools import chain

from reviews.models import Category, Comment, Genre, Review, Title, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role'
    )
    list_editable = ('role',)
    search_fields = ('username',)
    list_filter = ('role',)


@admin.register(Category, Genre)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    search_fields = ('slug',)
    list_filter = ('name',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'rating',
        'description',
        'category',
        'genre_names',
    )
    list_editable = ('category',)
    search_fields = ('name',)
    list_filter = ('name',)
    filter_horizontal = ('genre',)

    def genre_names(self, obj):
        a = obj.genre.values_list('name')
        return list(chain.from_iterable(a))


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'text',
        'score',
        'pub_date',
    )
    search_fields = ('title',)
    list_filter = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'review',
        'text',
        'pub_date',
    )
    search_fields = ('author',)
    list_filter = ('author',)


admin.site.empty_value_display = '-пусто-'
