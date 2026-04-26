
# --- Pantalla del lobby ---

# Aquí se le pide al usuario su
# nombre, avatar y equipo.
# Después se inicia el juego.

# Imports necesarios
import random as random
from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang().lobbyScreen # Se necesita únicamente el diccionario de este frame

# Importar estilos
from assets.styles import Style
style = Style()

# Importar lista de Pokémon
# Esta se usará para mostrarla en las listas seleccionables
from assets.data.pokemon_list import PokemonList
pokemon_list = PokemonList()



# Se define la clase del frame
class LobbyFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"]) # Se hereda de StyledFrame
        
        # --- Banner ---
        
        banner = tk.Frame(
            self,
            bg=style.colors["lobby_bg"],
            height=10
        )
        banner.pack(fill="x")
        
        # --- Banner ---
        
        # --- Body ---
        
        # Contenedor principal
        split_frame = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        split_frame.pack(fill="both", expand=True, pady=20)
        
        # Configuración de las columnas
        split_frame.grid_columnconfigure(0, weight=33)
        split_frame.grid_columnconfigure(1, weight=33)
        split_frame.grid_columnconfigure(2, weight=33)


        # -- Body izquierdo|...|... --
        
        # Contenedor izquierdo
        left = tk.Frame(
            split_frame,
            bg=style.colors["default"]
        )
        left.grid(row=0, column=0, sticky="nsew")
        
        # Título
        self.create_title(left, lang.title).pack(pady=10)
        self.create_text1(left, lang.description, 10, 5, 400).pack(pady=10)
        
        # Contenedor para el campo de texto
        form_name = tk.Frame(
            left,
            bg=style.colors["default"]
        )
        form_name.pack(pady=20)
        
        # Campo de texto para el nombre
        tk.Label(
            form_name,
            text=f"{lang.name_label}:",
            bg=style.colors["default"],
            font=style.a14
        ).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        # Entrada de texto
        self.name_entry = tk.Entry(
            form_name,
            font=style.a14
        )
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Botón para continuar
        self.name_next_btn = self.create_button1(
            left, 
            lang.next_button,
            self.checkName
        )
        self.name_next_btn.pack(pady=10)
        
        # Texto de error
        self.name_error_txt = self.create_text1(
            left,
            "",
            10,
            5,
            400
        )
        
        # -- Body izquierdo|...|... --
        
        
        # -- ...|Body central|... --
        
        # Contenedor central
        middle = tk.Frame(
            split_frame,
            bg=style.colors["default"]
        )
        middle.grid(row=0, column=1, sticky="nsew")
        
        # Contenedor para el avatar
        self.form_avatar = tk.Frame(
            middle,
            bg=style.colors["default"]
        )
        
        # Título
        self.create_title(
            self.form_avatar,
            lang.avatar_title
        ).pack(pady=10)
        
        # Subtítulo
        self.create_text1(
            self.form_avatar,
            lang.avatar_description,
            10,
            5,
            400
        ).pack(pady=10)
        
        # Imagen del avatar
        self.avatar_img = tk.PhotoImage(
            master=self.form_avatar,
            file="assets/img/char_01.png"
        )
        
        # Etiqueta de la imagen
        self.avatar_img_label = tk.Label(
            self.form_avatar,
            image=self.avatar_img,
            bg=style.colors["default"]
        )
        self.avatar_img_label.pack(pady=10)
        
        # Contenedor para los botones de cambiar avatar
        avatar_btn_group = tk.Frame(
            self.form_avatar,
            bg=style.colors["default"]
        )
        avatar_btn_group.pack()
        
        # --- Botones
        # Botón para avatar anterior
        self.imgBackBtn = self.create_button1(
            avatar_btn_group,
            lang.avatar_back,
            self.backAvatar # Función para desplazar avatares
        )
        self.imgBackBtn.pack(pady=10, padx=5, side="left")
        
        # Botón para avatar siguiente
        self.imgNextBtn = self.create_button1(
            avatar_btn_group,
            lang.avatar_next,
            self.nextAvatar # Función para desplazar avatares
        )
        self.imgNextBtn.pack(pady=10, padx=5, side="right")
        
        # Botón para continuar
        self.avatar_next_btn = self.create_button1(
            self.form_avatar,
            lang.next_button,
            self.checkAvatar
        )
        self.avatar_next_btn.pack(pady=10)
        
        
        # -- ...|Body central|... --
        
        
        # -- ...|...|Body derecho --
        
        # Contenedor derecho
        right = tk.Frame(
            split_frame,
            bg=style.colors["default"]
        )
        right.grid(row=0, column=2, sticky="nsew")
        
        # Contenedor para el equipo
        self.form_team = tk.Frame(
            right,
            bg=style.colors["default"]
        )
        
        # Título
        self.create_title(
            self.form_team,
            lang.team_title
        ).pack(pady=10)
        
        # Subtítulo
        self.create_text1(
            self.form_team,
            lang.team_description,
            10,
            5,
            400
        ).pack(pady=10)
        
        # Fila de los primeros dos pokemons
        team_row1 = tk.Frame(
            self.form_team,
            bg=style.colors["default"]
        )
        team_row1.pack()
        
        # Grupo del primer pokemon
        self.group_team_1 = tk.Frame(
            team_row1,
            bg=style.colors["default"]
        )
        self.group_team_1.pack(side="left", padx=5)
        
        # Imagen del primer pokemon
        self.img_team_1 = tk.PhotoImage(
            master=self.group_team_1,
            file="assets/img/pkm0.png"
        ).subsample(2, 2) # Se utiliza subsample para reducir el tamaño de la imagen
        
        # Etiqueta de la imagen
        self.img_team_1_label = tk.Label(
            self.group_team_1,
            image=self.img_team_1,
            bg=style.colors["default"]
        )
        self.img_team_1_label.pack(pady=10, side="top")

        # Selector del primer pokemon
        self.select_team_1 = ttk.Combobox(
            self.group_team_1,
            values=pokemon_list.getNames(),
            font=style.a16,
            state="readonly" # Se utiliza readonly para evitar ingresar datos inválidos
            )
        self.select_team_1.pack(pady=10, side="top")
        
        # Se le asigna una función a la selección del combobox (Event listener)
        self.select_team_1.bind(
            "<<ComboboxSelected>>",
            # Esta función verifica que el pokemon no esté repetido y sea válido
            lambda e: self.checkSelection(self.select_team_1, self.img_team_1_label)
        )
        
        # Grupo del segundo pokemon
        self.group_team_2 = tk.Frame(
            team_row1,
            bg=style.colors["default"]
        )
        self.group_team_2.pack(side="right", padx=5)
        
        # Imagen del segundo pokemon
        self.img_team_2 = tk.PhotoImage(
            master=self.group_team_2,
            file="assets/img/pkm0.png"
        ).subsample(2, 2)
        
        # Etiqueta de la imagen
        self.img_team_2_label = tk.Label(
            self.group_team_2,
            image=self.img_team_2,
            bg=style.colors["default"]
        )
        self.img_team_2_label.pack(pady=10, side="top")
        
        # Selector del segundo pokemon
        self.select_team_2 = ttk.Combobox(
            self.group_team_2,
            values=pokemon_list.getNames(),
            font=style.a16,
            state="readonly"
        )
        self.select_team_2.pack(pady=10, side="top")
        
        # Se le asigna una función a la selección del combobox (Event listener)
        self.select_team_2.bind(
            "<<ComboboxSelected>>",
            lambda e: self.checkSelection(self.select_team_2, self.img_team_2_label)
        )
        
        
        # Fila del tercer pokemon
        team_row2 = tk.Frame(
            self.form_team,
            bg=style.colors["default"]
        )
        team_row2.pack()
        
        # Grupo del tercer pokemon
        self.group_team_3 = tk.Frame(
            team_row2, 
            bg=style.colors["default"]
        )
        self.group_team_3.pack(side="right", padx=5)
        
        # Imagen del tercer pokemon
        self.img_team_3 = tk.PhotoImage(
            master=self.group_team_3,
            file="assets/img/pkm0.png"
        ).subsample(2, 2)
        
        # Etiqueta de la imagen
        self.img_team_3_label = tk.Label(
            self.group_team_3,
            image=self.img_team_3,
            bg=style.colors["default"]
        )
        self.img_team_3_label.pack(pady=10, side="top")
        
        # Selector del tercer pokemon
        self.select_team_3 = ttk.Combobox(
            self.group_team_3,
            values=pokemon_list.getNames(),
            font=style.a16,
            state="readonly"
        )
        self.select_team_3.pack(pady=10, side="top")
        
        # Se le asigna una función a la selección del combobox (Event listener)
        self.select_team_3.bind(
            "<<ComboboxSelected>>",
            lambda e: self.checkSelection(self.select_team_3, self.img_team_3_label)
        )
        
        # Botón de avanzar
        self.team_next_btn = self.create_button1(
            self.form_team,
            lang.next_button,
            self.checkTeam # Esta función verifica el equipo y continúa
        )
        self.team_next_btn.pack(pady=10)
        
        # Mensaje de error
        self.team_error_txt = self.create_text1(
            self.form_team,
            "",
            10,
            5,
            400
        )
        
        # -- ...|...|Body derecho --
        
        
    
    # Función para verificar que el nombre sea válido
    def checkName(self):
        name = self.name_entry.get() # Se obtiene el nombre de la entrada
        
        if name == "": # Si el nombre esta vacio
            self.name_error_txt.config(text=lang.error_empty_name)
            self.show(self.name_error_txt)
            return
        
        elif len(name) < 3: # Si el nombre es muy corto
            self.name_error_txt.config(text=lang.error_name_too_short)
            self.show(self.name_error_txt)
            return
        
        elif len(name) > 15: # Si el nombre es muy largo
            self.name_error_txt.config(text=lang.error_name_too_long)
            self.show(self.name_error_txt)
            return
        
        self.hide(self.name_error_txt) # Se oculta el mensaje de error
        
        self.controller.player.setName(name) # Se asigna el nombre al modelo del jugador
        self.controller.rival.setName(self.controller.rival_name) # Se asigna el nombre al modelo del rival
        
        # Se deshabilita el campo de nombre
        self.name_entry.config(state="disabled")
        self.name_next_btn.config(state="disabled")
        
        # Se habilita el selector de avatar
        self.imgBackBtn.config(state="normal")
        self.imgNextBtn.config(state="normal")
        self.avatar_next_btn.config(state="normal")
        
        self.show(self.form_avatar) # Se muestran la siguiente sección para escoger el avatar
    
    # Lista de avatares predefinidos
    avatarList = [
        "assets/img/char_01.png",
        "assets/img/char_02.png",
        "assets/img/char_03.png",
        "assets/img/char_04.png",
        "assets/img/char_11.png",
        "assets/img/char_12.png",
        "assets/img/char_13.png",
        "assets/img/char_14.png"
    ]
    avatarCounter = 0 # Variable de control para el selector de avatares
    
    # Función para volver al avatar anterior
    def backAvatar(self):
        
        if self.avatarCounter == 0: # Se evitan valores inválidos
            self.avatarCounter = len(self.avatarList) - 1
        else:
            self.avatarCounter -= 1
            
        # Se asigna el índice actual de la variable de control
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file=self.avatarList[self.avatarCounter])
        self.avatar_img_label.config(image=self.avatar_img)
        
        
    # Función para avanzar al siguiente avatar
    def nextAvatar(self):
        
        if self.avatarCounter == len(self.avatarList) - 1: # Se evitan valores inválidos
            self.avatarCounter = 0
        else:
            self.avatarCounter += 1
            
        # Se asigna el índice actual de la variable de control
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file=self.avatarList[self.avatarCounter])
        self.avatar_img_label.config(image=self.avatar_img)
        
        
    # Función para escoger el avatar
    def checkAvatar(self):
        self.controller.player.setAvatar(self.avatarList[self.avatarCounter]) # Se asigna el avatar al modelo del jugador
        self.controller.rival.setAvatar(self.avatarList[random.randint(0, len(self.avatarList) - 1)]) # Se asigna un avatar aleatorio al modelo del rival
        
        # Se deshabilita el selector de avatar
        self.imgBackBtn.config(state="disabled")
        self.imgNextBtn.config(state="disabled")
        self.avatar_next_btn.config(state="disabled")
        
        # Se habilita el selector de equipo
        self.team_next_btn.config(state="normal")
        
        # Se muestra la sección para escoger el equipo
        self.show(self.form_team)
        
    
    # Función para mostrar el pokemon seleccionado
    def checkSelection(self, element, image):
        pkm = pokemon_list.getPokemon(element.get()) # Se obtiene el Pokémon seleccionado
        new_img = tk.PhotoImage(file=pkm.img).subsample(2, 2) # Se obtiene la imagen del Pokémon
        image.config(image=new_img) # Se muestra la imagen
        image.image = new_img
    
    
    # Función para escoger el equipo
    def checkTeam(self):
        
        # Se obtienen los pokemones seleccionados
        pokemon1 = self.select_team_1.get()
        pokemon2 = self.select_team_2.get()
        pokemon3 = self.select_team_3.get()
        
        # Se evitan valores inválidos
        if pokemon1 == "" or pokemon2 == "" or pokemon3 == "":
            self.team_error_txt.config(text=lang.error_select_pokemon)
            self.show(self.team_error_txt)
            return
        
        # Se evitan pokemones duplicados
        if pokemon1 == pokemon2 or pokemon2 == pokemon3 or pokemon3 == pokemon1:
            self.team_error_txt.config(text=lang.error_duplicate_pokemon)
            self.show(self.team_error_txt)
            return
        
        # Se asignan los pokemones al equipo
        self.controller.player.setTeam([
            pokemon_list.getPokemon(pokemon1),
            pokemon_list.getPokemon(pokemon2),
            pokemon_list.getPokemon(pokemon3)
        ])
        
        # Se asigna un equipo aleatorio al rival
        self.controller.rival.setTeam([
            
            # Se utiliza clone para evitar que afecte al equipo del jugador
            pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)].clone(),
            pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)].clone(),
            pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)].clone()
        ])
        
        # Se ocultan las secciones
        self.hide(self.team_error_txt)
        self.hide(self.form_team)
        self.hide(self.form_avatar)
        
        # Se habilitan los botones para siguientes rondas
        self.name_entry.config(state="normal")
        self.name_next_btn.config(state="normal")
        
        # Se muestra la pantalla de ronda
        self.controller.show_frame("RoundFrame")
        
        
    # Función para actualizar los datos
    def update_display(self):
        
        # Se limpian los datos del jugador
        self.controller.player.setName("")
        self.controller.player.setAvatar("assets/img/char_01.png")
        self.controller.player.setTeam([])
        self.controller.player.setCurrentPokemon(None)
        self.controller.player.setScore(0)

        # Se limpian los datos del rival
        self.controller.rival.setName("")
        self.controller.rival.setAvatar("assets/img/char_11.png")
        self.controller.rival.setTeam([])
        self.controller.rival.setCurrentPokemon(None)
        self.controller.rival.setScore(0)

        # Se reinicia el contador de rodnas
        self.controller.round_number = 1
        
        # Se limpia el campo del nombre
        self.name_entry.delete(0, tk.END)
        self.name_error_txt.config(text="")
        
        # Se limpian los avatares seleccionados
        self.avatarCounter = 0
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file=self.avatarList[self.avatarCounter])
        self.avatar_img_label.config(image=self.avatar_img)
        self.team_error_txt.config(text="")

        # Se deshabilitan los botones siguientes
        self.imgBackBtn.config(state="disabled")
        self.imgNextBtn.config(state="disabled")
        self.avatar_next_btn.config(state="disabled")
        self.team_next_btn.config(state="disabled")
        
        # Se ocultan las secciones siguientes
        self.hide(self.form_avatar)
        self.hide(self.form_team)
        
        # Se limpian los equipos
        self.select_team_1.set("")
        self.select_team_2.set("")
        self.select_team_3.set("")
        self.img_team_1 = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.img_team_1_label.config(image=self.img_team_1)
        self.img_team_2 = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.img_team_2_label.config(image=self.img_team_2)
        self.img_team_3 = tk.PhotoImage(file="assets/img/pkm0.png").subsample(2, 2)
        self.img_team_3_label.config(image=self.img_team_3)
        
        