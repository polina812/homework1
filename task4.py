lecture = ["Аня", "Борис", "Вика", "Гоша", "Аня"]
seminar = ["Вика", "Дима", "Борис", "Ева"]

lecture = sorted(list(set(lecture)))
seminar = sorted(list(set(seminar)))
together = sorted(list(set(lecture + seminar)))
vce = []
lec = []

for l in lecture:
    if l in seminar: vce.append(l)
    else: lec.append(l)
        
print(f"Всего уникальных студентов: {len(together)}")
print(f"На обеих парах: {vce}")
print(f"Только на лекции: {lec}")
print(f"Хотя бы на одной: {together}")

