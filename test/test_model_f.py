from model_f import model_f


def func_demo(a: int, x, b=2, c: int=3): ...

def filter_keys[T](exclude: dict[str, bool]):
    def execute_filter(d: dict[str, T]):
        return dict(filter(lambda e: not exclude.get(e[0]), d.items()))
    
    return execute_filter

def test_model_f():
    TestModelA = model_f('TestModelA')(func_demo)
    TestModelB = model_f('TestModelB')(func_demo, filter_keys({ 'x': True }))

    print(TestModelA.__pydantic_fields__)
    print(TestModelB.__pydantic_fields__)

    assert TestModelA.__pydantic_fields__['b'].annotation is int
    assert TestModelB.__pydantic_fields__['b'].annotation is int

    assert len(TestModelA.__pydantic_fields__) == 4
    assert len(TestModelB.__pydantic_fields__) == 3

    assert TestModelB.__pydantic_fields__.get('x') is None

    assert len(TestModelA(a=1, x=2).model_dump().keys()) == 4
    assert len(TestModelB(a=1, b=2).model_dump().keys()) == 3
