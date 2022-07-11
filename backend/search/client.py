from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, **kwargs):
    """
    perform_search("hello", tags=["electronics"], public=True)
    """
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags

    # allows us to filter by anyother argument we might have
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if index_filters != 0:
        params['facetFilters'] = index_filters
    results = index.search(query, params)
    return results