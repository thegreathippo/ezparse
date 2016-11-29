def get_arg_num(group):
  level, commas, values = 0, 0, 0
  for e in group:
    if e == "(":
      level += 1
    elif e == ")":
      level -= 1
    elif level == 1:
      if e == ",":
        commas += 1
        values += 1
      elif values == 0:
        values += 1
  return values



test_1 = "f(3, (5 + 2, 5 + 9), 5 + 10 + 3)"
ans = (3)
test1 = "f", "(", 3, ",", "(", 5, "+", 2, ",", 5, "+", 9, ")", ",", 5, "+", 10, "+", 3, ")"

test_2 = "((5, 3, 6) + 10, (3, 1 + 2), -10)"
ans = (3)
test2 = "(", "(", 5, ",", 3, ",", 6, ")", "+", 10, ",", "(", 3, ",", 1, "+", 2, ")", ",", -10, ")"

test_3 = "()"
ans = (0)
test3 = "(", ")"

print(get_arg_num(test1))
print(get_arg_num(test2))
print(get_arg_num(test3))
