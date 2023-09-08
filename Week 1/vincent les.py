def main():

  aantal_plaatsen = 15

  print("Er zijn", aantal_plaatsen, "beschikbare plekken in de bios.")

  aantal_plekken_reserven = int(input("Hoeveel plekken wilt u reserveren?"))

  if aantal_plekken_reserven > aantal_plaatsen:
    print("Helaas, zoveel plekken hebben wij niet.")
  else:
    aantal_plaatsen = aantal_plaatsen - aantal_plekken_reserven
    print("Er zijn nu", aantal_plaatsen, "beschikbare plekken in de bios.")



if __name__ == '__main__':
  main()