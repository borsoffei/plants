from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import plantfilter


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.options = plantfilter.get_symptoms_by_categories()
        self.selected_options = []
        self.popups = {}

    def suggestion(self, *args):
        data = self.ids.plant_input.text
        fit_plants = plantfilter.get_plant_by_name(data)
        text = ''
        if fit_plants is None:
            text = 'Такого растения нет в базе'
        else:
            for el in fit_plants:
                print(str(el.get_name()))
                text += str(el.get_name()) + ', '
        self.ids.suggestion_label.text = text.strip(', ')

    def create_buttons(self):
        for popup in self.options.keys():
            btn = Button(text=popup, on_release=self.open_popup)
            self.ids.button_box.add_widget(btn)

    def create_popups(self):
        for popup, options in self.options.items():
            layout = BoxLayout(orientation='vertical')
            for option in options:
                popup_button = Button(text=option, on_release=self.update_list, background_color=(0, 0, 1, 1))
                layout.add_widget(popup_button)
            self.popups[popup] = Popup(title=popup, content=layout, size_hint=(None, None), size=(200, 200),
                                       auto_dismiss=True)

    def open_popup(self, instance):
        self.popups[instance.text].open()

    def update_list(self, instance):
        if instance.text in self.selected_options:
            self.selected_options.remove(instance.text)
        else:
            self.selected_options.append(instance.text)
        self.ids.selected_options_label.text = 'Выбранные симптомы:' + str(self.selected_options).rstrip(']').lstrip(
            '[').replace("'", '')


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mymain.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
