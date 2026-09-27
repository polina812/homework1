words = ["кот", "пёс", "кот", "кот", "ёж", "пёс", "кот"]

groups = {}  #создаем словарь 
for w in words:   
    key = w
    if key not in groups:
        groups[key] = 1
    else: groups[key] += 1
    
groups = dict(sorted(groups.items(), key = lambda item: -item[1]))   #сортируем по уменьшению словарь

n = 0 #выводим топ-3 самых частых слов с нумерацией
for name, col in groups.items():
    n += 1
    if n<=3: print(f"{n}. {name} - {col}")


