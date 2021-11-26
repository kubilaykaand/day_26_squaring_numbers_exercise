numbers= [1,1,2,3,5,8,13,21,34,55]

squared_numbers=[number*number for number in numbers]

#code for picking the even numbers
even_numbers=[number for number in numbers if number%2==0]

print(squared_numbers)

print(even_numbers)