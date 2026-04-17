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

class HallOfFameFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])

        self.top_path = os.path.join(os.path.dirname(__file__), "data", "top.json")
        self.record_images = []

        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["hall_of_fame_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---

        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(fill="both", expand=True, pady=20, padx=20)

        self.create_title(body, lang.hallOfFameScreen.title).pack(pady=10)
        self.summary_label = self.create_text1(body, "", 10, 5, 700)
        self.summary_label.pack(pady=5)

        table_frame = tk.Frame(body, bg=style.colors["default"])
        table_frame.pack(fill="both", expand=True, pady=20)

        self.records_canvas = tk.Canvas(table_frame, bg=style.colors["default"], highlightthickness=0)
        self.records_canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.records_canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.records_canvas.configure(yscrollcommand=scrollbar.set)
        self.records_list_frame = tk.Frame(self.records_canvas, bg=style.colors["default"])
        self.list_window = self.records_canvas.create_window((0, 0), window=self.records_list_frame, anchor="nw")

        self.records_list_frame.bind(
            "<Configure>",
            lambda event: self.records_canvas.configure(scrollregion=self.records_canvas.bbox("all"))
        )
        self.records_canvas.bind(
            "<Configure>",
            lambda event: self.records_canvas.itemconfig(self.list_window, width=event.width)
        )

        self.create_button1(body, lang.hallOfFameScreen.back_button, lambda: controller.show_frame("IntroFrame")).pack(pady=20)

    def update_display(self):
        self.display_records()

    def display_records(self):
        records = self.load_records()
        self.record_images.clear()
        for child in self.records_list_frame.winfo_children():
            child.destroy()

        if not records:
            self.summary_label.config(text=lang.hallOfFameScreen.no_records)
            self.create_text1(self.records_list_frame, lang.hallOfFameScreen.no_records, 10, 10, 700).pack(pady=20)
            return

        self.summary_label.config(text=f"Top {min(len(records), 10)} jugadores")

        for index, record in enumerate(records, start=1):
            row = tk.Frame(self.records_list_frame, bg=style.colors["default"], relief="solid", borderwidth=1)
            row.pack(fill="x", padx=5, pady=5)

            avatar_file = record.get("avatar") or "assets/img/char_01.png"
            avatar_img = self.load_avatar_image(avatar_file)
            avatar_label = tk.Label(row, image=avatar_img, bg=style.colors["default"])
            avatar_label.image = avatar_img
            avatar_label.pack(side="left", padx=10, pady=10)
            self.record_images.append(avatar_img)

            details_frame = tk.Frame(row, bg=style.colors["default"])
            details_frame.pack(side="left", fill="x", expand=True, padx=10, pady=10)

            name_label = self.create_title(details_frame, f"{index}. {record.get('name', '---')}", fg=style.colors["black"], bg=style.colors["default"])
            name_label.pack(anchor="w")

            score = record.get("score", 0)
            team = record.get("team", [])
            team_text = ", ".join(team) if team else "---"
            self.create_text2(
                details_frame,
                f"{lang.hallOfFameScreen.score_column}: {score}\n{lang.hallOfFameScreen.team_column}: {team_text}",
                0,
                0,
                700,
                "left",
            ).pack(anchor="w")

    def load_records(self):
        if not os.path.exists(self.top_path):
            self.save_records([])
            return []

        try:
            with open(self.top_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    normalized = []
                    for item in data:
                        if isinstance(item, dict):
                            record = item.copy()
                            try:
                                record["score"] = int(record.get("score", 0))
                            except (TypeError, ValueError):
                                record["score"] = 0
                            normalized.append(record)
                    return sorted(normalized, key=lambda item: item.get("score", 0), reverse=True)[:10]
        except (json.JSONDecodeError, FileNotFoundError):
            pass

        self.save_records([])
        return []

    def save_records(self, records):
        os.makedirs(os.path.dirname(self.top_path), exist_ok=True)
        with open(self.top_path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)

    def load_avatar_image(self, path):
        try:
            return tk.PhotoImage(file=path).subsample(2, 2)
        except Exception:
            return tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)
