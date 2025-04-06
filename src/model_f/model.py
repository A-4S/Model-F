from inspect import Parameter, _empty, signature
from types import MappingProxyType
from typing import Any, Callable

from pipe_fp import pipe
from pydantic import (
    BaseModel,
    create_model,
)

from .type import FDDict, FieldDefinition
from .util import mask


def field_definition(p: Parameter) -> FieldDefinition:
    def param_annotation(p: Parameter):
        match p.annotation is _empty:
            case True:
                match p.default is _empty:
                    case True:
                        return p.replace(annotation=Any)
                    case False:
                        return p.replace(annotation=type(p.default))
            case False:
                return p

    def param_default(p: Parameter):
        return p.replace(default=...) if p.default is _empty else p

    def field(p: Parameter):
        return (p.annotation, p.default)

    return pipe(
        param_annotation,
        param_default,
        field
    )(p)


def field_definitions(params: MappingProxyType[str, Parameter]):
    return { p.name: field_definition(p) for p in params.values() }


@mask(create_model)
def model_f(*args, **kwargs):
    def construct_model[T](
            f: Callable,
            cb: Callable[[FDDict[T]], FDDict[T]] | None=None
        ) -> type[BaseModel]:

        return pipe(
            lambda f: field_definitions(signature(f).parameters),
            lambda f_d: cb(f_d) if cb is not None else f_d,
            lambda f_d: create_model(*args, **f_d, **kwargs)
        )(f)

    return construct_model
