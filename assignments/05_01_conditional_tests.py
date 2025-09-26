#test 1: Equality check
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#test 2: Inequality check
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

#test 3: Equality check with different value
print("\nIs car == 'audi'? I predict False.")
print(car == 'toyota')

#test 4: inequality check with different value
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

#test 5: Greater than check with non-matching values
car='bmw'
print("\nIs car > 'audi'? I predict True.")
print(car > 'mercedes')

#test 6: inequality check with a matching value
print("\nIs car < 'audi'? I predict False.")
print(car < 'tesla')

#test 7: Greater than or equal to check with matching value
print("\nIs car >= 'bmw'? I predict True.")
print(car >= 'bmw') 

#test 8: Less than or equal to check with non-matching value
print("\nIs car <= 'audi'? I predict False.")
print(car <= 'mercedes')

#test 9: Greater than or equal to check with a numeric value
age = 25
print("\nIs age >= 18? I predict True.")
print(age >= 25)

#test 10: inequality check with a numeric value
print("\nIs age < 18? I predict False.")
print(age < 18)