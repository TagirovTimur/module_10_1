from time import sleep
from datetime import datetime
from threading import Thread
time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='UTF-8') as file:
        for i in range(1,word_count + 1):
            file.write(f"Какое-то слово № {i}")
            file.write('\n')
            sleep(0.1)
    print (f"Завершилась запись в файл {file_name}")

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

start_func = datetime.now()

thr_first = Thread(target=write_words, args =(10, 'example5.txt'))
thr_second = Thread(target=write_words, args =(30, 'example6.txt'))
thr_third = Thread(target=write_words, args =(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args =(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_func = datetime.now()
res_func = end_func - start_func
print(f'Работа потоков {res_func}')