from algoliasearch_django import AlgoliaIndex
from .models import Product
from algoliasearch_django.decorators import register

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index states if the item will go into algolia's console or not
    # should_index = 'is_public'
    fields = [
        'title',
        'body',
        'price',
        'user',
        'public',
        'path',
        'endpoint',
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'