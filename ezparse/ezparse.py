from . import helper
import re

L, R = helper.L, helper.R
LEFT, RIGHT = helper.LEFT, helper.RIGHT

class Parser:
    def __init__(self, *args, **kwargs):
        # Get our operator/function overrides.
        operators, functions = _arg_check(args)
        # Keyword assignments become our internal scope.
        # Internal scope assignments always take precedence
        # over function assignments.
        f_operations = {k:v[0] for k, v in functions.items()}
        o_operations = {k:v[0] for k, v in operators.items()}
        self.operations = {**f_operations, **o_operations}
        self._scope = dict(kwargs)
        self._operators = set(operators)
        self._functions = set(functions)
        self._precedence = {k:v[1] for k, v in operators.items()}
        self._left = {o for o in operators if operators[o][2] == L}
        self._right = {o for o in operators if operators[o][2] == R}
        
    def __call__(self, value):
        rpn = self.rpn(value)
        stack = _Stack()
        for token in rpn:
            if token in self.operations:
                val2, val1 = stack.pop(), stack.pop()
                stack.push(self.operations[token](val1, val2))
            else:
                if callable(token):
                    stack.push(token(self._scope))
                else:
                    stack.push(token)
        return stack[0]

    def rpn(self, text):
        """Translate an infix expression (given as a string) into
        reverse polish notation (RPN) using the parser instance's
        particular operation precedence and associativity rules.
        """
        output = []
        stack = _Stack()

        def pop_operator(t):
            o = stack.get_top()
            if o in self._operators:
                t_pre, o_pre = self._precedence[t], self._precedence[o]
                if ((t in self._left and t_pre <= o_pre) or
                        (t in self._right and t_pre < o_pre)):
                    output.append(stack.pop())
                    return pop_operator(t)

        def pop_parenthesis(t):
            top = stack.get_top()
            if top is None:
                raise Exception("Mismatched ()")
            if top == "(":
                stack.pop()
                if stack.get_top() in self._functions:
                    output.append(stack.pop())
                return
            output.append(stack.pop())
            return pop_parenthesis(t)

        formatted = self._format(text)
        for token in formatted:
            if _is_int(token):
                output.append(int(token))
            elif _is_float(token):
                output.append(float(token))
            elif token in self._functions:
                stack.push(token)
            elif token == ",":
                while stack.get_top() != "(":
                    output.append(stack.pop())
            elif token in self._operators:
                pop_operator(token)
                stack.push(token)
            elif token == "(":
                stack.push(token)
            elif token == ")":
                pop_parenthesis(token)
            else:
                matching = [s for s in self._scope if token.startswith(s)]
                if matching:
                    output.append(_Internal(token))
        for o in reversed(stack):
            output.append(stack.pop())
        return output

    def _format(self, text):
        pattern = "([( )," + "".join(self._operators) + "])"
        if "-" in pattern:
            i = pattern.index("-")
            pattern = pattern[:i] + "\\" + pattern[i:]
        raw = re.split(pattern, text)
        return [e for e in raw if e != " " and e != ""]


class _Stack(list):

    def push(self, item):
        self.append(item)

    def get_top(self):
        if len(self) > 0:
            return self[-1]



class _Internal:
    def __init__(self, path):
        _path = path.split(".")
        self.root = _path[0]
        self.path = _path[1:]

    def __call__(self, _dict):
        root = _dict[self.root]
        for step in self.path:
            root = getattr(root, step)
        if callable(root):
            return root()
        return root


def _arg_check(args):
    """Evaluate *args from Parser.__init__ for operation and
    function overrides; we do this instead of assigning these
    values as keywords to avoid polluting a parser instance's
    internal scope.
    """
    
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


def _is_int(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


def _is_float(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

