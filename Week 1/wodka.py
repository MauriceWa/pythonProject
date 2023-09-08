def survey():
  print('1) Blue')
  print('2) Red')
  print('3) Yellow')

  ans = 0
  while not ans:
    try:
      ans = int(input('Out of these options\(1, 2, 3), which is your favourite?'))
      if ans not in (1, 2, 3):
        raise ValueError
    except ValueError:
      ans = 0
      print("That's not an option!")

  if ans == 1:
    print('Nice!')
  elif ans == 2:
    print('Cool')
  elif ans == 3:
    print('Awesome!')
  return None
