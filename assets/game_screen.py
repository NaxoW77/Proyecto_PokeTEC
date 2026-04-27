
# --- Pantalla del juego ---

# Aquí se muestra el jugador y el rival,
# sus pokemon y estadísticas,
# y los movimientos a realizar.

# Imports necesarios
from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

import random as random

# Importar textos
from assets.lang import Lang
lang = Lang().gameScreen # Se necesita únicamente el diccionario de este frame

# Importar estilos
from assets.styles import Style
style = Style()


# Se define la clase del frame
class GameFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"]) # Se hereda el controlador
        
        # --- Banner ---
        
        banner = tk.Frame(
            self,
            bg=style.colors["game_bg"],
            height=10
        )
        banner.pack(fill="x")
        
        # --- Banner ---
        
        
        
        # --- Título ---
        
        self.create_title(
            self,
            lang.title
        ).pack(pady=15)    
        
        # --- Título ---    
        
        # --- Contenedor de los jugadores ---
        
        players_frame = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        players_frame.pack(fill="both", expand=False, pady=10, padx=20)
        
        # Configuración de las columnas
        players_frame.grid_columnconfigure(0, weight=1, uniform="cols")
        players_frame.grid_columnconfigure(1, weight=1, uniform="cols")
        
        # -- Contenedor del jugador
        p1_frame = tk.Frame(
            players_frame,
            bg=style.colors["default"],
            relief="solid",
            borderwidth=1
        )
        p1_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        
        # Imagen del jugador
        self.p1_img = tk.PhotoImage(file="assets/img/char_01.png")
        
        # Etiqueta de la imagen
        self.p1_img_label = tk.Label(
            p1_frame,
            image=self.p1_img,
            bg=style.colors["default"]
        )
        self.p1_img_label.pack(pady=5, padx=10, side="left")
        
        # Etiqueta del nombre del jugador
        self.p1_title = self.create_title(
            p1_frame,
            f"{lang.player_label}: {lang.default}"
        )
        self.p1_title.pack(pady=5, padx=5, side="left", fill="x")
        
        # Configuración de la etiqueta del nombre
        self.p1_title.config(wraplength=150)
        
        # Contenedor del pokemon del jugador
        pokemon1_frame = tk.Frame(
            p1_frame,
            bg=style.colors["default"]
        )
        pokemon1_frame.pack(pady=(0,25), padx=5, fill="x", expand=True)
        
        # Marco de la imagen del pokemon
        pokemon1_img_frame = tk.Frame(
            pokemon1_frame,
            bg=style.colors["default"]
        )
        pokemon1_img_frame.pack(pady=5, padx=20, fill="x", expand=True)
        
        # Imagen del pokemon
        self.p1_pokemon_img = tk.PhotoImage(
            file="assets/img/pkm0.png"
        ).subsample(2, 2) # Se reduce el tamaño de la imagen
        
        # Etiqueta de la imagen
        self.p1_pokemon_img_label = tk.Label(
            pokemon1_img_frame,
            image=self.p1_pokemon_img,
            bg=style.colors["default"]
        )
        self.p1_pokemon_img_label.pack()
        
        # Nombre del pokemon
        self.p1_pokemon = self.create_text1(
            pokemon1_frame,
            f"{lang.pokemon_label}: {lang.default}",
            15,
            3, 
            300
        )
        self.p1_pokemon.pack()
        
        # Vida del pokemon
        self.p1_health = self.create_text1(
            pokemon1_frame,
            f"{lang.health_label}: {lang.default}",
            15,
            3,
            300
        )
        self.p1_health.pack()
        
        
        # -- Contenedor del rival
        p2_frame = tk.Frame(
            players_frame,
            bg=style.colors["default"], 
            relief="solid", 
            borderwidth=1
        )
        p2_frame.grid(row=0, column=1, sticky="nsew", padx=10)
        
        # Imagen del rival
        self.p2_img = tk.PhotoImage(file="assets/img/char_11.png")
        
        # Etiqueta de la imagen
        self.p2_img_label = tk.Label(
            p2_frame,
            image=self.p2_img, 
            bg=style.colors["default"]
        )
        self.p2_img_label.pack(pady=5, padx=5, side="right")
        
        # Etiqueta del nombre del rival
        self.p2_title = self.create_title(
            p2_frame,
            f"{lang.player_label}: {lang.default}"
        )
        self.p2_title.pack(pady=5, padx=5, side="right", fill="x")
        
        # Configuración de la etiqueta del nombre
        self.p2_title.config(wraplength=150)
        
        # Contenedor del pokemon del rival
        pokemon2_frame = tk.Frame(
            p2_frame, 
            bg=style.colors["default"]
        )
        pokemon2_frame.pack(pady=(0,25), padx=5, fill="x", expand=True)
        
        # Marco de la imagen del pokemon rival
        pokemon2_img_frame = tk.Frame(
            pokemon2_frame,
            bg=style.colors["default"]
        )
        pokemon2_img_frame.pack(pady=5, padx=20, fill="x", expand=True)
        
        # Imagen del pokemon rival
        self.p2_pokemon_img = tk.PhotoImage(
            file="assets/img/pkm0.png"
        ).subsample(2, 2)
        
        # Etiqueta de la imagen
        self.p2_pokemon_img_label = tk.Label(
            pokemon2_img_frame,
            image=self.p2_pokemon_img,
            bg=style.colors["default"]
        )
        self.p2_pokemon_img_label.pack(pady=5, padx=15)
        
        # Nombre del pokemon rival
        self.p2_pokemon = self.create_text1(
            pokemon2_frame,
            f"{lang.pokemon_label}: {lang.default}",
            15,
            3,
            300
        )
        self.p2_pokemon.pack()
        
        # Vida del pokemon rival
        self.p2_health = self.create_text1(
            pokemon2_frame,
            f"{lang.health_label}: {lang.default}",
            15,
            3,
            300
        )
        self.p2_health.pack()
        
        
        # -- Contenedor de los textos de batalla
        battle_frame = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        battle_frame.pack(fill="x", expand=True, pady=3, padx=20)
        
        # Título de batalla
        self.battle_log = self.create_text1(
            battle_frame,
            f"{lang.default_action}",
            10,
            5,
            600
        )
        self.battle_log.pack(pady=5, fill="x", expand=True)
        
        # Subtítulo de batalla
        self.battle_log2 = self.create_text2(
            battle_frame,
            "",
            10,
            3,
            600,
            "center"
        )
        self.battle_log2.pack(pady=3, fill="x", expand=True)
        
        
        # -- Contenedor de las acciones
        self.actions_frame = tk.Frame(
            self,
            bg="white",
            relief="solid", 
            borderwidth=2
        )
        
        # Etiqueta de las acciones
        self.create_text1(
            self.actions_frame,
            lang.actions_prompt,
            0,
            10, 
            400
        ).pack(pady=5)
        
        # Contenedor de los botones
        actions_btn_frame = tk.Frame(
            self.actions_frame,
            bg="white"
        )
        actions_btn_frame.pack(pady=10)
        
        # Botón de acción "A"
        self.actionBtn1 = self.create_button1(
            actions_btn_frame,
            f"A: {lang.default}", 
            lambda: self.select_action(0)
        )
        self.actionBtn1.pack(side="left", padx=5)
        
        # Botón de acción "B"
        self.actionBtn2 = self.create_button1(
            actions_btn_frame,
            f"B: {lang.default}",
            lambda: self.select_action(1)
        )
        self.actionBtn2.pack(side="left", padx=5)
        
        # Botón de acción "C"
        self.actionBtn3 = self.create_button1(
            actions_btn_frame,
            f"C: {lang.default}",
            lambda: self.select_action(2)
        )
        self.actionBtn3.pack(side="left", padx=5)
        
        # Botón de acción "D"
        self.actionBtn4 = self.create_button1(
            actions_btn_frame,
            f"D: {lang.default}",
            lambda: self.select_action(3)
        )
        self.actionBtn4.pack(side="left", padx=5)
        
        
        # -- Contenedor de los botones de siguiente
        btn_container = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        btn_container.pack(side="bottom", pady=20)
        
        # Botón para mostrar las acciones
        self.btn_actions = self.create_button1(
            btn_container,
            lang.actions_button,
            self.toggle_actions
        )
        self.btn_actions.pack(side="left", padx=5)
        
        # Botón para pasar de ronda
        self.btn_continue = self.create_button1(
            btn_container,
            f"{lang.continue_button}",
            self.next_round
        )
        self.btn_continue.pack(side="left", padx=5)


    
    # Función para mostrar las acciones
    def toggle_actions(self):
        if self.actions_frame.winfo_ismapped():
            self.actions_frame.pack_forget()
        else:
            self.actions_frame.pack(side="bottom", pady=5, padx=20, fill="x")

    # Función para pasar de ronda
    def next_round(self):
        self.controller.round_number += 1
        self.controller.show_frame("RoundFrame")

        
    # Función para realizar una acción del jugador
    def select_action(self, action):
        player = self.controller.player # Se obtiene el jugador actual
        rival = self.controller.rival # Se obtiene el rival actual
        player_pkm = player.getCurrentPokemon() # Se obtiene el Pokemon actual del jugador
        rival_pkm = rival.getCurrentPokemon() # Se obtiene el Pokemon actual del rival
        
        self.btn_actions.config(state="disabled") # Se deshabilita el botón de acciones
        self.toggle_actions() # Se ocultan las acciones
        
        # Se muestra: [Jugador] usó: [Movimiento]
        self.battle_log.config(text=f"{player.name} {lang.pkm_action} {player_pkm.moveset[action].name}")
        
        result = None
        if player_pkm.moveset[action].type == "ATK": # Si el movimiento es de ataque
            
            def animate_atk_1(): # Se anima como si fuese un ataque
                original_x = self.p1_pokemon_img_label.winfo_x() # Obteniendo el x original
                self.p1_pokemon_img_label.place(x=original_x + 30) # Se mueve hacia la derecha
                self.after(300, lambda: self.p1_pokemon_img_label.place(x=original_x)) # Se mueve hacia donde estaba
        
            self.after(75, animate_atk_1) # Se llama la animación después de un momento
            
            # Se realiza el ataque
            result = rival_pkm.takeDamage(player_pkm.moveset[action].power, player_pkm.moveset[action].accuracy, player_pkm.current_attack)
            
            # Si el ataque fue mayor a 0
            if result > 0:
                # Se muestra: Tu [Pokemon] hizo [Ataque] de daño.
                self.battle_log2.config(text=f"{lang.player_pref} {player_pkm.name} {lang.pkm_attack[0]} {result} {lang.pkm_attack[1]}")
            
            # Si el ataque es menor o igual a 0
            else:
                
                # Si el ataque es 0
                if result == 0:
                    # Se guarda: ...se defendió del ataque.
                    result = lang.pkm_defend
                    
                # Si el ataque es menor a 0
                else:
                    # Se guarda: ...esquivó el ataque.
                    result = lang.pkm_avoid
                
                # Se muestra: Pero el [Pokemon] rival [{esquivó/se defendió} del ataque]
                self.battle_log2.config(text=f"{lang.pkm_action_fail} {lang.rival_pref.lower()} {rival_pkm.name} {lang.rival_name} {result}")
                
        # Si el movimiento es de acción
        else:
            
            def animate_act_1(): # Se anima como si fuese una acción
                original_x = self.p1_pokemon_img_label.winfo_x() # Obteniendo el x original
                original_y = self.p1_pokemon_img_label.winfo_y() # Obteniendo el y original
                self.p1_pokemon_img_label.place(x=original_x,y=original_y - 30) # Se mueve hacia arriba
                self.after(300, lambda: self.p1_pokemon_img_label.place(x=original_x,y=original_y)) # Se mueve hacia donde estaba
        
            self.after(75, animate_act_1) # Se llama la animación luego de un momento
            
            
            typeName = "" # Se guarda el tipo de estadística
            
            # Si el movimiento es de subir daño
            if player_pkm.moveset[action].type == "DMG":
                typeName = lang.stat_dmg # Se guarda: ...daño
                
            # Si el movimiento es de subir defensa
            else:
                typeName = lang.stat_def # Se guarda: ...defensa
                
            # Se realiza la acción
            result = player_pkm.takeStat(player_pkm.moveset[action].type, player_pkm.moveset[action].power)
            
            # Si el resultado es mayor a 0
            if result > 0:
                
                # Se muestra: Tu [Pokemon] aumentó su [estadística] en [valor].
                self.battle_log2.config(text=f"{lang.player_pref} {player_pkm.name} {lang.pkm_stat[0]} {typeName} {lang.pkm_stat[1]} {result}")
                
            # Si el resultado es menor o igual a 0
            else:
                
                # Se muestra: Pero su [estadística] no subió más.
                self.battle_log2.config(text=f"{lang.pkm_stat_fail[0]} {typeName} {lang.pkm_stat_fail[1]}")
                
                
        # Se actualizan las estadísticas
        self.update_stats()
            
        # Si el rival no tiene más vida
        if rival_pkm.current_hp <= 0:
            player.setScore(player.getScore() + 1) # Se suma un punto al jugador
            player.addPokemon(rival_pkm) # Se agrega el pokemon rival al equipo del jugador
            rival.removePokemon(rival_pkm) # Se elimina el pokemon rival del equipo del rival
            
            # Si el rival no tiene pokemons
            if rival.team == []:
                # Se pasa a la pantalla de resultados
                self.controller.show_frame("ResultsFrame")
                return
            
            # Se muestra: Has derrotado al [Pokemon] rival
            self.battle_log.config(text=f"{lang.player_win[0]} {rival_pkm.name} {lang.player_win[1]}")
            
            # Se muestra: Ahora tienes a [Pokemon] en tu equipo.
            self.battle_log2.config(text=f"{lang.player_win_pkm[0]} {rival_pkm.name} {lang.player_win_pkm[1]}")
            
            # Se oculta el botón de acciones y se muestra el botón de continuar
            self.hide(self.btn_actions)
            self.show(self.btn_continue)
            return
    
        # Si el rival tiene vida
        self.after(3000, lambda: (
            self.battle_log.config(text=lang.rival_thinking), # Se muestra un mensaje de espera
            self.battle_log2.config(text=""),
            self.after(random.randint(1500, 3000), lambda: self.rival_action()) # Se llama a la acción del rival en un tiempo aleatorio
        ))
        
    
    # Función para realizar la acción del rival
    def rival_action(self):
        player = self.controller.player # Se obtiene el jugador
        rival = self.controller.rival # Se obtiene el rival
        player_pkm = player.getCurrentPokemon() # Se obtiene el pokemon del jugador
        rival_pkm = rival.getCurrentPokemon() # Se obtiene el pokemon del rival
        
        # Se elige un movimiento aleatorio
        action = rival_pkm.moveset[random.randint(0, len(rival_pkm.moveset) - 1)]
        
        # Se muestra: El rival usó: [Movimiento]
        self.battle_log.config(text=f"{lang.rival_pref} {lang.rival_name} {lang.pkm_action} {action.name}")
        
        result = None
        if action.type == "ATK": # Si el movimiento es de ataque
            
            def animate_atk_2(): # Se anima como si fuese un ataque rival
                original_x = self.p2_pokemon_img_label.winfo_x() # Se guarda la x original
                self.p2_pokemon_img_label.place(x=original_x - 30) # Se mueve hacia la izquierda
                self.after(300, lambda: self.p2_pokemon_img_label.place(x=original_x)) # Se mueve hacia la posición original
        
            self.after(75, animate_atk_2) # Se llama a la animación después de un momento
            
            # Se realiza el ataque del rival
            result = player_pkm.takeDamage(action.power, action.accuracy, rival_pkm.current_attack)
            
            # Si el resultado es mayor a 0
            if result > 0:
                
                # Se muestra: El [Pokemon] rival hizo [Ataque] de daño.
                self.battle_log2.config(text=f"{lang.rival_pref} {rival_pkm.name} {lang.rival_name} {lang.pkm_attack[0]} {result} {lang.pkm_attack[1]}")
                
            # Si el resultado es menor o igual a 0
            else:
                
                # Si el resultado es 0
                if result == 0:
                    # Se guarda: ...se defendió del ataque.
                    result = lang.pkm_defend
                
                # Si el resultado es menor a 0
                else:
                    # Se guarda: ...esquivó el ataque.
                    result = lang.pkm_avoid
                    
                # Se muestra: Pero tu [Pokemon] [{esquivó/se defendió}, del ataque]
                self.battle_log2.config(text=f"{lang.pkm_action_fail} {lang.player_pref.lower()} {player_pkm.name} {result}")
        
        # Si el movimiento es de estadística
        else:
            
            def animate_act_2(): # Se anima como si fuese una acción
                original_x = self.p2_pokemon_img_label.winfo_x() # Se guarda la x original
                original_y = self.p2_pokemon_img_label.winfo_y() # Se guarda la y original
                self.p2_pokemon_img_label.place(x=original_x,y=original_y - 30) # Se mueve hacia arriba
                self.after(300, lambda: self.p2_pokemon_img_label.place(x=original_x,y=original_y)) # Se mueve hacia la posición original
        
            self.after(75, animate_act_2) # Se llama a la animación luego de un momento
            
            # Se guarda el tipo de estadística
            typeName = ""
            
            # Si el movimiento es de subir daño
            if action.type == "DMG":
                
                # Se guarda: ...daño
                typeName = lang.stat_dmg
                
            # Si el movimiento es de subir defensa
            else:
                
                # Se guarda: ...defensa
                typeName = lang.stat_def
            
            # Se realiza el movimiento
            result = rival_pkm.takeStat(action.type, action.power)
            
            # Si el resultado es mayor a 0
            if result > 0:
                
                 # Se muestra: El [Pokemon] rival aumentó su [estadística] en [valor].
                self.battle_log2.config(text=f"{lang.rival_pref} {rival_pkm.name} {lang.rival_name} {lang.pkm_stat[0]} {typeName} {lang.pkm_stat[1]} {result}")
            
            # Si el resultado es menor o igual a 0
            else:
                
                # Se muestra: Pero su [estadística] no subió más.
                self.battle_log2.config(text=f"{lang.pkm_stat_fail[0]} {typeName} {lang.pkm_stat_fail[1]}")
        
        
        # Se actualizan las estadísticas
        self.update_stats()
        
        # Si el jugador no tiene más vida
        if player_pkm.current_hp <= 0:
            rival.setScore(rival.getScore() + 1) # Se aumenta el puntaje (sin utilizar) del rival
            rival.addPokemon(player_pkm) # Se agrega el pokemon del jugador al equipo del rival
            player.removePokemon(player_pkm) # Se elimina el pokemon del equipo del jugador
            
            # Si el jugador no tiene más Pokémon
            if player.team == []:
                
                # Se muestra la pantalla de resultados
                self.controller.show_frame("ResultsFrame")
                return
            
            # Se muestra: Has sido derrotado por tu rival
            self.battle_log.config(text=lang.rival_win)
            
            # Se muestra: Te han quitado a [Pokemon] de tu equipo.
            self.battle_log2.config(text=f"{lang.rival_win_pkm[0]} {player_pkm.name} {lang.rival_win_pkm[1]}")
            
            # Se oculta el botón de acciones y se muestra el botón de continuar
            self.hide(self.btn_actions)
            self.show(self.btn_continue)
            return
        
        
        # Si el jugador aún tiene vida, se continua el juego
        self.after(3000, lambda: (
            self.battle_log.config(text=lang.default_action_turn),
            self.battle_log2.config(text=""),
            self.btn_actions.config(state="normal")
        ))
    
    
    # Función para actualizar las estadísticas
    def update_stats(self):
        
        # Se obtiene y se muestra la vida del pokemon del jugador
        self.p1_health.config(text=f"{lang.health_label}: {self.controller.player.getCurrentPokemon().current_hp}/{self.controller.player.getCurrentPokemon().hp}")
        
        # Se obtiene y se muestra la vida del pokemon del rival
        self.p2_health.config(text=f"{lang.health_label}: {self.controller.rival.getCurrentPokemon().current_hp}/{self.controller.rival.getCurrentPokemon().hp}")
    
    
    
    # Función para actualizar los datos en el frame
    def update_display(self):
        
        # Se habilita el botón de acciones
        self.btn_actions.config(state="normal")
        
        # Se limpian los mensajes
        self.battle_log.config(text=lang.default_action_turn)
        self.battle_log2.config(text="")
        
        # Se oculta el botón de continuar y se muestra el botón de acciones
        self.show(self.btn_actions)
        self.hide(self.btn_continue)
        
        # Se llama al modelo del jugador y su pokemon
        player = self.controller.player
        current_pokemon = self.controller.player.getCurrentPokemon()
        
        # Se muestra el nombre del jugador
        self.p1_title.config(text=f"{lang.player_label}: {player.getName()}")
        
        # Se muestra el avatar del jugador
        self.p1_img = tk.PhotoImage(file=player.getAvatar()).subsample(2, 2)
        self.p1_img_label.config(image=self.p1_img)
        
        # Se muestra el pokemon seleccionado del jugador
        self.p1_pokemon_img = tk.PhotoImage(file=current_pokemon.img).subsample(2, 2)
        self.p1_pokemon_img_label.config(image=self.p1_pokemon_img)
        
        # Se muestra el nombre del pokemon seleccionado del jugador
        self.p1_pokemon.config(text=f"{lang.pokemon_label}: {current_pokemon.name}")
        self.p1_health.config(text=f"{lang.health_label}: {current_pokemon.current_hp}/{current_pokemon.hp}")
        
        
        # Se llama al modelo del rival y su pokemon
        rival = self.controller.rival
        current_rival_pokemon = self.controller.rival.getCurrentPokemon()
        
        # Se muestra el nombre del rival
        self.p2_title.config(text=f"{lang.player_label}: {rival.getName()}")
        
        # Se muestra el avatar del rival
        self.p2_img = tk.PhotoImage(file=rival.getAvatar()).subsample(2, 2)
        self.p2_img_label.config(image=self.p2_img)
        
        # Se muestra el pokemon seleccionado del rival
        self.p2_pokemon_img = tk.PhotoImage(file=current_rival_pokemon.img).subsample(2, 2)
        self.p2_pokemon_img_label.config(image=self.p2_pokemon_img)
        
        # Se muestra el nombre del pokemon seleccionado del rival
        self.p2_pokemon.config(text=f"{lang.pokemon_label}: {current_rival_pokemon.name}")
        self.p2_health.config(text=f"{lang.health_label}: {current_rival_pokemon.current_hp}/{current_rival_pokemon.hp}")
        
        
        # Se muestran los movimientos según el pokemon seleccionado
        self.actionBtn1.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[0].name}")
        self.actionBtn2.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[1].name}")
        self.actionBtn3.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[2].name}")
        self.actionBtn4.config(text=f"A: {self.controller.player.getCurrentPokemon().moveset[3].name}")