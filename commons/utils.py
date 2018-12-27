from enum import Enum


# noinspection PyCompatibility
def objTypeCheck(obj, parentType, objName):
    if issubclass(parentType, Enum):
        if obj not in [et.value for et in parentType]:
            raise ValueError(f"Invalid value for {objName}:{obj}")
        return
    if not isinstance(obj, parentType):
        raise TypeError(f"Argument {objName} must be of type {parentType.__name__}")


def enumTuples(enumType, valueFirst=True):
    if valueFirst:
        return [(et.value, et.name) for et in enumType]
    return [(et.name, et.value) for et in enumType]
