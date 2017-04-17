# variables
fruit = "Apple"
first_char = fruit[0]
print (first_char)

fruit2 = "OrangE"
last_char = fruit2[5]
char2 = fruit2[0]
print (last_char)
print (first_char,last_char)

country = "India"
char = country[0]
print (first_char,last_char,char,char2)

#printing Length

india_len = len(country)
apple_len = len(fruit)
orange_len = len(fruit2)
print ("the length of country:"+country)
print (india_len , apple_len, orange_len)

#print lower case and upper case

print (fruit.lower())
print (fruit2.lower())
print (country.upper())

# * will repeat string, and + will concat line

print ("-" * 20)

print (fruit + " " + fruit2 + " "+ "grows in "+ country+ " " +".")

print ("-" * 30)

version = 3
print ("I love Python " + str(version)+ ".")

  
