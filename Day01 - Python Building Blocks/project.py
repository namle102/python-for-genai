print('-'*50)
print('Welcome to User Info Collector!')
print('-'*50)

print('Please provide the following information:\n')
first = input('First Name: ')
last = input('Last Name: ')
age = int(input('Age: '))
email = input('Email: ')
phone = input('Phone: ')
city = input('City: ')
langNums = int(input('Number of programming languages you know: '))
exp = int(input('Years of coding experience: '))
is_student = input('Are you currently a student? (yes/no): ').strip().lower() == 'yes'

print('-'*50)
print('User Information Summary')
print('-'*50)

print(f'Name: {first} {last}')
print(f'Age: {age} years old')
print(f'Birth Year: {2026 - age}' )
print(f'Email: {email}')
print(f'Phone: {phone}')
print(f'City: {city}\n')

print(f'Programming Experience:')
print(f'    Languages Known: {langNums}')
print(f'    Years of Experience: {exp}')
print(f'    Experience Level: {'Advanced' if exp > 4 else 'Intermediate'}')
print(f'    Student Status: {is_student}\n')

print('Message: Keep up the great work!')