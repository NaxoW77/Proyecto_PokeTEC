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

class LobbyFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["lobby_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        # --- Body|Body|Body ---
        split_frame = tk.Frame(self, bg=style.colors["default"])
        split_frame.pack(fill="both", expand=True, pady=20)
        split_frame.grid_columnconfigure(0, weight=33)
        split_frame.grid_columnconfigure(1, weight=33)
        split_frame.grid_columnconfigure(2, weight=33)

        # -- Body|...|... --
        left = tk.Frame(split_frame, bg=style.colors["default"])
        left.grid(row=0, column=0, sticky="nsew")
        
        # Título
        self.create_title(left, lang.lobbyScreen.title).pack(pady=10)
        self.create_text1(left, lang.lobbyScreen.description, 10, 5, 400).pack(pady=10)
        
        form_name = tk.Frame(left, bg=style.colors["default"])
        form_name.pack(pady=20)
        
        tk.Label(form_name, text=lang.lobbyScreen.name_label, bg=style.colors["default"], font=style.a14).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(form_name, font=style.a14)
        
        self.name_next_btn = self.create_button1(left, lang.lobbyScreen.next_button, self.checkName)
        self.name_next_btn.pack(pady=10)
        
        self.name_error_txt = self.create_text1(left, "", 10, 5, 400)
        
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # -- Body|...|... --
        
        
        
        # -- ...|Body|... --
        middle = tk.Frame(split_frame, bg=style.colors["default"])
        middle.grid(row=0, column=1, sticky="nsew")
        
        self.form_avatar = tk.Frame(middle, bg=style.colors["default"])
        
        self.create_title(self.form_avatar, lang.lobbyScreen.avatar_title).pack(pady=10)
        self.create_text1(self.form_avatar, lang.lobbyScreen.avatar_description, 10, 5, 400).pack(pady=10)
        
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file="assets/img/char_01.png")
        self.avatar_img_label = tk.Label(self.form_avatar, image=self.avatar_img, bg=style.colors["default"])
        self.avatar_img_label.pack(pady=10)
        
        avatar_btn_group = tk.Frame(self.form_avatar, bg=style.colors["default"])
        avatar_btn_group.pack()
        
        self.imgBackBtn = self.create_button1(avatar_btn_group, lang.lobbyScreen.avatar_back, self.backAvatar)
        self.imgBackBtn.pack(pady=10, padx=5, side="left")
        self.imgNextBtn = self.create_button1(avatar_btn_group, lang.lobbyScreen.avatar_next, self.nextAvatar)
        self.imgNextBtn.pack(pady=10, padx=5, side="right")
        
        self.avatar_next_btn = self.create_button1(self.form_avatar, lang.lobbyScreen.next_button, self.checkAvatar)
        self.avatar_next_btn.pack(pady=10)
        
        
        # -- ...|Body|... --
        
        
        
        # -- ...|...|Body --
        right = tk.Frame(split_frame, bg=style.colors["default"])
        right.grid(row=0, column=2, sticky="nsew")
        
        self.form_team = tk.Frame(right, bg=style.colors["default"])
        
        self.create_title(self.form_team, lang.lobbyScreen.team_title).pack(pady=10)
        self.create_text1(self.form_team, lang.lobbyScreen.team_description, 10, 5, 400).pack(pady=10)
        
        team_row1 = tk.Frame(self.form_team, bg=style.colors["default"])
        team_row1.pack()
        
        group_team_1 = tk.Frame(team_row1, bg=style.colors["default"])
        group_team_1.pack(side="right", padx=5)
        
        self.img_team_1 = tk.PhotoImage(master=group_team_1, file="assets/img/pkm0.png", width=100, height=100)
        self.img_team_1_label = tk.Label(group_team_1, image=self.img_team_1, bg=style.colors["default"])
        self.img_team_1_label.pack(pady=10, side="top")

        
        self.select_team_1 = ttk.Combobox(group_team_1, values=pokemon_list.getNames(), font=style.a16, state="readonly")
        self.select_team_1.pack(pady=10, side="top")
        self.select_team_1.bind("<<ComboboxSelected>>", lambda e: self.checkSelection(self.select_team_1, self.img_team_1))
        
        
        group_team_2 = tk.Frame(team_row1, bg=style.colors["default"])
        group_team_2.pack(side="left", padx=5)
        
        self.img_team_2 = tk.PhotoImage(master=group_team_2, file="assets/img/pkm0.png", width=100, height=100)
        self.img_team_2_label = tk.Label(group_team_2, image=self.img_team_2, bg=style.colors["default"])
        self.img_team_2_label.pack(pady=10, side="top")
        
        self.select_team_2 = ttk.Combobox(group_team_2, values=pokemon_list.getNames(), font=style.a16, state="readonly")
        self.select_team_2.pack(pady=10, side="top")
        self.select_team_2.bind("<<ComboboxSelected>>", lambda e: self.checkSelection(self.select_team_2, self.img_team_2))
        
        team_row2 = tk.Frame(self.form_team, bg=style.colors["default"])
        team_row2.pack()
        
        group_team_3 = tk.Frame(team_row2, bg=style.colors["default"])
        group_team_3.pack(side="right", padx=5)
        
        self.img_team_3 = tk.PhotoImage(master=group_team_3, file="assets/img/pkm0.png", width=100, height=100)
        self.img_team_3_label = tk.Label(group_team_3, image=self.img_team_3, bg=style.colors["default"])
        self.img_team_3_label.pack(pady=10, side="top")
        
        self.select_team_3 = ttk.Combobox(group_team_3, values=pokemon_list.getNames(), font=style.a16, state="readonly")
        self.select_team_3.pack(pady=10, side="top")
        self.select_team_3.bind("<<ComboboxSelected>>", lambda e: self.checkSelection(self.select_team_3, self.img_team_3))
        
        self.team_next_btn = self.create_button1 (self.form_team, lang.lobbyScreen.next_button, self.checkTeam)
        self.team_next_btn.pack(pady=10)
        
        self.team_error_txt = self.create_text1(self.form_team, "", 10, 5, 400)
        
        # -- ...|...|Body --
        
    def checkName(self):
        name = self.name_entry.get()
        if name == "":
            self.name_error_txt.config(text=lang.lobbyScreen.error_empty_name)
            self.show(self.name_error_txt)
            return
        elif len(name) < 3:
            self.name_error_txt.config(text=lang.lobbyScreen.error_name_too_short)
            self.show(self.name_error_txt)
            return
        elif len(name) > 15:
            self.name_error_txt.config(text=lang.lobbyScreen.error_name_too_long)
            self.show(self.name_error_txt)
            return
        
        self.hide(self.name_error_txt)
        
        self.controller.player.setName(name)
        self.controller.rival.setName("Rival")
        
        self.show(self.form_avatar)
        
        self.name_entry.config(state="disabled")
        self.name_next_btn.config(state="disabled")
        
        self.imgBackBtn.config(state="normal")
        self.imgNextBtn.config(state="normal")
        self.avatar_next_btn.config(state="normal")
        
    avatarList = ["assets/img/char_01.png", "assets/img/char_02.png", "assets/img/char_03.png", "assets/img/char_04.png", "assets/img/char_11.png", "assets/img/char_12.png", "assets/img/char_13.png", "assets/img/char_14.png"]
    avatarCounter = 0
    def backAvatar(self):
        if self.avatarCounter == 0:
            self.avatarCounter = len(self.avatarList) - 1
        else:
            self.avatarCounter -= 1
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file=self.avatarList[self.avatarCounter])
        self.avatar_img_label.config(image=self.avatar_img)
        
    def nextAvatar(self):
        if self.avatarCounter == len(self.avatarList) - 1:
            self.avatarCounter = 0
        else:
            self.avatarCounter += 1
        self.avatar_img = tk.PhotoImage(master=self.form_avatar, file=self.avatarList[self.avatarCounter])
        self.avatar_img_label.config(image=self.avatar_img)
        
        
        
    def checkAvatar(self):
        self.controller.player.setAvatar(self.avatarList[self.avatarCounter])
        self.controller.rival.setAvatar(self.avatarList[random.randint(0, len(self.avatarList) - 1)])
        
        self.imgBackBtn.config(state="disabled")
        self.imgNextBtn.config(state="disabled")
        self.avatar_next_btn.config(state="disabled")
        
        self.team_next_btn.config(state="normal")
        
        self.show(self.form_team)
        
    
    def checkSelection(self, element, image):
        pkm = pokemon_list.getPokemon(element.get())
        image.config(file=pkm.img)
    
        
    def checkTeam(self):
        pokemon1 = self.select_team_1.get()
        pokemon2 = self.select_team_2.get()
        pokemon3 = self.select_team_3.get()
        
        if pokemon1 == "" or pokemon2 == "" or pokemon3 == "":
            self.team_error_txt.config(text=lang.lobbyScreen.error_select_pokemon)
            self.show(self.team_error_txt)
            return
        
        if pokemon1 == pokemon2 or pokemon2 == pokemon3 or pokemon3 == pokemon1:
            self.team_error_txt.config(text=lang.lobbyScreen.error_duplicate_pokemon)
            self.show(self.team_error_txt)
            return
        
        self.controller.player.setTeam([pokemon_list.getPokemon(pokemon1), pokemon_list.getPokemon(pokemon2), pokemon_list.getPokemon(pokemon3)])
        
        self.controller.rival.setTeam([pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)], pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)], pokemon_list.list[random.randint(0, len(pokemon_list.list) - 1)]])
        
        self.hide(self.team_error_txt)
        self.hide(self.form_team)
        self.hide(self.form_avatar)
        
        self.name_entry.config(state="normal")
        self.name_next_btn.config(state="normal")
        
        self.controller.show_frame("RoundFrame")
        
        
    def hide(self, elem):
        elem.pack_forget()
    
    def show(self, elem):
        elem.pack(fill="both", expand=True)