# Step 1: Split the input and check if they satisfy all rules
# Step 2: Arrange the input to be displayed into viewer screen. There will be 3 or 4 lines. Note where the operand should be put, as the width of one set depends on 2 + maximum length of the two input numbers
# Step 3: Calculate optionally and display the answers too. Use join with empty strings of 4 white spaces to make it align with the above lines.

def arithmetic_arranger(problems, show_Answers=False):

  # Step 1
  #Check for number of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  #Check for valid operators: only '+' and '-' are accepted
  #Split the inputs, they are first_number, operator, and second_number
  #Arrange them to prepare for display. Use a list.
  arranged_problems = []
  for problem in problems: 
    firstNum, operator, secondNum = problem.split()
    
    if operator not in ('+', '-'):
      return "Error: Operator must be '+' or '-'."

    if not firstNum.isdigit() or not secondNum.isdigit():
      return "Error: Numbers must only contain digits."

    if len(firstNum) > 4 or len(secondNum) > 4:
      return "Error: Numbers cannot be more than four digits."

    #If the input reaches here, it means it is a valid input and we will append them into our list, taking note of the triplets tuple data that we are dealing with.
    arranged_problems.append((firstNum, operator, secondNum)) #3-Tuple

  # Step 2: Arrange the problems
  firstLine = []
  secondLine = []
  dashLine = []
  answerLine = []

  #This is arranging per individual problem
  for firstNum, operator, secondNum in arranged_problems:
    width = max(len(firstNum), len(secondNum)) + 2 #As according to rule
    firstLine.append(firstNum.rjust(width)) #White space 
    secondLine.append(operator + secondNum.rjust(width - 1, ' ')) #Fillchar = ' ' to fill in with whitespace between operand and second number
    dashLine.append('-' * width) #Number of - is according to problem length
    #Optional calculation for answer
    if show_Answers:
      answer = str(eval(firstNum + operator + secondNum)) #Directly parse and calculate result, make it back to a String afterwards.
      answerLine.append(answer.rjust(width))


  # Step 3: Display answers optionally
  if show_Answers:
    return '    '.join(firstLine) + '\n' + '    '.join(secondLine) + '\n' + '    '.join(dashLine) + '\n' + '    '.join(answerLine)
  else:
    return '    '.join(firstLine) + '\n' + '    '.join(secondLine) + '\n' + '    '.join(dashLine)
    