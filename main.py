from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


Window.clearcolor = get_color_from_hex('#111625')

# Yeh class tera 3x3 ka board aur game logic sambhalegi
class TicTacToeGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        self.cols = 3
        self.current_player = "X"
        

        for i in range(9):
            btn = Button(
                text="",
                font_size=60,
                bold=True,
                background_normal="", 
                background_color=get_color_from_hex('#111625'),
                color=get_color_from_hex('#00D0F5')
            )

            btn.bind(on_press=self.on_button_click)
            self.add_widget(btn)


    def on_button_click(self, instance):

        if instance.text == "":
            instance.text = self.current_player
            

            if self.current_player == "X":
                instance.color = get_color_from_hex('#00D0F5') # Cyan for X
                self.current_player = "O"
            else:
                instance.color = get_color_from_hex('#A88A34') # Gold for O
                self.current_player = "X"


class TicTacToeApp(App):
    def build(self):
        self.title = "TechFront Tic-Tac-Toe"
        return TicTacToeGrid()


if __name__ == '__main__':
    TicTacToeApp().run()
    