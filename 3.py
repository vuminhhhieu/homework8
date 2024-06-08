number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
numbers_dict = {}
for i, roman_numeral in enumerate(number_list, start=1):
    numbers_dict[roman_numeral] = i
roman_number = input("Nhập một số La Mã từ I đến XX: ")
arabic_number = numbers_dict.get(roman_number.upper(), "Not found")
print(arabic_number)
