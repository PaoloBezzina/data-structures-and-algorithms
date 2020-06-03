"""
Task 5
"""

stack = [] 

def convert(expression):
    items  = expression.split()

    for item in items:

        print (stack)
        
        if item in {"+", "-", "x", "/"}:

            num2 = stack.pop()
            num1 = stack.pop()

            if item == "+":
                ans = num1 + num2
            if item == "-":
                ans = num1 - num2
            if item == "x":
                ans = num1 * num2
            if item == "/":
                ans = num1 / num2

            stack.append(ans)

        else:
            stack.append(int(item))

    
    return stack.pop()

"""
Testing Task 5
"""
print(convert("1 2 +"))
print(convert("22 11 / 33 x"))
print(convert("3 4 + 4"))
print(convert("100 2 + 30 z"))