a = 'H'
b = 'E'
c = 'L'
d = 'L'
e = 'O'
f = ' '
g = 'W'
h = 'O'
i = 'R'
j = 'L'
k = 'D'
all_letters_that_were_above_the_line_that_declared_this_array = [a, b, c, d, e, f, g, h, i, j, k]
def make_all_the_letters_that_were_in_an_array_into_one_string(the_array_with_all_the_letters):
    if not the_array_with_all_the_letters:
        return ""
    new_variable = the_array_with_all_the_letters.pop(0)
    if not the_array_with_all_the_letters:
        return new_variable
    new_variable_two = the_array_with_all_the_letters.pop(-1)
    return new_variable + make_all_the_letters_that_were_in_an_array_into_one_string(the_array_with_all_the_letters) + new_variable_two
print(make_all_the_letters_that_were_in_an_array_into_one_string(all_letters_that_were_above_the_line_that_declared_this_array).lower())