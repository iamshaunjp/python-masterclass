contacts = []

# CHALLENGE - create an add_contact function to add new contacts to the list
# each contact should be a dictionary with a name and email property

def add_contact():
  return
  

# CHALLENGE - create a list_contacts function to print out all contacts
# each contact should be printed out on a new line with a name & email
# if there are no contacts yet, print out a "no contacts yet" message

def list_contacts():
  return

def main():
  while True:
    print('Press 1 to add a contact, press 2 to list contacts.')
    choice = input('Your choice: ')

    if choice == '1':
      print('You chose option 1.')
      name = input('New contact name: ')
      email = input('New contact email: ')

      add_contact()
      continue

    elif choice == '2':
      print('You chose option 2.')

      list_contacts()
      continue

    else:
      print('Invalid choice. Exiting program.')
      break

if __name__ == "__main__":
    main()