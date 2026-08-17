from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class StudentApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

    self.label = Label(
        text='[b]My Study AI[/b]\nReady for your notes',
        markup=True,
        font_size='24sp',
        halign='center',
    )
    layout.add_widget(self.label)

    self.btn = Button(
        text='Tap to Process PDF',
        size_hint=(1, 0.3),
        background_color=(0.1, 0.5, 0.8, 1),
    )
    self.btn.bind(on_press=self.on_button_click)
    layout.add_widget(self.btn)

    return layout

  def on_button_click(self, instance):
    self.label.text = 'Scanning local storage for PDFs...'


if __name__ == '__main__':
  StudentApp().run()

