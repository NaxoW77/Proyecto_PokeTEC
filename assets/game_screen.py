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
        players_frame.pack(fill="both", expand=False, pady=20, padx=20)
        players_frame.grid_columnconfigure(0, weight=1, uniform="cols")
        players_frame.grid_columnconfigure(1, weight=1, uniform="cols")
        
        # Player 1
        p1_frame = tk.Frame(players_frame, bg=style.colors["default"], relief="solid", borderwidth=1)
        p1_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        
        self.p1_img = tk.PhotoImage(file="assets/img/char_01.png")
        self.p1_img_label = tk.Label(p1_frame, image=self.p1_img, bg=style.colors["default"])
        self.p1_img_label.pack(pady=5, padx=5, side="left")
        
        self.p1_title = self.create_title(p1_frame, f"lang.gameScreen.player_label: {lang.gameScreen.default}")
        self.p1_title.pack(pady=5, padx=5, side="left", fill="x")
        self.p1_title.config(wraplength=150)
        
        self.p1_pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.p1_pokemon_img_label = tk.Label(p1_frame, image=self.p1_pokemon_img, bg=style.colors["default"])
        self.p1_pokemon_img_label.pack(pady=5, padx=15)
        
        self.p1_pokemon = self.create_text1(p1_frame, f"{lang.gameScreen.pokemon_label}: {lang.gameScreen.default}", 15, 5, 300)
        self.p1_pokemon.pack()
        self.p1_health = self.create_text1(p1_frame, f"{lang.gameScreen.health_label}: {lang.gameScreen.default}", 15, 5, 300)
        self.p1_health.pack()
        
        # Player 2
        p2_frame = tk.Frame(players_frame, bg=style.colors["default"], relief="solid", borderwidth=1)
        p2_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        
        self.p2_img = tk.PhotoImage(file="assets/img/char_11.png")
        self.p2_img_label = tk.Label(p2_frame, image=self.p2_img, bg=style.colors["default"])
        self.p2_img_label.pack(pady=5, padx=5, side="right")
        
        self.p2_title = self.create_title(p2_frame, f"{lang.gameScreen.player_label}: {lang.gameScreen.default}")
        self.p2_title.pack(pady=5, padx=5, side="right", fill="x")
        self.p2_title.config(wraplength=150)
        
        self.p2_pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.p2_pokemon_img_label = tk.Label(p2_frame, image=self.p2_pokemon_img, bg=style.colors["default"])
        self.p2_pokemon_img_label.pack(pady=5, padx=15)
        
        self.p2_pokemon = self.create_text1(p2_frame, f"{lang.gameScreen.pokemon_label}: {lang.gameScreen.default}", 15, 5, 300)
        self.p2_pokemon.pack()
        self.p2_health = self.create_text1(p2_frame, f"{lang.gameScreen.health_label}: {lang.gameScreen.default}", 15, 5, 300)
        self.p2_health.pack()
        
        # --- Battle Frame ---
        battle_frame = tk.Frame(self, bg=style.colors["default"])
        battle_frame.pack(fill="both", expand=True, pady=3, padx=20)
        
        self.create_title(battle_frame, lang.gameScreen.title).pack(pady=0)
        self.battle_log = self.create_text2(battle_frame, "A luchar... \nEscoge una acción abajo.", 10, 10, 600, "center")
        self.battle_log.pack(pady=2, fill="both", expand=True)
        
        self.battle_log2 = self.create_text2(battle_frame, "", 10, 10, 600, "center")
        self.battle_log2.pack(pady=2, fill="both", expand=True)
        
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
        
        # --- Bottom Buttons ---
        btn_container = tk.Frame(self, bg=style.colors["default"])
        btn_container.pack(side="bottom", pady=20)
        
        self.btn_actions = self.create_button1(btn_container, lang.gameScreen.actions_button, self.toggle_actions)
        self.btn_actions.pack(side="left", padx=5)
        
        self.btn_continue = self.create_button1(btn_container, "Continuar", lambda: self.controller.show_frame("RoundFrame"))
        self.btn_continue.pack(side="left", padx=5)
    
    
    
    def hide(self, elem):
        elem.pack_forget()
    
    def show(self, elem):
        elem.pack(side="left", padx=5)
    
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
        
        self.battle_log.config(text=f"Jugador usó: {player_pkm.moveset[action].name}")
        
        result = None
        if player_pkm.moveset[action].type == "ATK":
            result = rival_pkm.takeDamage(player_pkm.moveset[action].power, player_pkm.moveset[action].accuracy, player_pkm.current_attack)
            if isinstance(result, int):
                self.battle_log2.config(text=f"Tu {player_pkm.name} hizo {result} de daño.")
            else:
                self.battle_log2.config(text=f"Pero el {rival_pkm.name} rival {result}")
        else:
            typeName = ""
            if player_pkm.moveset[action].type == "DMG":
                typeName = "daño"
            else:
                typeName = "defensa"
            result = player_pkm.takeStat(player_pkm.moveset[action].type, player_pkm.moveset[action].power)
            if isinstance(result, int):
                self.battle_log2.config(text=f"Tu {player_pkm.name} aumentó su {typeName} en {result}.")
            else:
                self.battle_log2.config(text=f"Pero {result}")
                
        self.update_stats()
            
        if rival_pkm.current_hp <= 0:
            player.setScore(player.getScore() + 1)
            player.addPokemon(rival_pkm)
            rival.removePokemon(rival_pkm)
            if rival.team == []:
                self.controller.show_frame("ResultsFrame")
                return
            
            self.battle_log.config(text=f"Has derrotado al {rival_pkm.name} rival.")
            self.battle_log2.config(text=f"Ahora tienes a {rival_pkm.name} en tu equipo.")
            
            self.hide(self.btn_actions)
            self.show(self.btn_continue)
            return
        
    
        
        self.after(3000, lambda: (
            self.battle_log.config(text="El rival está pensando..."),
            self.battle_log2.config(text=""),
            self.after(random.randint(1500, 3000), lambda: self.rival_action())
        ))
        
    
    
    def rival_action(self):
        player = self.controller.player
        rival = self.controller.rival
        player_pkm = player.getCurrentPokemon()
        rival_pkm = rival.getCurrentPokemon()
        
        action = rival_pkm.moveset[random.randint(0, len(rival_pkm.moveset) - 1)]
        self.battle_log.config(text=f"Rival usó: {action.name}")
        
        result = None
        if action.type == "ATK":
            result = player_pkm.takeDamage(action.power, action.accuracy, rival_pkm.current_attack)
            if isinstance(result, int):
                self.battle_log2.config(text=f"El {rival_pkm.name} rival hizo {result} de daño.")
            else:
                self.battle_log2.config(text=f"Pero tu {player_pkm.name} {result}")
        else:
            result = rival_pkm.takeStat(action.type, action.power)
            if isinstance(result, int):
                self.battle_log2.config(text=f"{rival_pkm.name} aumentó su {action.type} en {result}.")
            else:
                self.battle_log2.config(text=f"Pero {result}")
        
        self.update_stats()
        
        if player_pkm.current_hp <= 0:
            rival.setScore(rival.getScore() + 1)
            rival.addPokemon(player_pkm)
            player.removePokemon(player_pkm)
            
            if player.team == []:
                self.controller.show_frame("ResultsFrame")
                return
            
            
            self.battle_log.config(text=f"Has sido derrotado por tu rival.")
            self.battle_log2.config(text=f"Te han quitado a {player_pkm.name} de tu equipo.")
            
            self.hide(self.btn_actions)
            self.show(self.btn_continue)
            return
        
        self.after(3000, lambda: (
            self.battle_log.config(text="Tu turno...\nSelecciona una acción abajo."),
            self.battle_log2.config(text=""),
            self.btn_actions.config(state="normal")
        ))
    
    
    def update_stats(self):
        self.p1_health.config(text=f"{lang.gameScreen.health_label}: {self.controller.player.getCurrentPokemon().current_hp}/{self.controller.player.getCurrentPokemon().hp}")
        self.p2_health.config(text=f"{lang.gameScreen.health_label}: {self.controller.rival.getCurrentPokemon().current_hp}/{self.controller.rival.getCurrentPokemon().hp}")
    
    def update_display(self):
        self.btn_actions.config(state="normal")
        self.battle_log.config(text="Tu turno...\nSelecciona una acción abajo.")
        self.battle_log2.config(text="")
        
        self.show(self.btn_actions)
        self.hide(self.btn_continue)
        
        player = self.controller.player
        current_pokemon = self.controller.player.getCurrentPokemon()
        
        self.p1_title.config(text=f"{lang.gameScreen.player_label}: {player.getName()}")
        
        self.p1_img = tk.PhotoImage(file=player.getAvatar()).subsample(2, 2)
        self.p1_img_label.config(image=self.p1_img)
        
        self.p1_pokemon_img = tk.PhotoImage(file=current_pokemon.img).subsample(2, 2)
        self.p1_pokemon_img_label.config(image=self.p1_pokemon_img)
        
        self.p1_pokemon.config(text=f"{lang.gameScreen.pokemon_label}: {current_pokemon.name}")
        self.p1_health.config(text=f"{lang.gameScreen.health_label}: {current_pokemon.current_hp}/{current_pokemon.hp}")
        
        rival = self.controller.rival
        current_rival_pokemon = self.controller.rival.getCurrentPokemon()
        
        self.p2_title.config(text=f"{lang.gameScreen.player_label}: {rival.getName()}")
        
        self.p2_img = tk.PhotoImage(file=rival.getAvatar()).subsample(2, 2)
        self.p2_img_label.config(image=self.p2_img)
        
        self.p2_pokemon_img = tk.PhotoImage(file=current_rival_pokemon.img).subsample(2, 2)
        self.p2_pokemon_img_label.config(image=self.p2_pokemon_img)
        
        self.p2_pokemon.config(text=f"{lang.gameScreen.pokemon_label}: {current_rival_pokemon.name}")
        self.p2_health.config(text=f"{lang.gameScreen.health_label}: {current_rival_pokemon.current_hp}/{current_rival_pokemon.hp}")
        
        
        self.actionBtn1.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[0].name}")
        self.actionBtn2.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[1].name}")
        self.actionBtn3.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[2].name}")
        self.actionBtn4.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[3].name}")
