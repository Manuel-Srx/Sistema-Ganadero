from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

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

        # Si no se llena el nombre, no agrega
        if not nombre:
            print("⚠️ Debes ingresar al menos el nombre del animal.")
            return

        # Guarda la nueva raza si no existe
        if raza_nueva and raza_nueva not in self.razas:
            self.razas.append(raza_nueva)
            self.ids.raza_spinner.values = self.razas

        # Muestra en lista
        texto = f"{nombre} | {raza_nueva or raza_sel} | {sexo} | {salud} | {peso} kg"
        self.ids.rv_animales.data.append({"text": texto})

        # Limpia campos
        for campo in ["nombre_input", "raza_input", "edad_input", "peso_input", "fecha_input", "obs_input"]:
            self.ids[campo].text = ""
        self.ids.salud_spinner.text = "Seleccione estado"
        self.ids.sexo_spinner.text = "Seleccione sexo"
        self.ids.raza_spinner.text = "Seleccionar raza"
        self.ids.obs_input.disabled = True


from db_manager import conectar, agregar_tratamiento, obtener_tratamientos

class VeterinariaScreen(Screen):
    pass

class VeterinariaScreen(Screen):
    animales = {
        "QR001": {"nombre": "Luna", "raza": "Holstein"},
        "QR002": {"nombre": "Toro", "raza": "Brahman"},
        "QR003": {"nombre": "Nube", "raza": "Angus"}
    }

    def buscar_por_qr(self, codigo):
        """Simula lectura de QR y autocompleta datos"""
        if codigo in self.animales:
            self.ids.nombre_input.text = self.animales[codigo]["nombre"]
            self.ids.raza_input.text = self.animales[codigo]["raza"]
        else:
            self.ids.nombre_input.text = ""
            self.ids.raza_input.text = ""
            self.ids.diagnostico_input.text = ""
            self.ids.medicamento_input.text = ""
            self.ids.dosis_input.text = ""
            self.ids.duracion_input.text = ""

    def generar_diagnostico(self):
        """Analiza síntomas y sugiere diagnóstico y tratamiento"""
        sintomas = self.ids.sintomas_input.text.lower()

        if not sintomas.strip():
            self.ids.diagnostico_input.text = "Ingrese síntomas para analizar."
            return

        if "tos" in sintomas or "respira" in sintomas:
            diag, med, dosis, dias = "Infección respiratoria", "Oxitetra", "10 ml", "5 días"
        elif "cojea" in sintomas or "pata" in sintomas:
            diag, med, dosis, dias = "Lesión muscular", "Meloxicam", "5 ml", "3 días"
        elif "diarrea" in sintomas or "vientre" in sintomas:
            diag, med, dosis, dias = "Problemas digestivos", "Florfenicol", "8 ml", "4 días"
        else:
            diag, med, dosis, dias = "Sin diagnóstico definido", "—", "—", "—"

        self.ids.diagnostico_input.text = diag
        self.ids.medicamento_input.text = med
        self.ids.dosis_input.text = dosis
        self.ids.duracion_input.text = dias

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
        sm.add_widget(VeterinariaScreen(name="veterinaria"))  # 👈 IMPORTANTE
        sm.current = "menu"
        return sm


if __name__ == "__main__":
    SistemaGanaderoApp().run()
