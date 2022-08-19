phonebook = {
    "Andrey": "+79757647210",
    "Natalia": "+79754297401",
    "Ruslan": "+79757493711",
}


phonebook = dict(
    Andrey = "+79757647210",
    Natalia = "+79754297401",
    Ruslan = "+79757493711"
)


phonebook = {}
phonebook["Andrey"] = '+79754297401'

>>> phonebook["Andrey"]
+79757647210

if "Maria" in phonebook:
    print(phonebook["Maria"])

>> > phonebook.get("Maria")
>> > phonebook.get("Maria", "такого контакта в книге нет")
'такого контакта в книге нет'

# Удаление
>>> del phonebook["Maria"]
>>> phonebook["Maria"]
KeyError: 'Maria'

>>> phonebook.pop("Maria", None)
>>> phonebook.pop("Maria", "не получилось удалить")
'не получилось удалить'

>>> del phonebook
>>> phonebook
NameError: name 'phonebook' is not defined

# Количество пар ключ-значение в словаре
>>> len(phonebook)
3

phonebook = {
    "Andrey": "+79757647210",
    "Natalia": "+79754297401",
    "Ruslan": "+79757493711",
    "Diana": "+79758990112"
}

for name, phone in phonebook.items()   #Перебираются пары значений
    print(name, phone)

# Andrey +79757647210
# Natalia +79754297401
# Ruslan +79757493711
# Diana +79758990112

>>> list(phonebook.keys())
['Andrey', 'Natalia', 'Ruslan', 'Diana']



phonebook_1 = {
    "Andrey": "+79757647210",
    "Natalia": "+7971111111",
}

phonebook_2 = {
    "Natalia": "+7972222222",
    "Ruslan": "+79757493711"
}

phonebook_1.update(phonebook_2)
phonebook_1
# {'Andrey': '+79757647210', 'Natalia': '+7972222222', 'Ruslan': '+79757493711'}

