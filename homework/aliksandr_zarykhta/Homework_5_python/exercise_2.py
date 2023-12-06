result_of_1 = 'результат операции: 42'
result_of_2 = 'результат операции: 514'
result_of_prog = 'результат работы программы: 9'

sum_of_res1 = 10 + int(result_of_1[result_of_1.index(":") + 2:])
sum_of_res2 = 10 + int(result_of_2[result_of_2.index(":") + 2:])
sum_of_prog = 10 + int(result_of_prog[result_of_prog.index(":") + 2:])
print(sum_of_res1, sum_of_res2, sum_of_prog, sep='\n')
