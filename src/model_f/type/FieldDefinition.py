from typing import Dict, Any


type FieldDefinition[T=Any] = tuple[type[T], T] | type[T]

type FDDict[T=Any] = Dict[str, FieldDefinition[T]]
