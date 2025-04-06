def filter_keys[T](exclude: dict[str, bool]):
    def execute_filter(d: dict[str, T]):
        return dict(filter(lambda e: not exclude.get(e[0]), d.items()))
    
    return execute_filter
