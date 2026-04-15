class Lang:
    def __init__(self):
        self.title = "PokéTEC"
        self.titleScreen = Lang.TitleScreen(self)
        self.lobbyScreen = Lang.LobbyScreen(self)
        self.roundScreen = Lang.RoundScreen(self)
        self.gameScreen = Lang.GameScreen(self)
        self.resultsScreen = Lang.ResultsScreen(self)
        self.hallOfFameScreen = Lang.HallOfFameScreen(self)
        self.copyright = "Copyright © 2026 Ignacio Apuy."
    
    class TitleScreen:
        def __init__(self, super):
            self.title = "Bienvenido"
            self.description = self.concat(
                f"{super.title} es un proyecto basado en el videojuego Pokemon.",
                "\nEl objetivo de este proyecto es recrear el juego en Python utilizando Tkinter.",
            )
            
            self.subtitle = "Instrucciones:"
            self.instructions = self.concat(
                "1. Para jugar, presiona el botón de \"Jugar\" abajo.",
                "\n2. Una vez en el lobby, escribe tu nombre, selecciona tu avatar, y escoge a tu equipo.",
                "\n3. Dale a comenzar. Se te brindará información sobre la primer ronda, y deberás escoger con cuál Pokémon quieres pelear esta ronda.",
                "\n4. Comienza el juego. En cada ronda se te darán 4 acciones a elegir según tu Pokémon. Cada una tendrá diferentes efectos durante el combate. Después de tu turno, seguirá tu oponente.",
                "\n5. Cuando uno de los dos Pokémon en combate pierda, el jugador ganador se llevará al Pokémon rival, y se le otorgará un punto. Luego, continuarás con la siguiente ronda, donde debes elegir otro Pokémon de tu equipo restante.",
                "\n6. Ronda tras ronda, cuando uno de los dos jugadores se quede sin Pokémon para pelear, terminará el juego y ganará quien se quede con todos los Pokémon.",
                "\n7. El puntaje final se registrará en el salón de la fama, al cual puedes acceder desde este menú principal.",
                
                "\nPiensa bien tus movimientos en combate, planea tu estrategia y toma decisiones inteligentes para ganar.",
            )
            
        # Función para concatenar texto
        def concat(self, *args):
            return "\n".join(args)
    
    class LobbyScreen:
        def __init__(self, super):
            self.title = "Bienvenido al Lobby"
            self.description = "Aquí puedes configurar tu nombre, avatar y seleccionar tu equipo inicial.\nEscribe tu nombre acá y dale a siguiente."
            self.name_label = "Nombre:"
            self.next_button = "Siguiente"
            self.avatar_title = "Avatar"
            self.avatar_description = "Selecciona tu avatar."
            self.avatar_back = "◀"
            self.avatar_next = "▶"
            self.team_title = "Equipo"
            self.team_description = "Selecciona tu equipo."
            
            self.error_empty_name = "Debes escribir tu nombre."
            self.error_name_too_short = "El nombre debe tener al menos 3 caracteres."
            self.error_name_too_long = "El nombre debe tener menos de 15 caracteres."
            self.error_select_pokemon = "Debes seleccionar 3 pokemon."
            self.error_duplicate_pokemon = "Los pokemon deben ser distintos."
    
    class RoundScreen:
        def __init__(self, super):
            self.title = "Ronda 1"
            self.description = "Elige con cuál Pokémon quieres pelear esta ronda."
            self.select_pokemon = "Selecciona tu pokemon"
            self.continue_button = "Continuar"
            self.error_select = "Debes seleccionar un Pokémon."
            self.default = "---"
    
    class GameScreen:
        def __init__(self, super):
            self.title = "Combate"
            self.actions_prompt = "Escoge un movimiento."
            self.actions_button = "Acciones"
            self.player_label = "Jugador"
            self.pokemon_label = "Pokémon"
            self.health_label = "Vida"
            self.default = "---"
    
    class ResultsScreen:
        def __init__(self, super):
            self.title = "Resultados"
            self.victory = "¡VICTORIA!"
            self.defeat = "¡DERROTA!"
            self.exit_button = "Salir"
            self.hall_of_fame_button = "Salón de la Fama"
    
    class HallOfFameScreen:
        def __init__(self, super):
            self.title = "Salón de la Fama"
            self.player_column = "Jugador"
            self.team_column = "Equipo"
            self.score_column = "Puntaje"
            self.back_button = "Volver"
            self.no_records = "No hay registros aún."