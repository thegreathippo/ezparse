# ezparser
ezparser provides instances of the Parser class, which accept infix expressions (as strings) and return callable objects (Formulas) that evaluate these expressions when called.

When instanced, a Parser object accepts keyword arguments. These keywords effectively become the 'namespace' for the infix expressions that the Parser evaluates. 

When called, Formulas will return either a single value or a tuple of values -- dependent on the expression provided to the Parser that produced it.

