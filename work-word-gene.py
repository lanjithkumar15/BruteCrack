import itertools

comname = input("Enter company name: ")
industry = input("Enter industry: ")
foundyear = input("Enter year founded: ")
headlocation = input("Enter headquarters location: ")
numofemployee = input("Enter number of employees: ")
revenue = input("Enter revenue: ")
file_name = input("Enter file_name: ")
file_year = input("Enter file_year: ")

personal_details = [comname,industry,foundyear,headlocation,numofemployee,revenue,file_name,file_year]
permutations = itertools.permutations(personal_details)
with open("work_wordlist.txt", "w") as f:
    for permutation in permutations:
        f.write("".join(permutation) + "\n") 
