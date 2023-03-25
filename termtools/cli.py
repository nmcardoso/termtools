import argparse

from tabulate import tabulate

from .conversions import base_converter, twos_compl, unsigned_to_signed


def bconv():
  parser = argparse.ArgumentParser(
    prog='bconv', 
    description='Convert binary number to hexadecimal and decimal'
  )
  parser.add_argument(
    'values', 
    help='binary value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='minimum number of digits in output',
    action='store',
    default=None,
    type=int,
  )
  args = parser.parse_args()
  
  for value in args.values:
    n_bits = args.n if args.n else len(value)
    hex_value = base_converter(value, ibase=2, obase=16).upper()
    uint_value = base_converter(value, ibase=2, obase=10)
    sint_value = unsigned_to_signed(int(uint_value), n_bits=n_bits)
    table = [
      ['BIN', value + ' ({})'.format(len(value))],
      ['HEX', hex_value],
      ['UNS', uint_value],
      ['SIG', sint_value],
    ]
    print(tabulate(table, tablefmt='rounded_grid'))
    
    

def hconv():
  parser = argparse.ArgumentParser(
    prog='hconv', 
    description='Convert hexadecimal number to binary and decimal'
  )
  parser.add_argument(
    'values', 
    help='hexadecimal value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='minimum number of digits in output',
    action='store',
    default=None,
    type=int,
  )
  args = parser.parse_args()
  
  for value in args.values:
    bin_value = base_converter(value, ibase=16, obase=2, n_bits=args.n)
    n_bits = args.n if args.n else len(bin_value)
    uint_value = base_converter(value, ibase=16, obase=10)
    sint_value = unsigned_to_signed(int(uint_value), n_bits=n_bits)
    table = [
      ['HEX', value.upper().replace('X', 'x')],
      ['BIN', bin_value],
      ['UNS', uint_value],
      ['SIG', sint_value],
    ]
    print(tabulate(table, tablefmt='rounded_grid'))
    
    
    
def dconv():
  parser = argparse.ArgumentParser(
    prog='dconv', 
    description='Convert decimal number to binary and hexadecimal'
  )
  parser.add_argument(
    'values', 
    help='hexadecimal value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='minimum number of digits in output',
    action='store',
    default=None,
    type=int,
  )
  args = parser.parse_args()
  
  for value in args.values:
    bin_value = base_converter(value, ibase=10, obase=2, n_bits=args.n)
    hex_value = base_converter(value, ibase=10, obase=16, n_bits=args.n)
    table = [
      ['DEC', value, len(value)],
      ['BIN', bin_value, len(bin_value)],
      ['HEX', hex_value.upper(), len(hex_value)]
    ]
    print(tabulate(table, tablefmt='rounded_grid'))