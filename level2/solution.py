import bisect


def answer(h, q):
    rs = list(tree_roots(h))
    parent_map = dict(zip(rs, rs[1:] + [-1]))
    parent_map.update((r * 2, parent_map[r]) for r in rs[:-1])

    return [parent_node(n, rs, parent_map) for n in q]


def cache(f):
    _cache = {}

    def wrapped_f(*args, **kwargs):
        return f(*args, **kwargs)

        key = tuple(args) + tuple(kwargs.items())
        if key in _cache:
            return _cache[key]
        else:
            res = f(*args, **kwargs)
            _cache[key] = res
            return res

    return wrapped_f


def parent_node(n, rs, parent_map):
    if n in parent_map:
        return parent_map[n]
    else:
        st_root = nearest_subtree_root(n, rs)
        st_node = n - st_root
        res = parent_node(st_node, rs, parent_map) + st_root
        parent_map[n] = res
        return res


def tree_roots(h):
    n = 1
    for _ in range(h):
        yield n
        n = n * 2 + 1


@cache
def nearest_subtree_root(n, rs):
    return rs[bisect.bisect_right(rs, n) - 1]
