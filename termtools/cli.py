import argparse

from tabulate import tabulate

from .conversions import base_converter


def b2h():
  parser = argparse.ArgumentParser(
    prog='b2h', 
    description='Binary to Hex Converter'
  )
  parser.add_argument(
    'values', 
    help='binary value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='fixed number of digits in output',
    action='store',
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
      converted = base_converter(value, ibase=2, obase=16, n=args.n)
      print(converted)
      
      
      
def h2b():
  parser = argparse.ArgumentParser(
    prog='h2b', 
    description='Hex to Binary Converter'
  )
  parser.add_argument(
    'values', 
    help='hex value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='fixed number of digits in output',
    action='store',
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    converted = base_converter(value, ibase=16, obase=2, n=args.n)
    print(converted)
    
    
    
def b2d():
  parser = argparse.ArgumentParser(
    prog='b2d', 
    description='Binary to Decimal Converter'
  )
  parser.add_argument(
    'values', 
    help='binary value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='fixed number of digits in output',
    action='store',
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    converted = base_converter(value, ibase=2, obase=10, n=args.n)
    print(converted)
    
    
    
def d2b():
  parser = argparse.ArgumentParser(
    prog='d2b', 
    description='Decimal to Binary Converter'
  )
  parser.add_argument(
    'values', 
    help='decimal value(s) to be converted separated by space', 
    nargs='+',
    action='store',
  )
  parser.add_argument(
    '-n',
    help='fixed number of digits in output',
    action='store',
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    converted = base_converter(value, ibase=10, obase=2, n=args.n)
    print(converted)
    
    
    
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
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    hex_value = base_converter(value, ibase=2, obase=16, n=args.n).upper()
    dec_value = base_converter(value, ibase=2, obase=10, n=args.n)
    table = [
      ['BIN', value, len(value)],
      ['HEX', hex_value, len(hex_value)],
      ['DEC', dec_value, len(dec_value)]
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
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    bin_value = base_converter(value, ibase=16, obase=2, n=args.n)
    dec_value = base_converter(value, ibase=16, obase=10, n=args.n)
    table = [
      ['HEX', value.upper().replace('X', 'x'), len(value)],
      ['BIN', bin_value, len(bin_value)],
      ['DEC', dec_value, len(dec_value)]
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
    default=''
  )
  args = parser.parse_args()
  
  for value in args.values:
    bin_value = base_converter(value, ibase=10, obase=2, n=args.n)
    hex_value = base_converter(value, ibase=10, obase=16, n=args.n)
    table = [
      ['DEC', value, len(value)],
      ['BIN', bin_value, len(bin_value)],
      ['HEX', hex_value.upper(), len(hex_value)]
    ]
    print(tabulate(table, tablefmt='rounded_grid'))