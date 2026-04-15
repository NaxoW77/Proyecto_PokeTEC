from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

import random as random

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

class GameFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["game_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        # --- Player frames ---
        players_frame = tk.Frame(self, bg=style.colors["default"])
        players_frame.pack(fill="x", pady=20, padx=20)
        players_frame.grid_columnconfigure(0, weight=1)
        players_frame.grid_columnconfigure(1, weight=1)
        
        # Player 1
        p1_frame = tk.Frame(players_frame, bg=style.colors["default"], relief="solid", borderwidth=1)
        p1_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        
        self.p1_img = tk.PhotoImage(file="assets/img/char_01.png").subsample(2, 2)
        self.p1_img_label = tk.Label(p1_frame, image=self.p1_img, bg=style.colors["default"])
        self.p1_img_label.pack(pady=5, side="left")
        
        self.p1_title = self.create_title(p1_frame, f"lang.gameScreen.player_label: {lang.gameScreen.default}")
        self.p1_title.pack(pady=5,side="left")
        
        self.p1_pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.p1_pokemon_img_label = tk.Label(p1_frame, image=self.p1_pokemon_img, bg=style.colors["default"])
        self.p1_pokemon_img_label.pack(pady=5)
        
        self.p1_pokemon = self.create_text1(p1_frame, f"{lang.gameScreen.pokemon_label}: {lang.gameScreen.default}", 0, 5, 300)
        self.p1_pokemon.pack()
        self.p1_health = self.create_text1(p1_frame, f"{lang.gameScreen.health_label}: {lang.gameScreen.default}", 0, 5, 300)
        self.p1_health.pack()
        
        # Player 2
        p2_frame = tk.Frame(players_frame, bg=style.colors["default"], relief="solid", borderwidth=1)
        p2_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        
        self.p2_img = tk.PhotoImage(file="assets/img/char_11.png").subsample(2, 2)
        self.p2_img_label = tk.Label(p2_frame, image=self.p2_img, bg=style.colors["default"])
        self.p2_img_label.pack(pady=5, side="right")
        
        self.p2_title = self.create_title(p2_frame, f"{lang.gameScreen.player_label}: {lang.gameScreen.default}")
        self.p2_title.pack(pady=5,side="right")
        
        self.p2_pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.p2_pokemon_img_label = tk.Label(p2_frame, image=self.p2_pokemon_img, bg=style.colors["default"])
        self.p2_pokemon_img_label.pack(pady=5)
        
        self.p2_pokemon = self.create_text1(p2_frame, f"{lang.gameScreen.pokemon_label}: {lang.gameScreen.default}", 0, 5, 300)
        self.p2_pokemon.pack()
        self.p2_health = self.create_text1(p2_frame, f"{lang.gameScreen.health_label}: {lang.gameScreen.default}", 0, 5, 300)
        self.p2_health.pack()
        
        # --- Battle Frame ---
        battle_frame = tk.Frame(self, bg=style.colors["default"])
        battle_frame.pack(fill="both", expand=True, pady=3, padx=20)
        
        self.create_title(battle_frame, lang.gameScreen.title).pack(pady=0)
        self.battle_log = self.create_text2(battle_frame, "Combate iniciado...", 10, 10, 600, "center")
        self.battle_log.pack(pady=2, fill="both", expand=True)
        
        # --- Action Dialog ---
        self.actions_frame = tk.Frame(self, bg="white", relief="solid", borderwidth=2)
        self.create_text1(self.actions_frame, lang.gameScreen.actions_prompt, 0, 10, 400).pack(pady=5)
        
        actions_btn_frame = tk.Frame(self.actions_frame, bg="white")
        actions_btn_frame.pack(pady=10)
        
        self.actionBtn1 = self.create_button1(actions_btn_frame, f"A: {lang.gameScreen.default}", lambda: self.select_action(0))
        self.actionBtn1.pack(side="left", padx=5)
        
        self.actionBtn2 = self.create_button1(actions_btn_frame, f"B: {lang.gameScreen.default}", lambda: self.select_action(1))
        self.actionBtn2.pack(side="left", padx=5)
        
        self.actionBtn3 = self.create_button1(actions_btn_frame, f"C: {lang.gameScreen.default}", lambda: self.select_action(2))
        self.actionBtn3.pack(side="left", padx=5)
        
        self.actionBtn4 = self.create_button1(actions_btn_frame, f"D: {lang.gameScreen.default}", lambda: self.select_action(3))
        self.actionBtn4.pack(side="left", padx=5)
        
        # --- Bottom Button ---
        btn_container = tk.Frame(self, bg=style.colors["default"])
        btn_container.pack(side="bottom", pady=20)
        
        self.btn_actions = self.create_button1(btn_container, lang.gameScreen.actions_button, self.toggle_actions)
        self.btn_actions.pack(side="left", padx=5)
    
    def toggle_actions(self):
        if self.actions_frame.winfo_ismapped():
            self.actions_frame.pack_forget()
        else:
            self.actions_frame.pack(side="bottom", pady=5, padx=20, fill="x")

        
    
    def select_action(self, action):
        player = self.controller.player
        rival = self.controller.rival
        player_pkm = player.getCurrentPokemon()
        rival_pkm = rival.getCurrentPokemon()
        
        self.btn_actions.config(state="disabled")
        self.toggle_actions()
        
        rival_pkm.takeDamage(player_pkm.moveset[action].type,player_pkm.moveset[action].power)
        self.battle_log.config(text=f"Jugador usó: {player_pkm.moveset[action].name}")
            
        if rival_pkm.current_hp <= 0:
            player.setScore(player.getScore() + 1)
            player.addPokemon(rival_pkm)
            rival.removePokemon(rival_pkm)
            if rival.team == []:
                self.controller.show_frame("ResultsFrame")
                return
            self.controller.show_frame("RoundFrame")
        
        self.update_stats()
        self.after(random.randint(500, 2500), lambda: self.rival_action())
    
    
    def rival_action(self):
        player = self.controller.player
        rival = self.controller.rival
        player_pkm = player.getCurrentPokemon()
        rival_pkm = rival.getCurrentPokemon()
        
        action = rival_pkm.moveset[random.randint(0, len(rival_pkm.moveset) - 1)]
        self.battle_log.config(text=f"Rival usó: {action.name}")
        player_pkm.takeDamage(action.type,action.power)
        
        if player_pkm.current_hp <= 0:
            rival.setScore(rival.getScore() + 1)
            rival.addPokemon(player_pkm)
            player.removePokemon(player_pkm)
            
            if player.team == []:
                self.controller.show_frame("ResultsFrame")
                return
            
            
            self.controller.show_frame("RoundFrame")
        
        self.update_stats()
        self.btn_actions.config(state="normal")
    
    
    def update_stats(self):
        self.p1_health.config(text=f"{lang.gameScreen.health_label}: {self.controller.player.getCurrentPokemon().current_hp}")
        self.p2_health.config(text=f"{lang.gameScreen.health_label}: {self.controller.rival.getCurrentPokemon().current_hp}")
    
    def update_display(self):
        player = self.controller.player
        current_pokemon = self.controller.player.getCurrentPokemon()
        
        self.p1_title.config(text=f"{lang.gameScreen.player_label}: {player.getName()}")
        
        self.p1_img = tk.PhotoImage(file=player.getAvatar()).subsample(2, 2)
        self.p1_img_label.config(image=self.p1_img)
        
        self.p1_pokemon_img.config(file=current_pokemon.img)
        
        self.p1_pokemon.config(text=f"{lang.gameScreen.pokemon_label}: {current_pokemon.name}")
        self.p1_health.config(text=f"{lang.gameScreen.health_label}: {current_pokemon.current_hp}")
        
        rival = self.controller.rival
        current_rival_pokemon = self.controller.rival.getCurrentPokemon()
        
        self.p2_title.config(text=f"{lang.gameScreen.player_label}: {rival.getName()}")
        
        self.p2_img = tk.PhotoImage(file=rival.getAvatar()).subsample(2, 2)
        self.p2_img_label.config(image=self.p2_img)
        
        self.p2_pokemon_img.config(file=current_rival_pokemon.img)
        
        self.p2_pokemon.config(text=f"{lang.gameScreen.pokemon_label}: {current_rival_pokemon.name}")
        self.p2_health.config(text=f"{lang.gameScreen.health_label}: {current_rival_pokemon.current_hp}")
        
        
        self.actionBtn1.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[0].name}")
        self.actionBtn2.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[1].name}")
        self.actionBtn3.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[2].name}")
        self.actionBtn4.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[3].name}")
