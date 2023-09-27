def formule_van_fibonacci(n):
  if n <= 0:
    return "Ongeldige invoer. Geef een positief getal."
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    fib_seq = [0, 1]
    while len(fib_seq) < n:
      next_num = fib_seq[-1] + fib_seq[-2]
      fib_seq.append(next_num)
    return fib_seq[-1]



print(formule_van_fibonacci(1000000))