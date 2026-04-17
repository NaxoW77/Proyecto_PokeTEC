from assets.classes import Pokemon
from assets.classes import Ataque

class PokemonList:
    def __init__(self):
        self.pokemon1 = Pokemon(
            "Snorlax", # Nombre
            120, # Vida
            30, # Ataque
            85, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Placaje", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Golpe Cuerpo", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Defensa Férrea (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Tambor (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm1.png" # Imagen
            )
        
        self.pokemon2 = Pokemon(
            "Squirtle", # Nombre
            110, # Vida
            35, # Ataque
            75, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Burbuja", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Hidrobomba", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Refugio (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Foco Energía (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm2.png" # Imagen
            )
        
        self.pokemon3 = Pokemon(
            "Bulbasaur", # Nombre
            105, # Vida
            40, # Ataque
            70, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Látigo Cepa", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Rayo Solar", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Síntesis (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Crecimiento (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm3.png" # Imagen
        )
        
        self.pokemon4 = Pokemon(
            "Mew", # Nombre
            100, # Vida
            45, # Ataque
            60, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Destructor", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Psíquico", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Barrera (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Maquinación (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm4.png" # Imagen
        )
        
        self.pokemon5 = Pokemon(
            "Eevee", # Nombre
            95, # Vida
            50, # Ataque
            50, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ataque Rápido", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Derribo", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Encanto (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Refuerzo (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm5.png" # Imagen
        )
        
        self.pokemon6 = Pokemon(
            "Dragonite", # Nombre
            100, # Vida
            60, # Ataque
            45, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ciclón", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Enfado", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Velo Sagrado (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Danza Dragón (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm6.png" # Imagen
        )
        
        self.pokemon7 = Pokemon(
            "Pikachu", # Nombre
            90, # Vida
            65, # Ataque
            40, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Impactrueno", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Trueno", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Pantalla Luz (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Carga (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm7.png" # Imagen
        )
        
        self.pokemon8 = Pokemon(
            "Charizard", # Nombre
            95, # Vida
            75, # Ataque
            35, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Ascuas", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Llamarada", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Pantalla Humo (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Danza Espada (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm8.png" # Imagen
        )
        
        self.pokemon9 = Pokemon(
            "Gengar", # Nombre
            85, # Vida
            85, # Ataque
            25, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Lengüetazo", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Come Sueños", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Mismo Destino (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Maldición (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
                    100, # Precisión
                    )
            ],
            "assets/img/pkm9.png" # Imagen
        )
        
        self.pokemon10 = Pokemon(
            "Mewtwo", # Nombre
            90, # Vida
            95, # Ataque
            20, # Defensa
            [ # Moveset
                Ataque( # Ataque 1
                    "Confusión", # Nombre
                    "ATK", # Tipo
                    20, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Onda Mental", # Nombre
                    "ATK", # Tipo
                    50, #Potencia
                    50, # Precisión
                    ),
                
                Ataque(
                    "Amnesia (+DEF)", # Nombre
                    "DEF", # Tipo
                    10, # Potencia
                    100, # Precisión
                    ),
                
                Ataque(
                    "Paz Mental (+ATK)", # Nombre
                    "DMG", # Tipo
                    10, # Potencia
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
                return pokemon.clone()
        
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