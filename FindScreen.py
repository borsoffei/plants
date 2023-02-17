
import plantfilter
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from MyChip import MyChip


class MD3Card(MDCard):

    text = StringProperty()
    plant_or_ill = StringProperty()
    image_path = StringProperty()


class FindScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.options = plantfilter.list_of_symptoms
        self.selected_options = []
        self.popups = {}
        self.plant = ''
        self.create_symptoms()
        self.create_cards()

    def suggestion(self, *args):
        self.plant = self.ids.plant_input.text.lower()
        fit_plants = plantfilter.get_plant_by_name(self.plant)
        self.ids.suggestion_box.clear_widgets()
        if fit_plants is None:
            self.ids.plant_input.helper_text = 'Такого растения нет в базе'
            self.ids.plant_input.error = True
        else:
            self.ids.plant_input.error = False
            self.ids.plant_input.helper_text = ''
            for el in fit_plants:
                self.ids.suggestion_box.add_widget(
                    MyChip(text=el.get_name().capitalize(), on_touch_down=self.autocomplete))
        self.create_cards()

    def autocomplete(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.ids.plant_input.text = instance.text
            self.create_cards()

    def create_symptoms(self):
        for symp in self.options:
            chip = MyChip(text=symp.capitalize(), on_touch_down=self.update_list)
            self.ids.symp_box.add_widget(chip)

    def clear_filters(self):
        for chip in self.ids.symp_box.children:
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
            print(self.selected_options)


    def create_cards(self):
        fit = plantfilter.get_plant_by_name(self.plant)
        self.ids.list_ill_box.clear_widgets()
        if fit is not None:
            fit_plants = [el.get_name() for el in fit]
            fit_ill_symp = plantfilter.get_illness_by_symptoms(self.selected_options)
            if len(fit_plants) == 0:
                # 'Растение не введено'
                if len(fit_ill_symp) != 0:
                    # 'Растение не введно, симптомы введены'
                    for ill in fit_ill_symp:
                        text = ill.get_name()
                        card = MD3Card(text=text.capitalize(), plant_or_ill='ill', image_path='photo_illnesses/' + ill.get_photo())
                        self.ids.list_ill_box.add_widget(card)
                        # card.width = card.parent.width * 0.3
                elif len(self.selected_options) == 0:
                    # 'Растение и симптомы не введены'
                    for ill in plantfilter.list_of_illnesses:
                        text = ill.get_name()
                        card = MD3Card(text=text.capitalize(), plant_or_ill='ill', image_path='photo_illnesses/' + ill.get_photo())
                        self.ids.list_ill_box.add_widget(card)
                        # card.width = card.parent.width * 0.3
            else:
                # 'Введено растение'
                if len(fit_ill_symp) != 0:
                    # 'Введено растение и симптомы'
                    for ill in fit_ill_symp:
                        for plant in ill.get_plant():
                            if plant in fit_plants:
                                text = ill.get_name()
                                card = MD3Card(text=text.capitalize(), plant_or_ill='ill', image_path='photo_illnesses/' + ill.get_photo())
                                self.ids.list_ill_box.add_widget(card)
                                # card.width = card.parent.width * 0.3
                elif len(self.selected_options) == 0:
                    'Введено растение не введены симптомы'
                    for plant in fit_plants:
                        illnesses = plantfilter.get_illness_by_plant(plant)
                        for ill in illnesses:
                            text = ill.get_name()
                            card = MD3Card(text=text.capitalize(), plant_or_ill='ill', image_path='photo_illnesses/' + ill.get_photo())
                            self.ids.list_ill_box.add_widget(card)
                            # card.width = card.parent.width * 0.3
