import collections

R = "RIGHT"
L = "LEFT"
RIGHT = R
LEFT = L

def add(val1, val2):
	return val1 + val2

def subtract(val1, val2):
	return val1 - val2

def divide(val1, val2):
	answer = val1 / val2
	if int(answer) == answer:
		return int(answer)
	return answer

def multiply(val1, val2):
	return val1 * val2

def exponent(val1, val2):
	return val1 ** val2

def _max(*args):
	return max(*args)

def _min(*args):
        return min(*args)

Operator = collections.namedtuple("Operator", ["function", "precedence",
                                               "associativity"])
Function = collections.namedtuple("Function", ["function"]) 

operators = {
	"+" : Operator(2, L, add),
	"-" : Operator(2, L, subtract),
	"/" : Operator(3, L, divide),
	"*" : Operator(3, L, multiply),
	"^" : Operator(4, R, exponent)
	}
		
functions = {
	"max" : Function(_max),
	"min" : Function(_min)
	}
