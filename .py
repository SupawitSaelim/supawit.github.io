import pickle as pkl

def main():
    with open('data.dat','rb') as file:
        end_file = False

        while not end_file:
            try:
                data = pkl.load(file)
                display_data(data)
            except EOFError:
                end_file = True

def display_data(data):
    print('Name: ', data['name'])
    print('Age: ', data['age'])
    print('Address: ', data['address'])
    print()

main()
