
import plantfilter
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from MyChip import MyChip


class MD3Card(MDCard):
    text = StringProperty()
    plant_or_ill = StringProperty()
    image_path = StringProperty()


class DictionaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories = plantfilter.get_categories()
        self.filters = plantfilter.get_plants_filters()
        self.selected_options = []
        self.plant = ''
        self.selected_category = ''
        self.create_filters()
        self.create_categories()
        self.current_chip = None
        self.create_cards()

    def create_filters(self):
        for filt in self.filters:
            chip = MyChip(text=filt.capitalize(), on_touch_down=self.update_list)
            self.ids.filter_box.add_widget(chip)

    def create_categories(self):
        for category in self.categories:
            chip = MyChip(text=category.capitalize(), on_touch_down=self.update_chip)
            self.ids.category_box.add_widget(chip)

    def create_cards(self):
        input_plant = self.ids.plant_input.text.lower()
        self.ids.list_plant_box.clear_widgets()
        fit_plants_by_input = plantfilter.get_plant_by_name(input_plant)
        if fit_plants_by_input is not None:
            fit_plants_by_category = plantfilter.get_plant_by_category(self.selected_category)
            fit_plants_by_filts = plantfilter.get_plant_by_filters(self.selected_options)
            plants_to_output = self.list_intersection(fit_plants_by_input, fit_plants_by_category, fit_plants_by_filts)
            if plants_to_output is not None:
                for plant in plants_to_output:
                    card = MD3Card(text=plant.get_name().capitalize(), plant_or_ill='plant',
                                   image_path='photo_plants/' + plant.get_photo())
                    self.ids.list_plant_box.add_widget(card)
                    # card.width = card.parent.width * 0.3

    def list_intersection(self, a, b, c):
        result = []
        if len(a) == 0:
            if len(b) == 0:
                if len(c) == 0:
                    return None
                else:
                    return c
            else:
                if len(c) == 0:
                    return None
                else:
                    for i in b:
                        if i in result:
                            continue
                        for j in c:
                            if i == j:
                                result.append(i)
                                break
                    return result
        else:
            if len(b) == 0:
                if len(c) == 0:
                    return None
                else:
                    for i in a:
                        if i in result:
                            continue
                        for j in c:
                            if i == j:
                                result.append(i)
                                break
                    return result
            else:
                if len(c) == 0:
                    return None
                else:
                    temp = []
                    for i in a:
                        if i in temp:
                            continue
                        for j in b:
                            if i == j:
                                temp.append(i)
                                break
                    for i in temp:
                        if i in result:
                            continue
                        for j in c:
                            if i == j:
                                result.append(i)
                                break
                    return result

    def clear_filters(self):
        for chip in self.ids.filter_box.children:
            if chip.active:
                chip.active = False
                self.selected_options.clear()
                self.create_cards()

    def update_list(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if instance.text.lower() in self.selected_options:
                self.selected_options.remove(instance.text.lower())
            else:
                self.selected_options.append(instance.text.lower())
            self.create_cards()

    def update_chip(self, chip, touch):
        if chip.collide_point(*touch.pos):
            if self.current_chip is None or self.current_chip != chip:
                if self.current_chip:
                    self.current_chip.active = False
                self.current_chip = chip
                self.selected_category = chip.text.lower()
            elif self.current_chip == chip:
                self.current_chip = None
                self.selected_category = ''
            self.create_cards()
