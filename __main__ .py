from assets.classes import tk
from assets.classes import ttk

# Importar secciones
from assets.title_screen import IntroFrame
from assets.lobby_screen import LobbyFrame
from assets.round_screen import RoundFrame
from assets.game_screen import GameFrame
from assets.results_screen import ResultsFrame
from assets.halloffame_screen import HallOfFameFrame

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()

# Importar modelo del jugador
from assets.classes import Player

class Main:
    def __init__(self, root):
        
        self.player = Player()
        self.rival = Player()
        self.round_number = 1
        
        #Configuración general
        self.root = root
        self.root.title(lang.title)
        width = 800
        height = 600
        self.root.geometry(f"{width}x{height}+{int(self.root.winfo_screenwidth()/2-width/2)}+{int(self.root.winfo_screenheight()/2-height/2)}")
        self.root.attributes("-fullscreen", True)
        self.root.resizable(False, False)
        self.root.configure(bg=style.colors["default"])

        # --- Header ---
        # Base del header
        self.main_header = tk.Frame(
            root,
            bg=style.colors["main_blue"],
            height=60
            )
        self.main_header.pack(fill="x")
        
        # Logo
        self.header_logo = tk.PhotoImage(
            master=self.main_header,
            file="assets/img/logo.png",
            width=70,
            height=70
            )
        
        self.header_img = tk.Label(
            self.main_header,
            image=self.header_logo,
            bg=style.colors["main_blue"]
            )
        self.header_img.pack(side="left", padx=(20, 0), pady=0)
        
        # Título
        self.header_label = tk.Label(
            self.main_header,
            text=lang.title,
            bg=style.colors["main_blue"],
            fg=style.colors["default"],
            font=style.A24
            )
        self.header_label.pack(
            side="left",
            padx=10,
            pady=20
            )

        # Botón de salir
        btn_exit = tk.Button(
            self.main_header,
            text="X",
            bg=style.colors["exit"],
            fg=style.colors["default"],
            font=style.A18,
            padx=12,
            pady=5,
            relief="groove",
            cursor="hand2", 
            command=lambda: self.root.destroy()
            )
        btn_exit.pack(
            side="right", 
            pady=20, 
            padx=20
            )
        
        # --- Header ---
        
        
        
        # --- Body ---
        
        # Base principal
        self.container = tk.Frame(
            root,
            bg=style.colors["default"]
            )
        self.container.pack(
            fill="both",
            expand=True
            )

        # Llamada a todos los frames
        self.screens = {}
        for screen in (IntroFrame, LobbyFrame, RoundFrame, GameFrame, ResultsFrame, HallOfFameFrame):
            page_name = screen.__name__
            screenFrame = screen(parent=self.container, controller=self)
            self.screens[page_name] = screenFrame
            screenFrame.grid(row=0, column=0, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Primer frame
        self.show_frame("IntroFrame")
    
        # --- Body ---
        
        
            
        # --- Footer ---
        
        # Base del footer
        self.main_footer = tk.Frame(root, bg=style.colors["main_blue"], height=60)
        self.main_footer.pack(fill="x")
        
        # Copyright
        self.footer_copyright = tk.Label(
            self.main_footer,
            text=lang.copyright,
            bg=style.colors["main_blue"],
            fg=style.colors["default"],
            font=style.a12
            )
        self.footer_copyright.pack(
            side="top",
            pady=15)
        
        # --- Footer ---
        
        
        
    # Función para cambiar de frame
    def show_frame(self, page_name):
        frame = self.screens[page_name]
        frame.tkraise()
        # Call update method if it exists
        if hasattr(frame, 'update_display'):
            frame.update_display()

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()