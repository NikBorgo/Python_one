# calculator
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

dictio = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

def function():
    num1 = (int(input("First number:")))
    for i in dictio:
        print(i)
    finished = False
    while not finished:
        symbol = input("Choose operation symbol you want to use:")
        num2 = (int(input("Next number:")))
        answer = dictio[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        continue_calculation = input(f"type 'y' to continue with {answer} or 'n' to run again:").lower()
        if continue_calculation == "n":
            finished = True
            function()
            num1 = answer
function()