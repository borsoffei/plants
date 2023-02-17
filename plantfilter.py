from plants import Plant
from illnesses import Illness
import csv

list_of_plants = []
list_of_illnesses = []
list_of_symptoms = []


# Чтение файлов со всем
def read_file():
    with open('base_plants.csv', newline='', encoding='utf8') as csvfile:
        temp_plants = list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
        for pl in temp_plants:
            list_of_plants.append(
                Plant(pl[0].lower(), pl[1].lower(), [a.lower() for a in pl[2].split(';')], pl[3], pl[4]))
    with open('base_illnesses.csv', newline='', encoding='utf8') as csvfile:
        temp_ills = list(csv.reader(csvfile, delimiter=',', quotechar='\n'))
        for ill in temp_ills:
            list_of_illnesses.append(
                Illness(ill[0].lower(), [a.lower() for a in ill[1].split(';')], [a.lower() for a in ill[2].split(';')],
                        ill[3], ill[4]))
    for ill in list_of_illnesses:
        for s in ill.get_symptoms():
            if s not in list_of_symptoms:
                list_of_symptoms.append(s)

            # Определение болезни - поиск бокс


def get_plant_by_name(name, short=False):
    if short:
        for plant in list_of_plants:
            if name == plant.get_name():
                return plant
    if name == '':
        return []
    fit_plants_sw = []
    fit_plants_ne = []
    for plant in list_of_plants:
        if name in plant.get_name():
            if plant.get_name().startswith(name):
                fit_plants_sw.append(plant)
            else:
                fit_plants_ne.append(plant)
    fit_plants = sorted(fit_plants_sw, key=lambda x: x.get_name()) + sorted(fit_plants_ne, key=lambda x: x.get_name())
    if len(fit_plants) == 0:
        return None
    # Нужна сортировка, сначала если в начале слово, потом если в конце
    return fit_plants


def get_ill_by_name(name):
    for ill in list_of_illnesses:
        if name == ill.get_name():
            return ill


# Определение болезни - вывод болезней по растению
def get_illness_by_plant(plant):
    fit_ill = []
    for ill in list_of_illnesses:
        if ill.get_plant() == plant:
            fit_ill.append(ill)
    return sorted(fit_ill, key=lambda x: x.get_name())


def get_illness_by_symptoms(symps):
    fit_ill = []
    for ill in list_of_illnesses:
        c = 1
        for symp in symps:
            c *= ill.get_symptoms().count(symp)
        if c != 0:
            fit_ill.append(ill)
    return sorted(fit_ill, key=lambda x: x.get_name())


def get_plant_by_filters(filters):
    fit_plant = []
    for plant in list_of_plants:
        c = 1
        for filt in filters:
            c *= plant.get_filters().count(filt)
        if c != 0:
            fit_plant.append(plant)
    return sorted(fit_plant, key=lambda x: x.get_name())


def get_plant_by_category(cat):
    fit_plants = []
    for plant in list_of_plants:
        if plant.get_category() == cat:
            fit_plants.append(plant)
    return sorted(fit_plants, key=lambda x: x.get_name())


def get_categories():
    cats = []
    for plant in list_of_plants:
        cat = plant.get_category()
        if cat not in cats:
            cats.append(cat)
    return sorted(cats)


def get_plants_filters():
    filters = []
    for plant in list_of_plants:
        for filt in plant.get_filters():
            if filt not in filters:
                filters.append(filt)
    return sorted(filters)


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

# for i in range(5):
#     print(list_of_plants[i].get_all())
# print('---------------------')
# for i in range(5):
#     print(list_of_illnesses[i].get_all())
# print('-----------------------')
# print(list_of_symptoms)
