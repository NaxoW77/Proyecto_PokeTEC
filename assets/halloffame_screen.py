
# --- Pantalla del salón de la fama ---

# Aquí se muestran los 10 mejores jugadores
# en base a su puntaje.

# Imports necesarios
import os
import json
from assets.classes import tk
from assets.classes import ttk
from assets.classes import StyledFrame

# Importar textos
from assets.lang import Lang
lang = Lang().hallOfFameScreen # Se necesita únicamente el diccionario de este frame

# Importar estilos
from assets.styles import Style
style = Style()

# Se define la clase del frame
class HallOfFameFrame(StyledFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, style.colors["default"]) # Se hereda el controlador

        # --- Configuración ---
        self.top_path = os.path.join(os.path.dirname(__file__), "data", "top.json") # Ruta del archivo de jugadores
        self.record_images = [] # Lista auxiliar de imagenes de los jugadores

        # --- Banner ---
        
        banner = tk.Frame(
            self,
            bg=style.colors["hall_of_fame_bg"],
            height=10
        )
        banner.pack(fill="x")
        
        # --- Banner ---

        # --- Body ---
        
        # Contenedor principal
        body = tk.Frame(
            self,
            bg=style.colors["default"]
        )
        body.pack(fill="both", expand=True, pady=20, padx=20)

        # Titulo
        self.create_title(
            body,
            lang.title
        ).pack(pady=10)
        
        # Descripción
        self.summary_label = self.create_text1(
            body,
            "",
            10,
            5, 
            700
        )
        self.summary_label.pack(pady=5)

        # Contenedor de la tabla
        table_frame = tk.Frame(
            body,
            bg=style.colors["default"]
        )
        table_frame.pack(fill="both", expand=True, pady=20)

        # Tabla
        self.records_canvas = tk.Canvas(
            table_frame,
            bg=style.colors["default"],
            highlightthickness=0
        )
        self.records_canvas.pack(side="left", fill="both", expand=True)

        # Barra de scroll
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical", 
            command=self.records_canvas.yview # Función de scroll en la tabla
            )
        scrollbar.pack(side="right", fill="y")

        # Configuración de la tabla
        self.records_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Contenedor de las entradas
        self.records_list_frame = tk.Frame(
            self.records_canvas,
            bg=style.colors["default"]
        )
        
        # Ventana para las entradas
        self.list_window = self.records_canvas.create_window(
            (0, 0),
            window=self.records_list_frame,
            anchor="nw"
        )

        # Función de scroll
        self.records_list_frame.bind(
            "<Configure>",
            lambda event: self.records_canvas.configure(scrollregion=self.records_canvas.bbox("all"))
        )
        
        # Función para la actualización de la tabla
        self.records_canvas.bind(
            "<Configure>",
            lambda event: self.records_canvas.itemconfig(self.list_window, width=event.width)
        )

        # Botón para volver
        self.create_button1(
            body,
            lang.back_button, 
            lambda: controller.show_frame("IntroFrame")
        ).pack(pady=20)
        
        # --- Body ---



    # Función para actualizar los datos en el frame
    def update_display(self):
        records = self.load_records() # Se llama a cargar los registros
        
        self.record_images.clear() # Se limpian las imagenes
        
        # Se limpian las entradas
        for child in self.records_list_frame.winfo_children():
            child.destroy()

        # -- Si no hay registros
        if not records:
            self.summary_label.config(text=lang.no_records) # Se muestra: "No hay registros."
            self.create_text1(
                self.records_list_frame,
                lang.default,
                10,
                10, 
                700
            ).pack(pady=20)
            return


        # -- Si hay registros
        
        # Subtítulo
        self.summary_label.config(text=f"{lang.subtitle}")

        # Se recorren los registros
        for index, record in enumerate(records, start=1):
            
            # Se crea una fila
            row = tk.Frame(
                self.records_list_frame,
                bg=style.colors["default"], 
                relief="solid",
                borderwidth=1
            )
            row.pack(fill="x", padx=5, pady=5)

            # Se busca la imagen del avatar
            avatar_file = record.get("avatar") or "assets/img/char_01.png"
            
            # Se carga la imagen
            avatar_img = tk.PhotoImage(file=avatar_file).subsample(2, 2)
            
            # Etiqueta de la imagen
            avatar_label = tk.Label(
                row,
                image=avatar_img,
                bg=style.colors["default"]
            )
            avatar_label.pack(side="left", padx=10, pady=10)
            
            # Se guarda la imagen
            self.record_images.append(avatar_img)

            # Etiqueta para los datos
            details_frame = tk.Frame(
                row,
                bg=style.colors["default"]
            )
            details_frame.pack(side="left", fill="x", expand=True, padx=10, pady=10)

            # Etiqueta del nombre del jugador
            name_label = self.create_title(
                details_frame,
                f"{index}. {record.get('name', '---')}",
                fg=style.colors["black"],
                bg=style.colors["default"]
            )
            name_label.pack(anchor="w")

            # Etiqueta para el puntaje
            score = record.get("score", 0)
            
            # Etiqueta para el equipo
            team = record.get("team", [])
            team_text = ", ".join(team) if team else "---"
            
            # Etiqueta con los datos
            self.create_text2(
                details_frame,
                f"{lang.score_column}: {score}\n{lang.team_column}: {team_text}",
                0,
                0,
                700,
                "left",
            ).pack(anchor="w")



    # Función para cargar los registros
    def load_records(self):
        # Se verifica si el archivo existe
        if not os.path.exists(self.top_path):
            self.save_records([])
            return []

        # Se carga el archivo
        try:
            # Se abre el archivo
            with open(self.top_path, "r", encoding="utf-8") as file:
                
                # Se lee el archivo
                data = json.load(file)
                
                # Se buscan los datos
                if isinstance(data, list):
                    normalized = [] # Se crea una lista vacia
                    
                    # Se recorren los datos
                    for item in data:
                        
                        # Se copian los datos
                        if isinstance(item, dict):
                            record = item.copy()
                            
                            # Se recorre la información
                            try:
                                record["score"] = int(record.get("score", 0))
                            except (TypeError, ValueError):
                                record["score"] = 0
                                
                            normalized.append(record) # Se guarda el puntaje
                            
                    # Se ordenan los datos por puntaje
                    return sorted(normalized, key=lambda item: item.get("score", 0), reverse=True)[:10]
                
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        
        # Se limpian los registros
        self.save_records([])
        return []



    # Función para guardar los registros
    def save_records(self, records):
        
        # Se busca el archivo
        os.makedirs(os.path.dirname(self.top_path), exist_ok=True)
        
        # Se abre el archivo
        with open(self.top_path, "w", encoding="utf-8") as file:
            
            # Se guardan los datos
            json.dump(records, file, indent=4, ensure_ascii=False)
