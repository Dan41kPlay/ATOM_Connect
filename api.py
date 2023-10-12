from dataclasses import dataclass


@dataclass
class Car:
    mirrors_folded: bool = True
    seat_position: float = 0.5
    backlight_mode: int = 0
    windows_heated: bool = False
    chair_position: float = 0.5
    music_on: bool = False
    trunk_open: bool = False
    hood_open: bool = False
    headlights_on: bool = False
    seats_heated: bool = False
    car_open: bool = False
    thermoregulation_on = False

    def change_mirrors(self):
        self.mirrors_folded = not self.mirrors_folded

    def seat_forward(self):
        self.seat_position += 0.1

    def seat_backward(self):
        self.seat_position -= 0.1

    def set_backlight(self):
        self.backlight_mode += 1
        self.backlight_mode %= 16

    def change_windows(self):
        self.windows_heated = not self.windows_heated

    def chair_forward(self):
        self.chair_position += 0.1

    def chair_backward(self):
        self.chair_position -= 0.1

    def change_music(self):
        self.music_on = not self.music_on

    def change_trunk(self):
        self.trunk_open = not self.trunk_open

    def change_hood(self):
        self.hood_open = not self.hood_open

    def change_headlights(self):
        self.headlights_on = not self.headlights_on

    def change_seat_heating(self):
        self.seats_heated = not self.seats_heated

    def change_car(self):
        self.car_open = not self.car_open

    def change_thermoregulation(self):
        self.thermoregulation_on = not self.thermoregulation_on

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, name, value):
        setattr(self, name, value)
