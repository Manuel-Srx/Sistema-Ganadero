from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, DictProperty

# Tamaño de la ventana (opcional)
Window.size = (900, 600)

# -------------------------
# CLASES DE PANTALLAS
# -------------------------

class MenuScreen(Screen):
    pass


class InventarioScreen(Screen):
    razas = ListProperty(["Holstein", "Angus", "Brahman"])

    def cambiar_salud(self, estado):
        """Habilita o deshabilita la observación si el animal está enfermo"""
        if estado == "Enferma":
            self.ids.obs_input.disabled = False
        else:
            self.ids.obs_input.disabled = True
            self.ids.obs_input.text = ""

    def agregar_animal(self):
        nombre = self.ids.nombre_input.text.strip()
        raza_nueva = self.ids.raza_input.text.strip()
        raza_sel = self.ids.raza_spinner.text.strip()
        edad = self.ids.edad_input.text.strip()
        peso = self.ids.peso_input.text.strip()
        sexo = self.ids.sexo_spinner.text.strip()
        fecha = self.ids.fecha_input.text.strip()
        salud = self.ids.salud_spinner.text.strip()
        obs = self.ids.obs_input.text.strip()

        if not nombre:
            print("⚠️ Debes ingresar al menos el nombre del animal.")
            return

        if raza_nueva and raza_nueva not in self.razas:
            self.razas.append(raza_nueva)
            self.ids.raza_spinner.values = self.razas

        texto = f"{nombre} | {raza_nueva or raza_sel} | {sexo} | {salud} | {peso} kg"
        self.ids.rv_animales.data.append({"text": texto})

        for campo in ["nombre_input", "raza_input", "edad_input", "peso_input", "fecha_input", "obs_input"]:
            self.ids[campo].text = ""
        self.ids.salud_spinner.text = "Seleccione estado"
        self.ids.sexo_spinner.text = "Seleccione sexo"
        self.ids.raza_spinner.text = "Seleccionar raza"
        self.ids.obs_input.disabled = True


# -------------------------
# MÓDULO VETERINARIO TIPO IA
# -------------------------


class VeterinariaScreen(Screen):

    # Lista de síntomas para el Spinner
    lista_sintomas = ListProperty([
        "Fiebre",
        "Diarrea",
        "Tos",
        "Secreción nasal",
        "Pérdida de apetito",
        "Cojeo",
        "Vómito",
        "Decaimiento"
    ])

    # Síntomas seleccionados por el usuario
    sintomas_seleccionados = ListProperty([])

    # Base de reglas de IA simple (enfermedad -> síntomas requeridos)
    base_conocimiento = DictProperty({
        "Fiebre aftosa": ["Fiebre", "Secreción nasal", "Decaimiento"],
        "Parasitosis": ["Diarrea", "Pérdida de apetito"],
        "Neumonía": ["Tos", "Fiebre", "Secreción nasal"],
        "Problema podal": ["Cojeo"]
    })

    # Medicamentos según enfermedad
    medicamentos = DictProperty({
        "Fiebre aftosa": ("Flunixin", "2 ml / 50kg", "3 días"),
        "Parasitosis": ("Ivermectina", "1 ml / 50kg", "1 día"),
        "Neumonía": ("Oxitetra", "5 ml / 50kg", "5 días"),
        "Problema podal": ("Ketoprofeno", "3 ml / 50kg", "3 días"),
    })

    def agregar_sintoma(self, sintoma):
        if sintoma not in self.sintomas_seleccionados and sintoma != "Seleccionar":
            self.sintomas_seleccionados.append(sintoma)
            print("Síntomas actuales:", self.sintomas_seleccionados)

    def generar_diagnostico(self):
        sintomas = set(self.sintomas_seleccionados)
        diagnostico = "No identificado"

        for enfermedad, req_sintomas in self.base_conocimiento.items():
            if sintomas.intersection(req_sintomas):
                diagnostico = enfermedad
                break

        self.ids.diagnostico_input.text = diagnostico

        if diagnostico in self.medicamentos:
            med, dosis, dias = self.medicamentos[diagnostico]
            self.ids.medicamento_input.text = med
            self.ids.dosis_input.text = dosis
            self.ids.dias_input.text = dias
        else:
            self.ids.medicamento_input.text = ""
            self.ids.dosis_input.text = ""
            self.ids.dias_input.text = ""

    def guardar_tratamiento(self):
        print("Tratamiento guardado correctamente (aquí va tu inserción SQL)")


# -------------------------
# GESTOR DE PANTALLAS
# -------------------------

class WindowManager(ScreenManager):
    pass


# -------------------------
# APLICACIÓN PRINCIPAL
# -------------------------

class SistemaGanaderoApp(App):
    def build(self):
        Builder.load_file("kv/main.kv")
        sm = WindowManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(InventarioScreen(name="inventario"))
        sm.add_widget(VeterinariaScreen(name="veterinaria"))
        sm.current = "menu"
        return sm


if __name__ == "__main__":
    SistemaGanaderoApp().run()
