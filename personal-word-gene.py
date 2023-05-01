import itertools

full_name = input("Enter full name: ")
place_of_birth = input("Enter place of birth: ")
age = input("Enter age: ")
gender = input("Enter gender: ")
nationality = input("Enter nationality: ")
occupation = input("Enter occupation: ")
education = input("Enter education: ")
phone_number = input("Enter phone number: ")
email = input("Enter email address: ")
spouse = input("Enter spouse's name: ")
children = input("Enter children's names: ")
number = input("Enter any Numbers you want to enter: ")

# create a list of personal details
personal_details = [full_name,place_of_birth,age,gender,nationality,occupation,education,phone_number,email,spouse,children,number]
permutations = itertools.permutations(personal_details)
with open("personal_wordlist.txt", "w") as f:
    for permutation in permutations:
        f.write("".join(permutation) + "\n")
