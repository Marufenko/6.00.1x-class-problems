def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    new={}
    for k, v in d.items():
        if v in new.keys():
            tmp_list = new[v]
            print tmp_list
            tmp_list.append(k)
            print tmp_list
            tmp_list.sort()
            print tmp_list
            new[v] = tmp_list
            print new
        else:
            new[v] = [k, ]
            print new
    return new
