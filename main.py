from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from db_manager import conectar

# --- Pantallas ---
class MenuScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        self.title = "Sistema Ganadero"
        conectar()  # Inicializa la base de datos
        # Cargar el archivo KV después de definir las clases
        return Builder.load_file("kv/main.kv")

if __name__ == "__main__":
    MainApp().run()
