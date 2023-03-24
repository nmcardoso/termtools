def base_converter(value: str, ibase: int, obase: int, n: int):
  fmt_map = {2: 'b', 10: 'd', 16: 'x'}
  return format(int(value, ibase), '0>{}{}'.format(n, fmt_map[obase]))  