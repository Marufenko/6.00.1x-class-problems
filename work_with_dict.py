def dict_interdiff(d1, d2):
  same = set(d1.keys()) & set(d2.keys()) # Keys in both dicts
  a = dict([(k, f(d1[k], d2[k])) for k in same]) # values
  dif = set(d1.keys()) ^ set(d2.keys()) # Keys in single dict
  b = dict([(k,d1.get(k, d2.get(k))) for k in dif]) # values
  return (a, b,)
