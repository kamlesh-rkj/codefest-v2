def is_higher_precedence(op1, op2):
    return (op1 in "*/" and op2 in "+-*/")
    # return (op1 in "*/" and op2 in "+-")

def perform_operation(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    else:
        raise ValueError("Invalid operator: " + operator)

def infix_to_postfix(formula):
    stack = []
    postfix_list = []
    for c in formula:
        if c.isdigit():
            postfix_list.append(c)
        elif c == ' ':
            continue
        elif c in "+-*/":
            while stack and is_higher_precedence(stack[-1], c):
                postfix_list.append(stack.pop())
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix_list.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        elif c == 's': # check for "substract" operator
            if formula[formula.index(c):formula.index(c)+9] == 'substract':
                postfix_list.append('-')
        elif c == 'm': # check for "multiple" operator
            if formula[formula.index(c):formula.index(c)+8] == 'multiple':
                postfix_list.append('*')
        else:
            raise ValueError("Invalid character: " + c)
    while stack:
        postfix_list.append(stack.pop())
    return postfix_list


def evaluate_postfix(postfix_formula):
    stack = []
    for c in postfix_formula:
        if c.isdigit():
            stack.append(float(c))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, c)
            stack.append(result)
    return stack.pop()

def is_correct_formula(formula, expected_result):
    try:
        postfix_formula = infix_to_postfix(formula)
        result = evaluate_postfix(postfix_formula)
        is_correct = (result == float(expected_result))
        return is_correct
    except:
        return False

# read input from file
with open("TMW_small.txt", "r") as input_file:
    # read number of test cases
    num_test_cases = int(input_file.readline())

    # open output file
    with open("TMW_small_output.txt", "w") as output_file:
        # loop through each test case
        for i in range(num_test_cases):
            try:
                # read formula and expected result
                line = input_file.readline().strip()
                formula, expected_result = line.split(" = ")

                # check if formula is correct
                is_correct = is_correct_formula(formula, expected_result)

                # write output to file
                output_file.write("Case #{}: {}\n".format(i+1, is_correct))
            except ValueError as e:
                # handle invalid input error
                output_file.write("Case #{}: false\n".format(i+1))
