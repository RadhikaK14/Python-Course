#3a
float_var = 8.98
int_var = 4
string_var = 'Jam'

#3b
print(hash(float_var))
#hash encodes data into unrecognisable value. NOTE: Doesn't work on Int type

print(round(pow(float_var, 3)))
#returns power of the number. 8.98 to the power 3 = 724.1507920000001
#round returns 724

print(f"is_integer method on float: {float_var.is_integer()}")
# returns True if float is an integer

print(divmod(int_var, 2))
#divmod(divident, divisor). Output: (2,0) - (quotient,remainder)

print(f"conjugate method on int: {int_var.conjugate()}")
# returns the complex conjugate of any in

print(string_var.casefold())
#same as lower. returns a string coverting all the characters to lower. More powerful than lower.

print(string_var.swapcase())
# returns string converting all upper cases to lower and vice versa

print(string_var.strip('a'))
#Removes only the leading and trailing characters. space is the default leading char to remove.

print(string_var.istitle())
#Returns TRUE if all the words starts with upper case and the rest of the word in lower case. Else FALSE