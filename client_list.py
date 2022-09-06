def main():

    names = open("clients.txt", "r")
    i = 1
    for name in names:

        print(str(i) + ". " + name.rstrip('\n'))
        i += 1

main()
    