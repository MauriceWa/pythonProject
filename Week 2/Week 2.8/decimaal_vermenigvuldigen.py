try:
  number = int(input())
  decimal_number = float(input())
  print(number * decimal_number)
except ValueError as e:
  print("There was an error with your input, please input a number " + str(e))
except:
  print("There was an error")