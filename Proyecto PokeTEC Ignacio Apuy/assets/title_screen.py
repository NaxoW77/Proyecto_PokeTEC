from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

class IntroFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"])
        
        # --- Banner ---
        banner = tk.Frame(self, bg=style.colors["intro_bg"], height=10)
        banner.pack(fill="x")
        # --- Banner ---
        
        
        
        # --- Body|Body ---
        split_frame = tk.Frame(self, bg=style.colors["default"])
        split_frame.pack(fill="both", expand=True, pady=20)
        split_frame.grid_columnconfigure(0, weight=15)
        split_frame.grid_columnconfigure(1, weight=85)

        # -- Body|... --
        left = tk.Frame(split_frame, bg=style.colors["default"])
        left.grid(row=0, column=0, sticky="nsew")
        
        # Título
        self.create_title(left, lang.titleScreen.title).pack()
        
        # Descripción
        self.create_text1(left, lang.titleScreen.description,55, 5, 500).pack(side="top",pady=(0, 20))
        
        # Imagen
        self.demo_img = tk.PhotoImage(
            master=left,
            file="assets/img/demo.png",
            )
        
        self.demo_img_label = tk.Label(
            left,
            image=self.demo_img,
            bg=style.colors["main_blue"]
            )
        self.demo_img_label.pack(side="top", padx=(0, 0), pady=0)
        
        # -- Body|... --
        
        
        # -- ...|Body --
 
        right = tk.Frame(split_frame, bg=style.colors["default"])
        right.grid(row=0, column=1, sticky="nsew")
        
        # Subtítulo
        self.create_title(right, lang.titleScreen.subtitle).pack()
        
        # Instrucciones
        self.create_text2(right, lang.titleScreen.instructions,10, 5, 800, "center").pack()

        btn_container = tk.Frame(self, bg=style.colors["default"])
        btn_container.pack(side="bottom", fill="x", pady=20)
        
        btn_group = tk.Frame(btn_container, width=200, bg=style.colors["default"])
        btn_group.pack(side="bottom", padx=5)
        self.create_button1(btn_group,"Jugar", lambda: controller.show_frame("LobbyFrame")).pack(side="left", padx=5)
        self.create_button1(btn_group,"Salón de la Fama", lambda: controller.show_frame("HallOfFameFrame")).pack(side="right", padx=5)