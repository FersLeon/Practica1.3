def jaccard_distancia(x, y):
    x1 = set(x.split())
    y1 = set(y.split())
    interseccion = len(x1.intersection(y1))
    union = len(x1.union(y1))
    return (interseccion / union)

