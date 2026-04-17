import os
import json

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

        self.top_path = os.path.join(os.path.dirname(__file__), "data", "top.json")

        # --- Banner ---
        self.banner = tk.Frame(self, bg=style.colors["results_bg_win"], height=10)
        self.banner.pack(fill="x")
        # --- Banner ---

        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(fill="both", expand=True, pady=40, padx=20)

        # Resultado
        self.result_title = self.create_title(body, lang.resultsScreen.title)
        self.result_title.pack(pady=30)

        result_body = tk.Frame(body, bg=style.colors["default"])
        result_body.pack(fill="both", expand=True)

        center_panel = tk.Frame(result_body, bg=style.colors["default"])
        center_panel.pack(fill="both", expand=True, padx=20, pady=10)

        self.player_img = tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)
        self.player_img_label = tk.Label(center_panel, image=self.player_img, bg=style.colors["default"])
        self.player_img_label.pack(pady=10)

        self.player_name_label = self.create_text1(center_panel, f"{lang.gameScreen.player_label}: Jugador", 0, 5, 250)
        self.player_name_label.pack(pady=5)
        self.player_score_label = self.create_text1(center_panel, "Puntaje: 0", 0, 5, 250)
        self.player_score_label.pack(pady=5)
        self.player_team_label = self.create_text1(center_panel, f"{lang.hallOfFameScreen.team_column}: ---", 0, 5, 250)
        self.player_team_label.pack(pady=5)

        self.result_description = self.create_text2(center_panel, "", 10, 10, 500, "center")
        self.result_description.pack(pady=20)

        btn_container = tk.Frame(body, bg=style.colors["default"])
        btn_container.pack(side="bottom", pady=20)

        self.create_button1(btn_container, lang.resultsScreen.exit_button, lambda: controller.show_frame("IntroFrame")).pack(side="left", padx=5)
        self.create_button1(btn_container, lang.resultsScreen.hall_of_fame_button, lambda: controller.show_frame("HallOfFameFrame")).pack(side="left", padx=5)

    def update_display(self):
        player = self.controller.player
        player_avatar = player.getAvatar() or "assets/img/char_01.png"
        player_name = player.getName() or "Jugador"
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
            self.result_title.config(text=lang.resultsScreen.defeat)
            self.banner.config(bg=style.colors["results_bg_loss"])
            description = "Has perdido. Intenta de nuevo para entrar al Salón de la Fama."
        else:
            self.result_title.config(text=lang.resultsScreen.victory)
            self.banner.config(bg=style.colors["results_bg_win"])
            description = "¡Felicidades! Tu resultado se guardará en el Salón de la Fama."
            self.save_top_record(player)

        team_names = ", ".join([pokemon.name for pokemon in player_team]) if player_team else "---"
        self.player_name_label.config(text=f"{lang.gameScreen.player_label}: {player_name}")
        self.player_score_label.config(text=f"Puntaje: {player_score}")
        self.player_team_label.config(text=f"{lang.hallOfFameScreen.team_column}: {team_names}")
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
