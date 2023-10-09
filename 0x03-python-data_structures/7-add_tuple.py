#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_aa = ((tuple_a[0] if len(tuple_a) > 0 else 0),
            (tuple_a[1] if len(tuple_a) > 1 else 0))
    tuple_bb = ((tuple_b[0] if len(tuple_b) > 0 else 0),
            (tuple_b[1] if len(tuple_b) > 1 else 0))
    return (tuple_aa[0] + tuple_bb[0],
            tuple_aa[1] + tuple_bb[1])
