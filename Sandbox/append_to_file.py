
filename = 'email_addresses.txt'

with open(filename, mode = 'a') as f:

    while True:
        s = input('Next e-mail address: ')

        if s:
            # f.write(s + '\n')

            print(s, file = f)
        else:
            break

