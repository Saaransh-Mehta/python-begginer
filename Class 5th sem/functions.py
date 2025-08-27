matrix = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
primary_sum = 0
secondary_sum = 0
total_sum = 0
rows = len(matrix)
columns = len(matrix[0])
for i in range(rows):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][columns - i - 1]

total_sum = primary_sum + secondary_sum

if len(matrix) % 2 == 1:
    total_sum -= matrix[rows//2][columns//2]

print(total_sum)
