input_string = input("Nhập vào một chuỗi ký tự: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Số lần xuất hiện của từng ký tự trong chuỗi:")
for char, count in char_count.items():
    print(f"{char}: {count}")
