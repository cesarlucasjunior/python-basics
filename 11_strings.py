# strings are similar to arrys, but imutables.

s = 'this is a string'
print(s)
s = "this is a string"
print(s)

print(s[:4]) #slicing
# s[0] = 'j' do not support this reassign
print(s)

#when we change the string, we're creating a new one
s += "!"
print(s)

#converting and sum or appending

val1, val2 = int("123"), int("234")
print(val1 + val2)

val1, val2 = str(123), str(234)
print(val1 + val2)

#ASCII - why not?
print(ord("Y"))

#combining a list of strings in one output

sarray = ['a', 'b', 'c', 'd', 'e']
print("".join(sarray))