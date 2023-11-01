import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """Фильтр для модели Title (произведение)."""

    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    genre = django_filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    category = django_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
<<<<<<< HEAD
=======
    year = django_filters.NumberFilter(field_name='year')
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

    class Meta:
        model = Title
        fields = [
            'name',
            'year',
            'genre',
            'category'
<<<<<<< HEAD
        ]
=======
        ]
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
