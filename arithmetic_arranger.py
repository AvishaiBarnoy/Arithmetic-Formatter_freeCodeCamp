def arithmetic_arranger(problems,solve=False):
  first = []
  second = []
  signs = []
  solutions = None
	# check number of problems
  if len(problems) > 5:
    return 'Error: Too many problems.'
  for problem in problems:
    split_problem = problem.split()
    first.append(split_problem[0])
    second.append(split_problem[2])
    signs.append(split_problem[1])
    # check problem is addition or subtraction
    if split_problem[1] != '+' and split_problem[1] != '-':
      return "Error: Operator must be '+' or '-'."
    # check no numerical in problem
    if split_problem[0].isnumeric() == False or split_problem[2].isnumeric() == False:
      return "Error: Numbers must only contain digits."
    if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
  arranged_problems = ''
  length_numbers = [len(max(problem.split(),key=len)) for problem in problems]
  # Print first line	
  for i,j in enumerate(first):	
    if i == len(first)-1:
      arranged_problems += ' '*(length_numbers[i]-len(j)+2) + j + '\n'
    else:
      arranged_problems += ' '*(length_numbers[i]-len(j)+2) + j + '    '
  # Pring second line
  for i,j in enumerate(second):
    if i == len(second)-1:
      arranged_problems += signs[i] + ' '*(1+abs(len(j)-length_numbers[i])) + j + '\n'
    else:
      arranged_problems += signs[i] + ' '*(1+abs(len(j)-length_numbers[i])) + j + '    '  
  # Print separator
  for i,j in enumerate(length_numbers):
    if i == len(length_numbers) - 1:
      if solve == True:
        arranged_problems += '-'*(j+2) + '\n'
      else:
        arranged_problems += '-'*(j+2)
    else: 
      arranged_problems += '-'*(j+2) + '    '
  # Print solution if asked for
  if solve == True:
    solutions = []
    for i,sign in enumerate(signs):
      intFirst = [int(i) for i in first]
      intSecond = [int(i) for i in second]
      if sign == '-':
        solutions.append(intFirst[i] - intSecond[i])
      if sign == '+':
        solutions.append(intFirst[i] + intSecond[i])
      solutions = [str(i) for i in solutions]
    for i,j in enumerate(solutions):
      if i == len(solutions)-1:
        if int(j) > 0:
          arranged_problems += ' '*(2+len(j)-length_numbers[i]) + j
        elif int(j) < 0:
          arranged_problems += ' '*(1+len(j)-length_numbers[i]) + j
      else:
        if int(j) > 0:
          arranged_problems += ' '*(2+len(j)-length_numbers[i]) + j + '    '
        if int(j) < 0:
          arranged_problems += ' '*(len(j)-length_numbers[i]) + j + '    '
  return arranged_problems
