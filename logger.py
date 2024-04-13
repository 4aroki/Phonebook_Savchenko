from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name} \n {surname} \n {phone} \n {adress} \n \n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{adress}\n"
                    f" Выберите вариант: "))

    while var != 1 and var != 2:
        print("неправильный ввод")
        var = int(input('введите число '))

    if var == 1:
        with open('data_first_var.csv', 'a', encoding='utf-8') as f:
                  f.write(f"{name} \n {surname} \n {phone} \n {adress} \n \n")

    elif var == 2:
        with open('data_sec_var.csv', 'a', encoding='utf-8') as f:
                  f.write(f"{name};{surname};{phone};{adress}\n")


def print_data():
    print('вывожу данные из файла 1: \n')
    with open('data_first_var.csv', 'r', encoding='utf-8') as f:
          data_first = f.readlines()
          data_first_list = []
          j = 0
          for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                      data_first_list.append(' '.join(data_first[j:i+1]))
                      j = i
          print(' '.join(data_first_list))

    print('вывожу данные из файла 2: \n')
    with open('data_sec_var.csv', 'r', encoding='utf-8') as f:
          data_second = f.readlines
          print(*data_second)


print_data


# def update_data():
# name = name_data()
# surname = surname_data()


def delete_data():
    file_name = 'data_first_var.csv'
    name = name_data()
    with open(file_name, 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i


        print(data_first_list)
        data_first_list = list(filter(lambda x: not(name) in x, data_first_list))
        print(data_first_list)


    with open(file_name, 'w') as f:
        f.write(''.join(data_first_list))

    

