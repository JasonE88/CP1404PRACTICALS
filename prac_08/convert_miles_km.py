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

    def handle_calculate(self, text):
        """Handle calculation when the text input changes."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, value):
        """Handle Up/Down button press to adjust miles number."""
        miles = self.convert_to_number(self.root.ids.input_miles.text) + value
        self.root.ids.input_miles.text = str(miles)
        self.update_result(miles)

    def update_result(self, miles):
        """Update the output label with the conversion result."""
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or return 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    MilesConverterApp().run()