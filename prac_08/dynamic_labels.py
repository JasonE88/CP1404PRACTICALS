from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    names = ["Jason", "Ralph", "Charlie", "Dexter", "Wilson"]

    def build(self):

