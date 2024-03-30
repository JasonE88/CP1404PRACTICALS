from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    names = ["Jason", "Ralph", "Charlie", "Dexter", "Wilson"]

    def build(self):
        self.title = "Dynamic Labels"
        layout = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name, font_size='24sp', color=(0, 0, 1, 1))
            layout.add_widget(label)
        return layout


if __name__ == "__main__":
    DynamicLabelsApp().run()
