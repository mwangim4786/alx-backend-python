#!/usr/bin/env python3
'''takes a float n as argument and returns the floor of the float
'''

def floor(n: float) -> int:
	if n >= 0:
		return(int(n))
	else:
		return(int(n) - 1)
