from . import helper

L, R = helper.L, helper.R
LEFT, RIGHT = helper.LEFT, helper.RIGHT

class Parser:
    def __init__(self, *args, **kwargs):
        operators, functions = _arg_check(args)
        self._scope = dict(kwargs)
        f_operations = {k:v[0] for k, v in functions.items()}
        o_operations = {k:v[0] for k, v in operators.items()}
        self.operations = {**f_operations, **o_operations}
        self.precedence = {k:v[1] for k, v in operators.items()}
        self.left = {o for o in operators if operators[o][2] == L}
        self.right = {o for o in operators if operators[o][2] == R}
        
        

    def __call__(self, value):
        pass

    def rpn(self, text):
        pass
    

class _Stack(list):

    def push(self, item):
        self.append(item)

    def get_top(self):
        if len(self) > 0:
            return self[-1]


def _arg_check(args):
    operators = dict(helper.operators)
    functions = dict(helper.functions)
    if len(args) > 0:
        # raise error here if args[0] isn't dict-like?
        operators.update(args[0])
    if len(args) > 1:
        # raise error here if args[1] isn't dict-like?
        functions.update(args[1])
    if len(args) > 2:
        # too many arguments, raise error
        pass
    return operators, functions
