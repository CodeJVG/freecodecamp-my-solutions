def arithmetic_arranger(problems, option=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for problem in problems:
        problem = problem.split()

        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            number = int(problem[0])
            number = int(problem[2])
        except:
            return "Error: Numbers must only contain digits."

        n_space = max(len(problem[0]), len(problem[2])) + 6
        line1 = line1 + " " * (n_space - len(problem[0])) + problem[0]
        line2 = line2 + " " * 4 + problem[1] + " " * (n_space - 5 - len(problem[2])) + problem[2]
        line3 = line3 + " " * 4 + "-" * (n_space - 4)

        if problem[1] == "+":
            result = int(problem[0]) + int(problem[2])
            result = str(result)
            line4 = line4 + " " * (n_space - len(result)) + result
        else:
            result = int(problem[0]) - int(problem[2])
            result = str(result)
            line4 = line4 + " " * (n_space - len(result)) + result

    line1 = line1[4:len(line1)]
    line2 = line2[4:len(line2)]
    line3 = line3[4:len(line3)]
    line4 = line4[4:len(line4)]

    if option is True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3

    return arranged_problems
