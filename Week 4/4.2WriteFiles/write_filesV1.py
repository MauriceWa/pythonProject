def creeer_het():
    with open("Test123", "x") as file:
        file.write("Kanker")

def schrijf_erin():
    with open("Logs.txt", "a") as file:
        file.write('\n' + input())
