name = input('Hello, what is your first name?     ').strip().capitalize()
last_name = input('What is your last name?    ').strip().capitalize()
species = input('What is your species?        ').strip().capitalize()
eye_colour = input('What is your eye colour?       ').strip().capitalize()
hair_colour = input('What is your hair colour?      ').strip().capitalize()

print('Hello' + ' ' + name + ' ' + last_name + ' ' + 'you are a' + ' ' + species + '. ' + 'And you have' + ' ' + eye_colour + ' ' + 'eyes' + ' ' + 'and your colour hair is' + ' ' + hair_colour)

birth_year = input('In what year were you born?     ')

age = 2020 - int(birth_year)
print('That makes you' + ' ' + str(age))
