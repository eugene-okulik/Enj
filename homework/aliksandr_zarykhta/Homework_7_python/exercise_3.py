def sum_result(text):
    return int((text)[(text).index(":") + 2:]) + 10


result_of_1 = 'результат операции: 42'
result_of_2 = 'результат операции: 54'
result_of_prog = 'результат работы программы: 209'
result_of_smt = 'результат: 2'

print(sum_result(result_of_1))
print(sum_result(result_of_2))
print(sum_result(result_of_prog))
print(sum_result(result_of_smt))
