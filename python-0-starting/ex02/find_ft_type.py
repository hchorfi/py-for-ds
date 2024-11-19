def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if isinstance(object, (list, tuple, set, dict)):
        print(f'{obj_type.__name__.capitalize()} : {obj_type}')
    elif isinstance(object, str):
        print(f'{object.capitalize()} is in the kitchen : {obj_type}')
    else:
        print("Type not found")
    return 42
