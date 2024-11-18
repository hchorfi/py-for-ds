def NULL_not_found(object: any) -> int:
    #your code here
    obj_type = type(object)
    if object is None:
        print(f'Nothing: None {obj_type}')
    elif obj_type is float and object != object:
        print(f'Cheese: nan {obj_type}')
    elif obj_type is int and object == 0:
        print(f'Zero: 0 {obj_type}')
    elif obj_type is str and object == '':
        print(f'Empty: {obj_type}')
    elif obj_type is bool and object == False:
        print(f'Fake: False {obj_type}')
    else:
        print('Type not Found')
        return 1
    return 0