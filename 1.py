numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
               'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

roman_number = input("Nhập một số La Mã từ I đến X: ")

arabic_number = numbers.get(roman_number.upper(), "Not found")
print(arabic_number)
