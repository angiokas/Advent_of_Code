removexmas_matrix = []
with open('day_4_input', 'r') as file:
    xmas_matrix = file.read().splitlines()

counter = 0

columns = len(xmas_matrix[0])
rows = len(xmas_matrix)

def word_counter(word):
    i = 0
    if (word == "XMAS"):
        print("IT'SA MATCH: ", word)
        i += 1
    if (word == "SAMX"):
        print("IT'SA MATCH: ", word)
        i +=1
    if(i ==0):
        print("nope: ", word)
    return i

def matrix_check_left(matrix,i,j):
    counter = 0
    if(j>=3): # Going left
        left_string = matrix[i][j-3:j+1]
        print("LEFT:")
        counter += word_counter(left_string)

        if(i>=3): # Going left up diagonal
            character_list = (matrix[i][j],
                        matrix[i-1][j-1],
                        matrix[i-2][j-2],
                        matrix[i-3][j-3])
            left_up_string = "".join(character_list)
            print("LEFT UP DIAGONAL:")
            counter += word_counter(left_up_string)

        if(i<=columns - 4): # Going left down diagonal
            character_list = (matrix[i][j],
                        matrix[i+1][j-1],
                        matrix[i+2][j-2],
                        matrix[i+3][j-3])
            left_down_string = "".join(character_list)
            print("LEFT UP DIAGONAL:")
            counter += word_counter(left_down_string)
    return counter

def matrix_check_right(matrix,i,j):
    counter = 0
    if(j<= columns-4): # Going right
        right_string = matrix[i][j:j+4]
        print("RIGHT:")
        counter += word_counter(right_string)

        if(i>=3): # Going right up diagonal
            character_list = (matrix[i][j],
                        matrix[i-1][j+1],
                        matrix[i-2][j+2],
                        matrix[i-3][j+3])
            right_up_string = "".join(character_list)
            print("RIGHT UP DIAGONAL:")
            counter += word_counter(right_up_string)

        if(i<=columns - 4): # Going right down diagonal
            character_list = (matrix[i][j],
                        matrix[i+1][j+1],
                        matrix[i+2][j+2],
                        matrix[i+3][j+3])
            right_down_string = "".join(character_list)
            print("RIGHT DOWN DIAGONAL:")
            counter += word_counter(right_down_string)
    return counter

def matrix_check_up(matrix,i,j):
    counter = 0
    if(i>=3): # Going up
        character_list = (matrix[i][j],
                        matrix[i-1][j],
                        matrix[i-2][j],
                        matrix[i-3][j])
        up_string = "".join(character_list)
        print("UP:")
        counter += word_counter(up_string)
    return counter

def matrix_check_down(matrix, i,j):
    counter = 0
    if(i<=rows - 4): # Going down
        character_list = (matrix[i][j],
                        matrix[i+1][j],
                        matrix[i+2][j],
                        matrix[i+3][j])
        down_string = "".join(character_list)
        print("DOWN:")
        counter += word_counter(down_string)
    return counter

main_counter = 0
for i in range(rows):
    for j in range(columns):
        if(xmas_matrix[i][j] =="X"):
            print("[",i,"]","[",j,"]")
            l = matrix_check_left(xmas_matrix, i,j)
            r = matrix_check_right(xmas_matrix, i,j)
            u = matrix_check_up(xmas_matrix, i,j)
            d = matrix_check_down(xmas_matrix, i,j)
            main_counter += l+r+u+d

print(main_counter)
            