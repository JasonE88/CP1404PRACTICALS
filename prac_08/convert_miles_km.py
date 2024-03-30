from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

