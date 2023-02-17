from kivy.animation import Animation
from kivymd.uix.chip import MDChip
from kivy.clock import Clock


class MyChip(MDChip):
    # icon_check_color = (0, 0, 0, 1)
    # text_color = (0, 0, 0, 0.5)
    _no_ripple_effect = False
    icon = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.set_chip_bg_color)
        self.bind(active=self.set_chip_text_color)
        self.md_bg_color = '#D5E7DB'
        self.text_color = '#161E1C'

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            Clock.schedule_once(self.set_active, .05)
            return True
        return super().on_touch_down(touch)

    def set_active(self, dt):
        self.active = not self.active

    def set_chip_bg_color(self, instance_chip, active_value: int):
        '''
        Will be called every time the chip is activated/deactivated.
        Sets the background color of the chip.
        '''

        if active_value:
            self.md_bg_color = '#0E6956'
            # self.text_color = '#EAEFEE'
        else:
            self.md_bg_color = '#D5E7DB'
            # self.text_color = '#161E1C'
        # self.md_bg_color = (
        #     (0, 0, 0, 0.4)
        #     if active_value
        #     else (
        #         self.theme_cls.bg_darkest
        #         if self.theme_cls.theme_style == "Light"
        #         else (
        #             self.theme_cls.bg_light
        #             if not self.disabled
        #             else self.theme_cls.disabled_hint_text_color
        #         )
        #     )
        # )

    def set_chip_text_color(self, instance_chip, active_value: int):
        Animation(
            color=(234/255, 239/255, 238/255, 1) if active_value else (22/255, 30/255, 28/255, 1), d=0.2
        ).start(self.ids.label)
