if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Calculate the average and print it with 2 decimal places
    if query_name in student_marks:
        avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(f"{avg_score:.2f}")