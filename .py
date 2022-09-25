def main():
    i = input('Enter file name to read: ')

    try:
        fileread = open(i, 'r')
        sum = 0

        for i in fileread:
            sum += int(i)
        fileread.close()
    except Exception as e:
        print(e)
        exit()
    else:
        print(sum)
    finally:
        print('Done!!!')    

main()
