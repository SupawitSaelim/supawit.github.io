from unittest import result


def main():
    i = open('text.txt', 'r')
    
    readdata = i.readline()

    while readdata != '':
        print(readdata.rstrip('\n'))
        readdata = i.readline()

main()

print('\n\n\n')