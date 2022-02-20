def append_in(self, pos, x):
    my_list = []
    a = 0
    for a in range(0, len(self)):
        my_list.append(MyList.__getitem__(self, a))
    return my_list.insert(pos, x)