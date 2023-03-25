from typing import Union


def base_converter(value: str, ibase: int, obase: int, n_bits: int = None):
  fmt_map = {2: 'b', 10: 'd', 16: 'x'}
  n_bits = n_bits or ''
  return format(int(value, ibase), '0>{}{}'.format(n_bits, fmt_map[obase]))


def unsigned_to_signed(value: int, n_bits: int):
  """compute the 2's complement of int value val"""
  if (value & (1 << (n_bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
    value = value - (1 << n_bits)        # compute negative value
  return value  


def twos_compl(value: Union[str, int], n_bits: int):
  if isinstance(value, str):
    value_int = int(value, 2)
  elif isinstance(value, int):
    value_int = value
    value = base_converter(str(value), ibase=10, obase=2, n_bits=n_bits)
  
  if (value_int & (1 << (n_bits - 1))) == 0:
    compl = str(abs(~value_int) + 0b1)
    return base_converter(compl, ibase=10, obase=2, n_bits=n_bits)

  return value