from django import template
from favs.models import FavList

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, contents):
    user = context.request.user
    fav_list, _ = FavList.objects.get_or_create(created_by=user)
    return contents in fav_list.books.all() or contents in fav_list.movies.all()
