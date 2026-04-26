# --- Estilos ---

# Estas son diferentes clases estáticas donde
# se pueden configurar y llamar diferentes propiedades
# fácilmente a través de todo el proyecto


# Se define la clase principal
class Style:
    def __init__(self):
        
        # Tipos de letra
        # Donde la letra mayúscula/minúscula significa el estilo
        # Y el número indica el tamaño
        self.A24 = ("Arial", 24, "bold")
        self.A20 = ("Arial", 20, "bold")
        self.A18 = ("Arial", 18, "bold")
        self.a18 = ("Arial", 18)
        self.a16 = ("Arial", 16)
        self.a14 = ("Arial", 14)
        self.a12 = ("Arial", 12)
        
        
        # Colores
        self.colors = {
            "default": "#ffffff",
            "black": "#000000",
            "main_blue": "#3984db",
            "intro_bg": "#83cfff",
            "lobby_bg": "#bb83ff",
            "game_bg": "#83f1ff",
            "round_bg": "#ffc183",
            "results_bg_win": "#83ff94",
            "results_bg_loss": "#ff8383",
            "hall_of_fame_bg": "#f7ff83",
            "exit": "#ff0000",
        }