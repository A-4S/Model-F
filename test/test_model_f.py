from model_f import model_f
from .lib import filter_keys, func_demo

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
