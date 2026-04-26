
# --- Pantalla de la ronda ---

# Aquí se muestran el jugador y el puntaje actual
# y se le pide al jugador escoger un pokemon para
# pelear durante esta ronda.

# Imports necesarios
import random as random

from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang().roundScreen # Se necesita únicamente el diccionario de este frame

# Importar estilos
from assets.styles import Style
style = Style()

# Importar lista de Pokémon
# Esta se usará para mostrarla en las listas seleccionables
from assets.data.pokemon_list import PokemonList
pokemon_list = PokemonList()


# Se define la clase del frame
class RoundFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"]) # Se hereda el controlador
        
        # --- Banner ---
        
        banner = tk.Frame(
            self,
            bg=style.colors["round_bg"],
            height=10
        )
        banner.pack(fill="x")
        
        # --- Banner ---
        
        
        
        # --- Body ---
        
        body = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        body.pack(pady=20, padx=20)
        
        # Título
        self.round_title = self.create_title(
            body,
            lang.title
        )
        self.round_title.pack(pady=10)
        
        # Descripción
        self.create_text1(
            body,
            lang.description,
            10,
            5,
            600
        ).pack(pady=10)
        
        # Contenedor izquierdo
        leftGroup = tk.Frame(body, bg=style.colors["default"])
        leftGroup.pack(side="left", padx=10)
        
        # Contenedor derecho
        rightGroup = tk.Frame(body, bg=style.colors["default"])
        rightGroup.pack(side="right", padx=10)
        
        
        # -- Jugador actual
        
        # Imagen del jugador
        self.player_img = tk.PhotoImage(
            file="assets/img/char_01.png"
        ).subsample(2, 2) # Se utiliza subsample para reducir el tamaño de la imagen
        
        # Etiqueta de la imagen
        self.player_img_label = tk.Label(
            leftGroup,
            image=self.player_img,
            bg=style.colors["default"]
        )
        self.player_img_label.pack(pady=5)
        
        # Nombre del jugador
        self.player_name_label = self.create_text1(
            leftGroup,
            f"{lang.player_label}: {lang.default}",
            0,
            5,
            400
        )
        self.player_name_label.pack(pady=5)
        
        # Puntaje del jugador
        self.player_score_label = self.create_text1(
            leftGroup,
            f"{lang.score_label}: {lang.default}",
            0, 
            5, 
            400
        )
        self.player_score_label.pack(pady=5)
        
        
        # -- Pokemon seleccionado
        
        # Imagen del pokemon
        self.pokemon_img = tk.PhotoImage(
            file="assets/img/pkm0.png"
        ).subsample(2, 2)
        
        # Etiqueta de la imagen
        self.pokemon_img_label = tk.Label(
            rightGroup,
            image=self.pokemon_img,
            bg=style.colors["default"]
        )
        self.pokemon_img_label.pack(pady=5)
        
        # Selector del pokemon
        self.pokemon_combo = ttk.Combobox(
            rightGroup,
            values=pokemon_list.getNames(), # Lista por defecto que será reemplazada por el equipo actual
            font=style.a16,
            state="readonly",
            width=10
        )
        self.pokemon_combo.pack(pady=10)
        
        # Se le asigna una función al selector
        self.pokemon_combo.bind(
            "<<ComboboxSelected>>",
            # Esta función revisa que el pokemon seleccionado sea válido
            lambda e: self.checkSelection(self.pokemon_combo, self.pokemon_img_label)
        )
        
        
        # Contenedor de botones
        btn_frame = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        btn_frame.pack(pady=20)
        
        # Botón de continuar
        self.create_button1(
            btn_frame,
            lang.continue_button,
            self.continue_round
        ).pack(padx=5)
        
        # Mensaje de error
        self.error_txt = self.create_text1(
            self,
            "",
            10,
            5,
            600
        )
        
        
    # Función para continuar la ronda
    def continue_round(self):
        selected = self.pokemon_combo.get() # Se obtiene el pokemon seleccionado
        
        if selected == "": # Mensaje de error si no se ha seleccionado un pokemon
            self.error_txt.config(text=lang.error_select)
            self.show(self.error_txt)
            return
        
        # Se oculta el mensaje de error
        self.hide(self.error_txt)
        
        # Se cambia el pokemon actual
        self.controller.player.setCurrentPokemon(self.controller.player.team[self.pokemon_combo.current()])
        
        # Se cambia el pokemon del rival
        self.controller.rival.setCurrentPokemon(self.controller.rival.team[random.randint(0, len(self.controller.rival.team) - 1)])
        
        # Se pasa a la pantalla de juego
        self.controller.show_frame("GameFrame")
        
    
    # Función para revisar que el pokemon seleccionado sea valido
    def checkSelection(self, element, image):
        pkm = pokemon_list.getPokemon(element.get()) # Se obtiene el Pokémon seleccionado
        new_img = tk.PhotoImage(file=pkm.img).subsample(2, 2) # Se obtiene la imagen del Pokémon
        image.config(image=new_img) # Se muestra la imagen
        image.image = new_img
    
    
    # Función para actualizar los datos en el frame
    def update_display(self):
        player = self.controller.player # Se obtiene el jugador
        
        # Se obtiene el avatar del jugador
        self.player_img = tk.PhotoImage(file=player.getAvatar()).subsample(2, 2)
        self.player_img_label.config(image=self.player_img)
        
        # Se obtiene el nombre del jugador
        self.player_name_label.config(text=f"{lang.player_label}: {player.getName()}")
        
        # Se obtiene el puntaje del jugador
        self.player_score_label.config(text=f"{lang.score_label}: {player.getScore()}")
        
        # Se limpia el selector
        self.pokemon_combo.set("")
        self.pokemon_img = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.pokemon_img_label.config(image=self.pokemon_img)
        
        # Se obtiene el equipo actual del jugador
        team = player.getTeam()
        
        # Se obtienen los nombres de los Pokémon
        teamNames = [pokemon.name for pokemon in team]
        
        # Se actualiza el selector con el equipo actual
        self.pokemon_combo.config(values=teamNames)
        
        # Se muestra el contador de la ronda actual
        self.round_title.config(text=f"{lang.title} {self.controller.round_number}")
        
        # Se reinician las estadísticas de cada pokemon
        for pokemon in self.controller.player.team:
                pokemon.current_hp = pokemon.hp
                pokemon.current_attack = pokemon.attack
                pokemon.current_defense = pokemon.defense
        
        # Se reinician las estadísticas de cada pokemon rival
        for pokemon in self.controller.rival.team:
                pokemon.current_hp = pokemon.hp
                pokemon.current_attack = pokemon.attack
                pokemon.current_defense = pokemon.defense