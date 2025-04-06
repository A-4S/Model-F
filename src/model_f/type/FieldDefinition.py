from typing import Dict

type FieldDefinition[T] = Dict[str, tuple[type[T], T]]
