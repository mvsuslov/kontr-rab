def filter_short_strings(input_array):
    # Создаем пустой массив для хранения строк с длиной <= 3 символа
    output_array = []
    
    # Перебираем все строки в исходном массиве
    for string in input_array:
        # Если длина строки <= 3, добавляем её в выходной массив
        if len(string) <= 3:
            output_array.append(string)
    
    return output_array

# Пример использования
input_array1 = ["Hello", "2", "world", ":-)"]
input_array2 = ["1234", "1567", "-2", "computer science"]
input_array3 = ["Russia", "Denmark", "Kazan"]

print(filter_short_strings(input_array1))  # Output: ["2", ":-)"]
print(filter_short_strings(input_array2))  # Output: ["-2"]
print(filter_short_strings(input_array3))  # Output: []
