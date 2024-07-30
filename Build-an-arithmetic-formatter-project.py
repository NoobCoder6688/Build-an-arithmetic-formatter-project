import re

def arithmetic_arranger(problems, show_answers=False):
    # Regular expressions for validation
    pattern1 = re.compile(r'^\s*\d+\s*[+-]\s*\d+\s*$')
    pattern2 = re.compile(r'^\s*\d{1,4}\s*[+-]\s*\d{1,4}\s*$')

    # List to hold all parts of the problems
    list_of_all = []

    # Validate the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        # Validate the operators
        if "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."
        # Validate that only digits are used
        if not pattern1.match(problem):
            return 'Error: Numbers must only contain digits.'
        # Validate the number of digits in each operand
        if not pattern2.match(problem):
            return 'Error: Numbers cannot be more than four digits.'
        
        # Split the problem into operands and operator
        operands_with_operator = re.split(r'\s*([\+\-])\s*', problem)
        list_of_all += operands_with_operator

    # Extract operands and operators
    operand1 = list_of_all[0::3]
    operand2 = list_of_all[2::3]
    operator = list_of_all[1::3]

    # Determine the maximum length of operands for formatting
    max_length = [max(len(o1), len(o2)) for o1, o2 in zip(operand1, operand2)]

    # Prepare the lines to be printed
    first_line = ''
    second_line = ''
    third_line = ''
    fifth_line = ''

    for i in range(len(operand1)):
        # Create the first line
        first_line += (max_length[i] + 2 - len(operand1[i])) * ' ' + operand1[i] + '    '
        # Create the second line
        second_line += operator[i] + ' ' * (max_length[i] + 1 - len(operand2[i])) + operand2[i] + '    '
        # Create the third line
        third_line += '-' * (max_length[i] + 2) + '    '

    # Prepare the results if show_answers is True
    if show_answers:
        for i in range(len(operand1)):
            result = str(eval(f'{operand1[i]} {operator[i]} {operand2[i]}'))
            fifth_line += ' ' * (max_length[i] + 2 - len(result)) + result + '    '

    # Combine the lines into the final output
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()
    if show_answers:
        arranged_problems += '\n' + fifth_line.rstrip()
    
    return arranged_problems

# Test the function
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')