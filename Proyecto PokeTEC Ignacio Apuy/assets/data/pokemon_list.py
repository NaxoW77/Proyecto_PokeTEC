from assets.classes import Pokemon
from assets.classes import Ataque

class PokemonList:
    def __init__(self):
        self.pokemon1 = Pokemon(
            "Pikachu", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Rayo", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Trueno", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Estática", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Carga", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm1.png" # Imagen
            )
        
        self.pokemon2 = Pokemon(
            "Pokemon2", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm2.png" # Imagen
            )
        
        self.pokemon3 = Pokemon(
            "Pokemon3", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm3.png" # Imagen
        )
        
        self.pokemon4 = Pokemon(
            "Pokemon4", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm4.png" # Imagen
        )
        
        self.pokemon5 = Pokemon(
            "Pokemon5", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm5.png" # Imagen
        )
        
        self.pokemon6 = Pokemon(
            "Pokemon6", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm6.png" # Imagen
        )
        
        self.pokemon7 = Pokemon(
            "Pokemon7", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm7.png" # Imagen
        )
        
        self.pokemon8 = Pokemon(
            "Pokemon8", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm8.png" # Imagen
        )
        
        self.pokemon9 = Pokemon(
            "Pokemon9", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm9.png" # Imagen
        )
        
        self.pokemon10 = Pokemon(
            "Pokemon10", # Nombre
            100, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque1", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Ataque2", # Nombre
                    "ATK", # Tipo
                    30, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa1", # Nombre
                    "DEF", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Daño1", # Nombre
                    "DMG", # Tipo
                    20, # Potencia
                    100, # Precisión
                )
            ],
            "assets/img/pkm10.png" # Imagen
        )
        
        self.list = [
            self.pokemon1,
            self.pokemon2,
            self.pokemon3,
            self.pokemon4,
            self.pokemon5,
            self.pokemon6,
            self.pokemon7,
            self.pokemon8,
            self.pokemon9,
            self.pokemon10
            ]
        
    def getPokemon(self, name):
        for pokemon in self.list:
            if pokemon.name == name:
                return pokemon
        
    def getNames(self):
        return [
            self.pokemon1.name,
            self.pokemon2.name,
            self.pokemon3.name,
            self.pokemon4.name,
            self.pokemon5.name,
            self.pokemon6.name,
            self.pokemon7.name,
            self.pokemon8.name,
            self.pokemon9.name,
            self.pokemon10.name
            ]