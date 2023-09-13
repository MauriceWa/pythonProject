def decide_discount(age):
  if age < 18:
    return 10
  else:
    return 0


def decide_ticket_price(discount_in_percentages): #parameter
  TICKET_PRICE = 13.50
  return TICKET_PRICE - (TICKET_PRICE * (discount_in_percentages / 100))

#Ticket price

def print_ticket(first_name, surname, ticket_price):
  print(first_name,surname,"Ticket price:", ticket_price)

def main():
  first_name = input("What is your first name?")
  surname = input("What is your surname?")
  age = int(input("What is your age?"))

  print_ticket(first_name,surname,decide_ticket_price(decide_discount(age)))

if __name__ == "__main__":
    main()