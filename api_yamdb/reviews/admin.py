from django.contrib import admin
from reviews.models import Category, Genre, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'bio',
        'role'
    )
    search_fields = ('username',)
    list_filter = ('role',)


@admin.register(Category, Genre)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    search_fields = ('slug',)
    list_filter = ('name',)


admin.site.empty_value_display = '-пусто-'
