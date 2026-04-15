from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

class HallOfFameFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["hall_of_fame_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(fill="both", expand=True, pady=20, padx=20)
        
        # Título
        self.create_title(body, lang.hallOfFameScreen.title).pack(pady=10)
        
        # Tabla de registros
        table_frame = tk.Frame(body, bg=style.colors["default"])
        table_frame.pack(fill="both", expand=True, pady=20)
        
        columns = ("jugador", "equipo", "puntaje")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        self.tree.heading("jugador", text=lang.hallOfFameScreen.player_column)
        self.tree.heading("equipo", text=lang.hallOfFameScreen.team_column)
        self.tree.heading("puntaje", text=lang.hallOfFameScreen.score_column)
        
        self.tree.column("jugador", width=150)
        self.tree.column("equipo", width=250)
        self.tree.column("puntaje", width=100)
        
        # Datos de ejemplo
        self.load_records()
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botón Volver
        self.create_button1(body, lang.hallOfFameScreen.back_button, lambda: controller.show_frame("IntroFrame")).pack(pady=20)
    
    def load_records(self):
        # JSON, etc etc
        records = [
            ("Jugador 1", "Pikachu, Charizard, Squirtle", "1000"),
            ("Jugador 2", "Blastoise, Venusaur, Arcanine", "950"),
            ("Jugador 3", "Alakazam, Gengar, Machamp", "900"),
        ]
        
        for record in records:
            self.tree.insert("", "end", values=record)