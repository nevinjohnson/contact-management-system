import json

def add_person():
    name = input('Name: ')
    age = input('Age: ')
    email = input('Email: ')

    person={'name' : name,'age' : age, 'email' : email} 
    people.append(person)
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i+1,'-',person['name'],'|',person['age'],'|',person['email'])
    
def delete_contact(people):
    display_people(people)

    while True:
        number = input('Enter a number to delete: ')
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print('Invalid number,out of range')
            else:
                break
        except:
            print('Invalid number')
    people.pop(number - 1)
    print('Contact Deleted.')

def search(people):
    search_name = input('Search for a name: ').lower()
    results = []

    for person in people:
        name = person['name']
        if search_name in name.lower():
            results.append(person)
    display_people(results)

print('Welcome to the contact management system.')
print()

try:
    with open("./contacts.json","r") as f:
        people = json.load(f)['contacts']

except(FileNotFoundError,json.JSONDecodeError):
    people = []

print(people)
while True:
    print()
    command = input("You can 'Add','Delete' or 'Search' & 'Q' to Quit: ").lower()
    print()

    if command == 'add':
        person = add_person()
        print('Contact Added')
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search(people)
    elif command == 'q':
        break
    else:
        print('Invalid Command.')

print(people)

with open('./contacts.json','w') as f:
    people = json.dump({'contacts':people},f, indent = 4)

    