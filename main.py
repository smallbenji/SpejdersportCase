with open("output.txt", "a") as file:
    def question(q):
        answer = input(f"{q}: ")
        file.write(f"{q}: {answer}\n")

    question("Fornavn")
    question("Efternavn")
    question("Addresse")
    question("Telefon nr.")
    question("Email")