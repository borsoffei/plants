from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.text import LabelBase
from kivymd.uix.tab import MDTabsBase
from ctypes import windll, c_int64
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

import plantfilter
from FindScreen import FindScreen
from DictionaryScreen import DictionaryScreen

import os, sys
from kivy.resources import resource_add_path, resource_find

class IllScreen(Screen):
    pass


class PlantScreen(Screen):
    pass


class MD3Card(MDCard):
    text = StringProperty()
    plant_or_ill = StringProperty()
    image_path = StringProperty()


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MyMainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window_size_x = 1440
        self.window_size_y = 900
        self.sm_main = ScreenManager()
        self.current_tab = 'one'
        self.tab_one_state = 'find'
        self.tab_two_state = 'dictionary'
        

        self.colors = {'aquamarine': '#30BBAC',
                       'ultra_dark_green': '#003128',
                       'white': '#FFFFFF',
                       'pink': '#F5BACC',
                       'light_pink': '#F7C6D5',
                       'dark_green': '#0E6956'}

    def build(self):
        self.theme_cls.material_style = "M3"
        Window.size = (self.window_size_x, self.window_size_y)
        self.title = 'Диагностирование заболеваний'
        return Builder.load_file("main.kv")

    def on_start(self):
        self.find_screen = FindScreen(name="find")
        self.ill_screen = IllScreen(name="ill")
        self.dictionary_screen = DictionaryScreen(name="dictionary")
        self.plant_screen = PlantScreen(name="plant")

        self.sm_main.add_widget(self.find_screen)
        self.sm_main.add_widget(self.ill_screen)
        self.sm_main.add_widget(self.dictionary_screen)
        self.sm_main.add_widget(self.plant_screen)
        self.sm_main.current = "find"

        self.root.add_widget(self.sm_main)

    def open_article(self, instance, touch):
        if instance.collide_point(*touch.pos):
            if instance.plant_or_ill == 'ill':
                self.sm_main.current = 'ill'
                ill = plantfilter.get_ill_by_name(instance.text.lower())
                self.ill_screen.ids.ill_name.text = ill.get_name().capitalize()
                self.ill_screen.ids.ill_image.source = 'photo_illnesses/' + ill.get_photo()
                self.ill_screen.ids.ill_plants.text = ', '.join([i.capitalize() for i in ill.get_plant()])
                self.ill_screen.ids.ill_symptoms.text = ', '.join([i.capitalize() for i in ill.get_symptoms()])
                description = open('data_illnesses/' + ill.get_description(), encoding='UTF8').read()
                self.ill_screen.ids.ill_description.text = description
                self.tab_one_state = 'ill'

            elif instance.plant_or_ill == 'plant':
                self.sm_main.current = 'plant'
                plant = plantfilter.get_plant_by_name(instance.text.lower(), short=True)
                self.plant_screen.ids.plant_name.text = plant.get_name().capitalize()
                self.plant_screen.ids.plant_image.source = 'photo_plants/' + plant.get_photo()
                self.plant_screen.ids.plant_category.text = plant.get_category().capitalize()
                self.plant_screen.ids.plant_filters.text = ', '.join([i.capitalize() for i in plant.get_filters()])
                description = open('data_plants/' + plant.get_description(), encoding='UTF8').read()
                self.plant_screen.ids.plant_description.text = description
                self.tab_two_state = 'plant'

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if self.current_tab == 'one' and tab_text == 'Растения':
            self.sm_main.current = 'dictionary'
            self.current_tab = 'two'
        elif self.current_tab == 'two' and tab_text == 'Поиск Заболевания':
            self.sm_main.current = 'find'
            self.current_tab = 'one'


if __name__ == "__main__":
    windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MyMainApp().run()
