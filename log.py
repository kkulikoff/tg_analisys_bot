def write_log(text, name, n_time):
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(f'{n_time}: {name}: {text} \n')
    f.close()
