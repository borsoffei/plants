from plants import Plant
from illnesses import Illness
from symptoms import Symptom

list_of_plants = []
list_of_illnesses = []
list_of_symptoms = []


# Чтение файлов со всем
def read_file():
    for i in range(5):
        list_of_plants.append(Plant(str(i * 5), str(i), str(i), str(i), str(i)))
    for k in range(5, 10):
        list_of_illnesses.append(Illness(k, k, k, k, k))
    for j in range(5, 10):
        list_of_symptoms.append(Symptom(j, j))


# Определение болезни - поиск бокс
def get_plant_by_name(name):
    if name == '':
        return []
    fit_plants = []
    for plant in list_of_plants:
        if name in plant.get_name():
            fit_plants.append(plant)
    if len(fit_plants) == 0:
        return None
    return fit_plants


# Определение болезни - вывод болезней по растению
def get_illness_by_plant(plant):
    fit_ill = []
    for ill in list_of_illnesses:
        if ill.get_plant() == plant:
            fit_ill.append(ill)
    return fit_ill


def get_illness_by_symptom(symp):
    fit_symp = []
    for ill in list_of_illnesses:
        ill_s = ill.get_symptoms()
        c = 0
        for s in ill_s:
            if s == symp:
                c += 1
                fit_symp.append([c, ill])
    return fit_symp


def get_plant_by_category(cat):
    fit_plants = []
    for plant in list_of_plants:
        if plant.get_category() == cat:
            fit_plants.append(plant)
    return fit_plants


def get_symptoms_by_categories():
    symptoms_by_categories = {}
    categories = []
    for symp in list_of_symptoms:
        if symp.get_category() not in categories:
            categories.append(symp.get_category())
    for cat in categories:
        temp = []
        for s in list_of_symptoms:
            if cat == s.get_category():
                temp.append(s.get_name())
        symptoms_by_categories[cat] = temp
    return symptoms_by_categories

read_file()