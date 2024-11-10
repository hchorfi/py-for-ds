# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$

def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if isinstance(object, (list, tuple, set, dict)):
        print(f'{obj_type.__name__.capitalize()} : {obj_type}')
    elif isinstance(object, str):
        print(f'{object.capitalize()} is in the kitchen : {obj_type}')
    else:
        print("Type not found")
    return 42