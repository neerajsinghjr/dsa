"""
NOTE:
class array(builtins.object)

 |  array(typecode [, initializer]) -> array
 |  
 |  Return a new array whose items are restricted by typecode, and
 |  initialized from the optional initializer value, which must be a list,
 |  string or iterable over elements of the appropriate type.
 |  
 |  Arrays represent basic values and behave very much like lists, except
 |  the type of objects stored in them is constrained. The type is specified
 |  at object creation time by using a type code, which is a single character.
 |  The following type codes are defined:
 |  
 |      Type code   C Type             Minimum size in bytes 
 |      'b'         signed integer     1 
 |      'B'         unsigned integer   1 
 |      'u'         Unicode character  2 (see note) 
 |      'h'         signed integer     2 
 |      'H'         unsigned integer   2 
 |      'i'         signed integer     2 
 |      'I'         unsigned integer   2 
 |      'l'         signed integer     4 
 |      'L'         unsigned integer   4 
 |      'q'         signed integer     8 (see note) 
 |      'Q'         unsigned integer   8 (see note) 
 |      'f'         floating point     4 
 |      'd'         floating point     8 
 |  NOTE: The 'u' typecode corresponds to Python's unicode character. On 
 |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
 |  
 |  NOTE: The 'q' and 'Q' type codes are only available if the platform 
 |  C compiler used to build Python supports 'long long', or, on Windows, 
 |  '__int64'.


"""

from array import array


x = array('u', ['a','b','c','d'])

for arr in x:
	print(arr)	

help(array)