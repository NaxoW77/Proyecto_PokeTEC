from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

class ResultsFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["results_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(fill="both", expand=True, pady=40, padx=20)
        
        # Resultado
        self.result_title = self.create_title(body, lang.resultsScreen.title)
        self.result_title.pack(pady=30)
        
        # Stats
        stats_frame = tk.Frame(body, bg=style.colors["default"])
        stats_frame.pack(pady=20)
        
        self.player_name_label = self.create_text1(stats_frame, f"{lang.gameScreen.player_label}: Jugador", 0, 5, 400)
        self.player_name_label.pack(pady=5)
        self.player_score_label = self.create_text1(stats_frame, "Puntaje: 0", 0, 5, 400)
        self.player_score_label.pack(pady=5)
        
        # Botones
        btn_container = tk.Frame(body, bg=style.colors["default"])
        btn_container.pack(side="bottom", pady=20)
        
        self.create_button1(btn_container, lang.resultsScreen.exit_button, lambda: controller.show_frame("IntroFrame")).pack(side="left", padx=5)
        self.create_button1(btn_container, lang.resultsScreen.hall_of_fame_button, lambda: controller.show_frame("HallOfFameFrame")).pack(side="left", padx=5)
    
    def update_display(self):
        player = self.controller.player
        
        player_avatar = player.getAvatar()
        player_name = player.getName()
        player_score = player.getScore()
        
        player_team = player.getTeam()
        
        if player_team == []:
            self.result_title.config(text=lang.resultsScreen.defeat)
        else:
            self.result_title.config(text=lang.resultsScreen.victory)
        
        self.player_name_label.config(text=f"{lang.gameScreen.player_label}: {player_name}")
        self.player_score_label.config(text=f"Puntaje: {player_score}")