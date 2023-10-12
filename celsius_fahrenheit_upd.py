

# updated: used try/except instead if/else;
# updated logic for conversion
# added elif in case if temp. in Celsius to write it in the new file


# C:\Users\Ksenia.Velkova\PycharmProjects\Temp.txt
file_path = input('Please enter file path: ')
print(file_path)


try:
    with open(file_path, 'r') as f:
        lines = f.read()
        ln = lines.replace('\n', ' ').split(" ")
        for i in ln:
            if 'F' in i:
                t = float((int(i[:-1]) - 32)*(5/9))
                with open('Temp_C.txt', 'a') as n:
                    n.write(f'{t:.2f}C\n')
                print(f'{t:.2f}C\n')
            elif 'C' in i:
                t = (int(i[:-1]))
                with open('Temp_C.txt', 'a') as n:
                    n.write(f'{t:.2f}C\n')
                print(f'{t:.2f}C\n')


except FileNotFoundError:
    print('The file does not exist, please enter the correct file path')