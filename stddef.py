# import stddic
import pandas as pd
import json

f = open('stddic.json', )
data = json.load(f)


def errorprint():
    print('invalid input. try again!')
    # main.main()


def exitt():
    print('Have a nice day')


def student_details():

    df = pd.DataFrame(data).T
    df.fillna(0, inplace=True)
    print(df)
    # main.main()


def insert_student():
    stdk = []
    enlist = []
    for i in data.values():
        enlist.append(i['enrollment'])
    # stu_key = str(len(data)+1)
    for i in data.keys():
        # print(i)
        stdk.append(int(i))
    stu_key = str(stdk[-1] + 1)
    en = input('enrollment num: ')
    if en.isdigit() and en not in enlist:
        name = input('name of student: ')
        if name.isalpha():
            dep = input('name of department: ')
            if dep.isalpha():
                city = input('name of city: ')
                if city.isalpha():
                    data[stu_key] = {}
                    data[stu_key]['enrollment'] = en
                    data[stu_key]['name'] = name
                    data[stu_key]['department'] = dep
                    data[stu_key]['city'] = city
                    # print(students)
                    print('student added')
                    # main.main()
                else:
                    print('invalid input')
                    insert_student()
            else:
                print('invalid input')
                insert_student()
        else:
            print('invalid input')
            insert_student()
    else:
        print('invalid input')
        insert_student()
    json_object = json.dumps(data, indent=4)
    with open("stddic.json", "w") as outfile:
        outfile.write(json_object)


def update_student():
    enlist = []
    ch = []
    for i, j in data.items():
        print(i, j)
        ch.append(i)
    ask = input('enter number: ')
    if ask in ch:
        en = input('enrollment num: ')
        for i, j in data.items():
            if i != ask:
                enlist.append(j['enrollment'])
        if en.isdigit() and en not in enlist:
            name = input('name of student: ')
            if name.isalpha():
                dep = input('name of department: ')
                if dep.isalpha():
                    city = input('name of city: ')
                    if city.isalpha():
                        data[ask]['enrollment'] = en
                        data[ask]['name'] = name
                        data[ask]['department'] = dep
                        data[ask]['city'] = city
                        # print(students)
                        print('student update successfully')
                        # main.main()
                    else:
                        print('invalid input')
                        update_student()
                else:
                    print('invalid input')
                    update_student()
            else:
                print('invalid input')
                update_student()
        else:
            print('invalid input')
            update_student()
    else:
        print('invalid input')
        update_student()
    json_object = json.dumps(data, indent=4)
    with open("stddic.json", "w") as outfile:
        outfile.write(json_object)


def delete_student():
    for i, j in data.items():
        print(i, j)
    ask = input('enter number: ')
    if ask in data:
        print(data[ask])
        check = input('are you sure to delete this student? [y/n]: ').lower()
        if check == 'y':
            del data[ask]
            print(f'student is deleted')
            # main.main()
        elif check == 'n':
            print(f'student is not deleted')
            # main.main()
        else:
            errorprint()
    else:
        print("student details doesn't match")
        # main.main()
    json_object = json.dumps(data, indent=4)
    with open("stddic.json", "w") as outfile:
        outfile.write(json_object)


def search():
    opt = input('search by enrollment/department/city/name: ')
    if opt == 'name' or opt == 'enrollment' or opt == 'city' or opt == 'department':
        en = input(f'enter {opt}: ')
        for i in data.values():
            if en in i[opt]:
                print(i)
            # else:
            #     print('no data found')
        # main.main()
    else:
        errorprint()


def sorting():
    xyz = input('sort by name/department/city/enrollment: ')
    dd = input('a - ascending and d - descending: ')
    if xyz == 'name' and dd == 'a':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['name'])}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'enrollment' and dd == 'a':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['enrollment'])}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'department' and dd == 'a':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['department'])}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'city' and dd == 'a':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['city'])}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'name' and dd == 'd':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['name'], reverse=True)}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'enrollment' and dd == 'd':
        sorted_dict = {k: v for k, v in
                       sorted(data.items(), key=lambda item: item[1]['enrollment'], reverse=True)}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'department' and dd == 'd':
        sorted_dict = {k: v for k, v in
                       sorted(data.items(), key=lambda item: item[1]['department'], reverse=True)}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    elif xyz == 'city' and dd == 'd':
        sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['city'], reverse=True)}
        for i in sorted_dict.values():
            print(i)
        # main.main()
    else:
        errorprint()


f.close()
