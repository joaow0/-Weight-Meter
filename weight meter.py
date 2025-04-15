people = []
person_data = []
heaviest = lightest = 0

while True:
    person_data.append(str(input('Name: ')))
    person_data.append(int(input('Weight: ')))

    if len(people) == 0:
        heaviest = lightest = person_data[1]
    else:
        if person_data[1] > heaviest:
            heaviest = person_data[1]
        if person_data[1] < lightest:
            lightest = person_data[1]

    people.append(person_data[:])  # Save a copy of current person
    person_data.clear()

    cont = str(input('Do you want to continue? [Y/N] '))
    if cont.lower() == 'n':
        break

print(f'\nTotal people registered: {len(people)}')

print(f'\nHeaviest weight recorded: {heaviest} kg. Person(s): ', end='')
for person in people:
    if person[1] == heaviest:
        print(f'{person[0]}...', end='')

print(f'\nLightest weight recorded: {lightest} kg. Person(s): ', end='')
for person in people:
    if person[1] == lightest:
        print(f'{person[0]}...', end='')

print('\nProgram ended.')