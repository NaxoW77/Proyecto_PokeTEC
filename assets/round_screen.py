import random as random

from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

# Importar lista de Pokémon
from assets.data.pokemon_list import PokemonList
pokemon_list = PokemonList()

class RoundFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["round_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        # --- Body ---
        body = tk.Frame(self, bg=style.colors["default"])
        body.pack(pady=20, padx=20)
        
        # Título
        self.create_title(body, lang.roundScreen.title).pack(pady=10)
        
        # Descripción
        self.create_text1(body, lang.roundScreen.description, 10, 5, 600).pack(pady=10)
        
        leftGroup = tk.Frame(body, bg=style.colors["default"])
        leftGroup.pack(side="left", padx=10)
        
        rightGroup = tk.Frame(body, bg=style.colors["default"])
        rightGroup.pack(side="right", padx=10)
        
        # Jugador
        self.player_img = tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)
        self.player_img_label = tk.Label(leftGroup, image=self.player_img, bg=style.colors["default"])
        self.player_img_label.pack(pady=5)
        
        self.player_name_label = self.create_text1(leftGroup, f"{lang.gameScreen.player_label}: {lang.roundScreen.default}", 0, 5, 400)
        self.player_name_label.pack(pady=5)
        
        self.player_score_label = self.create_text1(leftGroup, f"Puntaje: {lang.roundScreen.default}", 0, 5, 400)
        self.player_score_label.pack(pady=5)
        
        self.pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png")
        self.pokemon_img_label = tk.Label(rightGroup, image=self.pokemon_img, bg=style.colors["default"])
        self.pokemon_img_label.pack(pady=5)
        
        self.pokemon_combo = ttk.Combobox(rightGroup, values=pokemon_list.getNames(), font=style.a16, state="readonly", width=10)
        self.pokemon_combo.pack(pady=10)
        
        self.pokemon_combo.bind("<<ComboboxSelected>>", lambda e: self.checkSelection(self.pokemon_combo, self.pokemon_img))
        
        # Botones
        btn_frame = tk.Frame(self, bg=style.colors["default"])
        btn_frame.pack(pady=20)
        
        self.create_button1(btn_frame, lang.roundScreen.continue_button, self.continue_round).pack(padx=5)
        
        # Error message
        self.error_txt = self.create_text1(self, "", 10, 5, 600)
        
    def continue_round(self):
        selected = self.pokemon_combo.get()
        
        if selected == "":
            self.error_txt.config(text=lang.roundScreen.error_select)
            self.show(self.error_txt)
            return
        
        self.hide(self.error_txt)
        self.controller.player.setCurrentPokemon(pokemon_list.getPokemon(selected))
        self.controller.rival.setCurrentPokemon(self.controller.rival.team[random.randint(0, len(self.controller.rival.team) - 1)])
        self.controller.show_frame("GameFrame")
    
    def hide(self, elem):
        elem.pack_forget()
    
    def show(self, elem):
        elem.pack(fill="x", pady=10)
        
    def checkSelection(self, element, image):
        pkm = pokemon_list.getPokemon(element.get())
        image.config(file=pkm.img)
        
    def update_display(self):
        player = self.controller.player
        
        self.player_img = tk.PhotoImage(file=player.getAvatar()).subsample(2, 2)
        self.player_img_label.config(image=self.player_img)
        
        self.player_name_label.config(text=f"{lang.gameScreen.player_label}: {player.getName()}")
        self.player_score_label.config(text=f"Puntaje: {player.getScore()}")
        
        team = player.getTeam()
        
        teamNames = [pokemon.name for pokemon in team]
        self.pokemon_combo.config(values=teamNames)
        
        for pokemon in self.controller.player.team:
                pokemon.current_hp = pokemon.hp
        
        for pokemon in self.controller.rival.team:
                pokemon.current_hp = pokemon.hp