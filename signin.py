from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    pass

class SigninApp():
    def build(self):
        return SigninWindow()

if __name__ == "__mail__":
    sa = SigninApp()
    sa.run() 
