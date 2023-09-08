def main():
  woord_1 = "smnetl"

  woord_2 = "aegsed"

  output_woord = ""

  for i in range(len(woord_1)):
    output_woord += woord_1[i]
    output_woord += woord_2[i]

  print(output_woord)


if __name__ == '__main__':
  main()