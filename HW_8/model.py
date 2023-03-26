

def read_phonebook():
    temp = []
    file = open('file.txt', 'r', encoding='utf-8')
    for line in file.read().split('\n'):
        temp.append(line)
    file.close()
    lst = []
    for i in temp:
        a = i.split()
        lst.append(a)
    return lst[:len(lst)-1]


def add_contact(family, name, phone):
    with open("file.txt", 'a', encoding='utf-8') as file:
        file.write(family+" "+name+" "+phone+"\n")
        file.close()


def find(sub_string):
    data = read_phonebook()
    result = []
    for line in data:
        if sub_string in line:
            result.append(line)
    return (result)


def rewrite_line(initial_line, new_line):
    data = read_phonebook()
    result = []
    for line in data:
        if line == initial_line:
            result.append(new_line)
        else:
            result.append(line)
    with open("file.txt", 'w', encoding='utf-8') as file:
        for line in result:
            for item in line:
                file.write(item+" ")
            file.write("\n")
        file.close()


def delete_line(line_to_delete):
    data = read_phonebook()
    result = []
    for line in data:
        if line != line_to_delete:
            result.append(line)
    with open("file.txt", 'w', encoding='utf-8') as file:
        for line in result:
            for item in line:
                file.write(item+" ")
            file.write("\n")
        file.close()