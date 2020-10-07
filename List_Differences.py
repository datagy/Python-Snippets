def difference(a, b):
  """Returns items that exist only in list a, but not in b."""
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
