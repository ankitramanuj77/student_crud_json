import stddef

def main():
    option = input(
        '1 - to show all student details\n2 - to insert student\n3 - to update student info\n4 - to delete student\n5 - search\n6 - sort\n7 - to exit\nenter your choice here: ')
    if option == '7':
        stddef.exitt()
    elif option == '1':
        stddef.student_details()
        # print(stddef.student_details())
        main()
    elif option == '2':
        stddef.insert_student()
        main()
    elif option == '3':
        stddef.update_student()
        main()
    elif option == '4':
        stddef.delete_student()
        main()
    elif option == '5':
        stddef.search()
        main()
    elif option == '6':
        stddef.sorting()
        main()
    else:
        main()

main()
