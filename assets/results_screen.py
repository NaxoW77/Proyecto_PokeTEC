
# --- Pantalla de resultados ---

# Aquí se muestra el resultado de la partida
# Si el jugador gana, se muestra un banner de victoria
# y se añade al salón de la fama,
# si pierde, se muestra un banner de derrota.

# Imports necesarios
import os
import json
from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang().resultsScreen

# Importar estilos
from assets.styles import Style
style = Style()

class ResultsFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])

        self.top_path = os.path.join(os.path.dirname(__file__), "data", "top.json")

        # --- Banner ---
        self.banner = tk.Frame(self, bg=style.colors["results_bg_win"], height=10)
        self.banner.pack(fill="x")
        # --- Banner ---

        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(fill="both", expand=True, pady=40, padx=20)

        # Resultado
        self.result_title = self.create_title(body, lang.title)
        self.result_title.pack(pady=5)

        result_body = tk.Frame(body, bg=style.colors["default"])
        result_body.pack(fill="both", expand=True)

        center_panel = tk.Frame(result_body, bg=style.colors["default"])
        center_panel.pack(fill="both", expand=True, padx=20, pady=5)

        self.player_img = tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)
        self.player_img_label = tk.Label(center_panel, image=self.player_img, bg=style.colors["default"])
        self.player_img_label.pack(pady=10)

        self.player_name_label = self.create_text1(center_panel, f"{lang.player_label}: {lang.default}", 0, 5, 250)
        self.player_name_label.pack(pady=3)
        
        self.player_score_label = self.create_text1(center_panel, f"{lang.score_label} 0", 0, 1, 250)
        self.player_score_label.pack(pady=1)
        
        self.player_team_label = self.create_text2(center_panel, f"{lang.team_label}: {lang.default}", 0, 5, 250)
        self.player_team_label.pack(pady=5)

        self.result_description = self.create_text2(center_panel, "", 10, 1, 500, "center")
        self.result_description.pack(pady=20)

        btn_container = tk.Frame(body, bg=style.colors["default"])
        btn_container.pack(side="bottom", pady=20)

        self.create_button1(btn_container, lang.exit_button, lambda: controller.show_frame("IntroFrame")).pack(side="left", padx=5)
        self.create_button1(btn_container, lang.hall_of_fame_button, lambda: controller.show_frame("HallOfFameFrame")).pack(side="left", padx=5)

    def update_display(self):
        player = self.controller.player
        player_avatar = player.getAvatar() or "assets/img/char_01.png"
        player_name = player.getName() or lang.player_label
        player_score = player.getScore()
        player_team = player.getTeam()

        try:
            img = tk.PhotoImage(file=player_avatar).subsample(2, 2)
        except Exception:
            img = tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)

        self.player_img = img
        self.player_img_label.config(image=self.player_img)
        self.player_img_label.image = self.player_img

        if player_team == []:
            self.result_title.config(text=lang.defeat)
            self.banner.config(bg=style.colors["results_bg_loss"])
            description = lang.defeat_msg
        else:
            self.result_title.config(text=lang.victory)
            self.banner.config(bg=style.colors["results_bg_win"])
            description = lang.victory_msg
            self.save_top_record(player)

        team_names = ", ".join([pokemon.name for pokemon in player_team]) if player_team else lang.default
        self.player_name_label.config(text=f"{lang.player_label}: {player_name}")
        self.player_score_label.config(text=f"{lang.score_label} {player_score}")
        self.player_team_label.config(text=f"{lang.team_label}: {team_names}")
        self.result_description.config(text=description)

    def load_top_records(self):
        if not os.path.exists(self.top_path):
            return []
        try:
            with open(self.top_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        return []

    def save_top_records(self, records):
        os.makedirs(os.path.dirname(self.top_path), exist_ok=True)
        with open(self.top_path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)

    def save_top_record(self, player):
        if not player.getName():
            return

        current_records = self.load_top_records()
        player_record = {
            "name": player.getName(),
            "avatar": player.getAvatar() or "assets/img/char_01.png",
            "score": player.getScore(),
            "team": [pokemon.name for pokemon in player.getTeam()],
        }

        existing = next((item for item in current_records if item.get("name") == player_record["name"]), None)
        if existing:
            if player_record["score"] >= existing.get("score", 0):
                existing.update(player_record)
        else:
            current_records.append(player_record)

        current_records.sort(key=lambda item: item.get("score", 0), reverse=True)
        self.save_top_records(current_records[:10])
