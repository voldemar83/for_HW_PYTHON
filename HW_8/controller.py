import view
import model

def run():
    view.greeting()
    while True:
        view.menu()
        answer = int(input())
        if answer == 1:
            view.ask_family()
            family = input()
            view.ask_name()
            name = input()
            view.ask_phone()
            phone = input()
            model.add_contact(family, name, phone)
            view.complete()
            view.second_menu()
            second_answer = int(input("Ваш выбор: "))
            if second_answer == 1:
                continue
            else:
                break
        elif answer == 2:
            data = model.read_phonebook()
            view.print_phonebook(data)
            view.second_menu()
            second_answer = int(input("Ваш выбор: "))
            if second_answer == 1:
                continue
            if second_answer == 2:
                break
        elif answer == 3:
            view.ask_find_word()
            sub_string = input()
            finded_line = model.find(sub_string)
            if (finded_line):
                view.print_finded_line(finded_line)
            else:
                view.print_no_finded_line()
            view.second_menu()
            second_answer = int(input("Ваш выбор: "))
            if second_answer == 1:
                continue
            if second_answer == 2:
                break
        elif answer == 4:
            view.change_contact()
            sub_string = input()
            finded_line = model.find(sub_string)
            if (finded_line):
                if (len(finded_line) > 1):
                    view.print_finded_line(finded_line)
                    view.ask_number_of_contact()
                    number_of_contact = int(input())
                else:
                    number_of_contact = 1
                view.print_finded_line(
                    [finded_line[number_of_contact-1]])
                view.menu_of_change_contact()
                answer_menu_of_change_contact = int(input())
                if answer_menu_of_change_contact == 1:
                    view.ask_family()
                    new_family = input()
                    new_line = []
                    new_line.append(new_family)
                    new_line.append(finded_line[number_of_contact-1][1])
                    new_line.append(finded_line[number_of_contact-1][2])
                    model.rewrite_line(
                        finded_line[number_of_contact-1], new_line)
                    view.suссess_result()
                if answer_menu_of_change_contact == 2:
                    view.ask_name()
                    new_name = input()
                    new_line = []
                    new_line.append(finded_line[number_of_contact-1][0])
                    new_line.append(new_name)
                    new_line.append(finded_line[number_of_contact-1][2])
                    model.rewrite_line(
                        finded_line[number_of_contact-1], new_line)
                    view.suссess_result()
                if answer_menu_of_change_contact == 3:
                    view.ask_phone()
                    new_phone = input()
                    new_line = []
                    new_line.append(finded_line[number_of_contact-1][0])
                    new_line.append(finded_line[number_of_contact-1][1])
                    new_line.append(new_phone)
                    model.rewrite_line(
                        finded_line[number_of_contact-1], new_line)
                    view.suссess_result()
                if answer_menu_of_change_contact == 4:
                    pass
            else:
                view.print_no_finded_line()
        elif answer == 5:
            view.delete_contact()
            sub_string = input()
            finded_line = model.find(sub_string)
            if (finded_line):
                if (len(finded_line) > 1):
                    view.print_finded_line(finded_line)
                    view.ask_number_of_contact_to_delete()
                    number_of_contact = int(input())
                else:
                    number_of_contact = 1
                view.print_finded_line(
                    [finded_line[number_of_contact-1]])
                view.delete_menu()
                answer_delete_menu = int(input())
                if answer_delete_menu == 1:
                    model.delete_line(
                        finded_line[number_of_contact-1])
                    view.suссess_result()

            else:
                view.print_no_finded_line()
        else:
            break
    view.bye()