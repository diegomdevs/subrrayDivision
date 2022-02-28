def birthday(s: list, d: int, m: int) -> int:
  sum: int = 0
  squares: int = 0
  element: int = 0
  a: int = 1
  for i in range(0, len(s)):
    print(f"""
          sum = {sum}
          squares = {squares}
          element = {element}
          a = {a}
          """)
    element = s[i]
    if i == ((m * a) - 1):
      sum += element
      if sum == d:
        sum = 0
        squares += 1
        a += 1
      else:
        sum = 0
        a += 1
    else:
      sum += element
    if squares == m:
      break
  return squares

print(birthday([1, 2, 1, 3, 2], 3, 2))