import tkinter as tk
from tkinter import ttk

# Importar estilos
from assets.styles import Style
style = Style()

class Player:
    def __init__(self, name="", avatar="", team=None):
        self.name = name if name else ""
        self.avatar = avatar if avatar else ""
        self.team = team if team is not None else []
        self.score = 0
        self.current_pokemon = None
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAvatar(self, avatar):
        self.avatar = avatar
    
    def getAvatar(self):
        return self.avatar
    
    def setTeam(self, team):
        self.team = team
    
    def getTeam(self):
        return self.team
    
    def setScore(self, score):
        self.score = score
        
    def getScore(self):
        return self.score
    
    def setCurrentPokemon(self, pokemon):
        self.current_pokemon = pokemon
    
    def getCurrentPokemon(self):
        return self.current_pokemon
    
    def addPokemon(self, pokemon):
        self.team.append(pokemon)
        
    def removePokemon(self, pokemon):
        for x in self.team:
            if x.name == pokemon.name:
                self.team.remove(x)
    
class Pokemon:
    def __init__(self, name="", hp=100, attack=50, defense=50, moveset=[], img=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moveset = moveset
        self.img = img
        
        self.current_hp = hp
        self.current_attack = attack
        self.current_defense = defense
        
    def takeDamage(self, type, damage):
        if type == "ATK":
            self.current_hp = self.current_hp - damage
        elif type == "DEF":
            self.current_attack = self.current_attack - damage
        elif type == "DMG":
            self.current_defense = self.current_defense - damage
    
class Ataque:
    def __init__(self, name="", type="", power=50, accuracy=100):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
    
    def takeDamage(self, damage):
        self.hp = max(0, self.hp - damage)
    
    def heal(self, amount):
        self.hp = min(self.current_hp, self.hp + amount)
    
    def isAlive(self):
        return self.hp > 0

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 1
        self.max_rounds = 3
    
    def isGameOver(self):
        return len(self.player1.team) == 0 or len(self.player2.team) == 0
    
    def nextRound(self):
        self.round += 1

class HallOfFame:
    def __init__(self, games=[]):
        self.games = games

class StyledFrame(tk.Frame):
    def __init__(self, parent, controller, bg_color):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        
    def create_title(self, parent, text, fg=style.colors["black"], bg=style.colors["default"]):
        return tk.Label(
            parent,
            text=text,
            fg=fg,
            bg=bg,
            font=style.A20,
            padx=0,
            pady=3,
            )
    
    def create_text1(self, parent, text, padx=0, pady=5, wraplength=800, fg=style.colors["black"], bg=style.colors["default"]):
        return tk.Label(
            parent,
            text=text,
            fg=fg,
            bg=bg,
            font=style.a16,
            padx=padx,
            pady=pady,
            wraplength=wraplength
            )

    def create_text2(self, parent, text, padx=0, pady=5, wraplength=800, justify="left", fg=style.colors["black"], bg=style.colors["default"]):
        return tk.Label(
            parent,
            text=text,
            fg=fg,
            bg=bg,
            justify=justify,
            font=style.a14,
            padx=padx,
            pady=pady,
            wraplength=wraplength
            )
    
    def create_button1(self, parent, text, command):
        return tk.Button(
            parent,
            text=text,
            bg=style.colors["main_blue"],
            fg=style.colors["default"], 
            font=style.a12,
            padx=20,
            pady=10, 
            relief="flat",
            cursor="hand2",
            command=command
            )