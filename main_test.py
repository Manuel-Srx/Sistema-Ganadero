# main_test.py (cópialo COMPLETO y reemplaza el anterior)
from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
#:import OneLineIconListItem kivymd.uix.list.OneLineIconListItem
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget

MDScreen:

    MDNavigationLayout:

        ScreenManager:
            MDScreen:
                name: "home"

                MDTopAppBar:
                    title: "Sistema Ganadero"
                    elevation: 4
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                BoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: "Pantalla Principal"
                        halign: "center"
                        pos_hint: {"center_y": .6}
                    MDRaisedButton:
                        text: "Probar botón"
                        pos_hint: {"center_x": .5}
                        on_release: app.test_action()

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: "vertical"
                spacing: "12dp"
                padding: "12dp"

                MDLabel:
                    text: "Menú"
                    font_style: "H5"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Inicio"
                            on_release:
                                nav_drawer.set_state("close")
                                app.change_screen("home")
                            IconLeftWidget:
                                icon: "home"

                        OneLineIconListItem:
                            text: "Inventario"
                            on_release:
                                nav_drawer.set_state("close")
                                app.change_screen("inventario")
                            IconLeftWidget:
                                icon: "cow"

                        OneLineIconListItem:
                            text: "Reportes"
                            on_release:
                                nav_drawer.set_state("close")
                                app.change_screen("reportes")
                            IconLeftWidget:
                                icon: "file-chart"

                        OneLineIconListItem:
                            text: "Configuración"
                            on_release:
                                nav_drawer.set_state("close")
                                app.change_screen("config")
                            IconLeftWidget:
                                icon: "cog"

        # Pantallas "placeholder" adicionales para navegación (se definen como MDScreen)
        MDScreen:
            name: "inventario"
            MDLabel:
                text: "Inventario (pantalla de prueba)"
                halign: "center"

        MDScreen:
            name: "reportes"
            MDLabel:
                text: "Reportes (pantalla de prueba)"
                halign: "center"

        MDScreen:
            name: "config"
            MDLabel:
                text: "Configuración (pantalla de prueba)"
                halign: "center"
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def test_action(self):
        print("Botón probado — la app responde.")

    def change_screen(self, name):
        # obtener screen manager y cambiar pantalla
        sm = self.root.ids.get("nav_drawer").parent.ids.get("screen_manager") if False else None
        # alternativa segura: recorrer widgets hasta encontrar ScreenManager
        for child in self.root.walk():
            from kivy.uix.screenmanager import ScreenManager
            if isinstance(child, ScreenManager):
                child.current = name
                return
        print("No se encontró ScreenManager para cambiar pantalla.")

MainApp().run()
