
# --- Clases ---

# Estas son diferentes clases para instanciar objetos,
# para luego utilizarlos en el juego y globalizar
# sus funciones y propiedades

# Imports necesarios
import tkinter as tk
from tkinter import ttk
import random as random

# Se optó por utilizar deepcopy para instanciar objetos
# Referencia: https://docs.python.org/3/library/copy.html
from copy import deepcopy

# Importar textos
from assets.lang import Lang
lang = Lang()

# Importar estilos
from assets.styles import Style
style = Style()


# Se define el modelo de jugador
class Player:
    def __init__(self, name="", avatar="", team=None): # Parámetros de inicialización
        self.name = name if name else "" # Nombre del jugador
        self.avatar = avatar if avatar else "" # Imagen del jugador
        self.team = team if team is not None else [] # Equipo
        self.score = 0 # Puntaje
        self.current_pokemon = None # Pokemon seleccionado
        
        
    # --- Setters y getters
    
    # Nombre
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    # Avatar
    def setAvatar(self, avatar):
        self.avatar = avatar
    
    def getAvatar(self):
        return self.avatar
    
    # Equipo
    def setTeam(self, team):
        self.team = team
    
    def getTeam(self):
        return self.team
    
    # Puntaje
    def setScore(self, score):
        self.score = score
        
    def getScore(self):
        return self.score
    
    # Pokemon seleccionado
    def setCurrentPokemon(self, pokemon):
        self.current_pokemon = pokemon
    
    def getCurrentPokemon(self):
        return self.current_pokemon
    
    # Métodos para añadir o eliminar pokemones del equipo actual
    def addPokemon(self, pokemon):
        self.team.append(pokemon)
        
    def removePokemon(self, pokemon):
        for x in self.team:
            if x.name == pokemon.name:
                self.team.remove(x)
    
    
# Se define el modelo de pokemon
class Pokemon:
    def __init__(self, name="", hp=100, attack=50, defense=50, moveset=[], img=None): # Parámetros de inicialización
        self.name = name # Nombre del pokemon
        self.hp = hp # Vida
        self.attack = attack # Ataque base
        self.defense = defense # Defensa base
        self.moveset = moveset # Set de movimientos
        self.img = img # Imagen
        
        self.current_hp = hp # Vida actual
        self.current_attack = attack # Ataque actual
        self.current_defense = defense # Defensa actual
        
        
    # Método para calcular el daño recibido
    def takeDamage(self, atkPower, atkChance, pkmPower):
        
        # Calculamos la probabilidad de realizar el ataque
        if random.randint(1, 100) <= atkChance:
            
            # Fórmula del daño total
            total = (atkPower + pkmPower)-self.current_defense
            
            if total <= 0: # Si no hicimos daño
                total = 0
                return 0 # Devolvemos 0, o sea, el pokemón se defendió del ataque
            
            self.current_hp-=total # Restamos el daño
            
            if self.current_hp <= 0:
                self.current_hp = 0 # Evitamos valores negativos
                
            return total # Devolvemos el daño para mostrarlo luego
        else:
            return -1 # Devolvemos -1 para indicar si el ataque falló
    
    
    # Método para calcular la estadística aplicada
    def takeStat(self, type, val):
        statLimit = 30 # Límite de veces que se puede subir la estadística
        
        # Si la estadística es del tipo ataque
        if type == "DMG":
            
            # Aumentamos el ataque actual en base a lo que nos permita el movimiento
            self.current_attack = self.current_attack + val
            if self.current_attack > self.attack+statLimit: # Si superamos el límite
                self.current_attack = self.attack+statLimit
                return 0 # Devolvemos 0, o sea, no subimos la estadística
            
            return val # Devolvemos el aumento para mostrarlo luego
        
        # O si es del tipo defensa
        elif type == "DEF":
            
            # Aumentamos la defensa actual en base a lo que nos permita el movimiento
            self.current_defense = self.current_defense + val
            if self.current_defense > self.defense+statLimit: # Si superamos el límite
                self.current_defense = self.defense+statLimit
                return 0 # Devolvemos 0, o sea, no subimos la estadística
            
            return val # Devolvemos el aumento para mostrarlo luego


    # Función para instanciar objetos
    def clone(self):
        return Pokemon(
            self.name,
            self.hp,
            self.attack,
            self.defense,
            deepcopy(self.moveset), # Utilizamos deepcopy para evitar que el ataque nos afecte por error
            self.img
        )
    
    
# Se define el modelo de ataque
class Ataque:
    def __init__(self, name="", type="", power=50, accuracy=100, auto=False): # Parámetros de inicialización
        self.name = name # Nombre del movimiento
        self.type = type # Tipo del movimiento
        self.power = power # Poder del movimiento
        self.accuracy = accuracy # Precisión del movimiento


# Se define el modelo de pantalla
# Este es el modelo que guardará secciones para poder mostrarlas luego
class StyledFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller # Controlador para llamar variables globales
        
    # Método para crear títulos rápidamente
    def create_title(self, parent, text, fg=style.colors["black"], bg=style.colors["default"]): # Parámetros
        return tk.Label(
            parent, # Ubicación
            text=text, # Texto
            fg=fg, # Color
            bg=bg, # Fondo
            font=style.A20, # Fuente
            padx=0, # Distanciado en x
            pady=3, # Distanciado en y
            )
    
    
    # Método para crear textos grandes rápidamente
    def create_text1(self, parent, text, padx=0, pady=5, wraplength=800, fg=style.colors["black"], bg=style.colors["default"]): # Parámetros
        return tk.Label(
            parent, # Ubicación
            text=text, # Texto
            fg=fg, # Color
            bg=bg, # Fondo
            font=style.a16, # Fuente
            padx=padx, # Distanciado en x
            pady=pady, # Distanciado en y
            wraplength=wraplength # Ancho máximo
            )


    # Método para crear textos medianos rápidamente
    def create_text2(self, parent, text, padx=0, pady=5, wraplength=800, justify="left", fg=style.colors["black"], bg=style.colors["default"]): # Parámetros
        return tk.Label(
            parent, # Ubicación
            text=text, # Texto
            fg=fg, # Color 
            bg=bg, # Fondo
            justify=justify, # Posición del texto
            font=style.a14, # Fuente
            padx=padx, # Distanciado en x
            pady=pady, # Distanciado en y
            wraplength=wraplength # Ancho máximo
            )
    
    # Método para crear botones
    def create_button1(self, parent, text, command):
        return tk.Button(
            parent, # Ubicación
            text=text, # Texto
            bg=style.colors["main_blue"], # Fondo
            fg=style.colors["default"],  # Color
            font=style.a12, # Fuente
            padx=20, # Distanciado en x
            pady=10, # Distanciado en y
            relief="flat", # Diseño
            cursor="hand2", # Cursor
            command=command # Función
            )
        
        
    # Método para ocultar un elemento
    def hide(self, elem):
        elem.pack_forget()
    
    
    # Método para mostrar un elemento
    def show(self, elem):
        elem.pack(fill="both", expand=True)