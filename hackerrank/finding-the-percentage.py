def calc_average(grades):
    return sum(grades) / len(grades)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('{0:.2f}'.format(calc_average(student_marks[query_name])))
