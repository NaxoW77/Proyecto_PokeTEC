# --- Archivo de idiomas ---
# Aquí se guardan todos los textos del juego para
# poder utilizarlos en cualquier parte del proyecto


# Se define la clase principal
# Por cada clase hay una subclase para cada pantalla
class Lang:
    
    # Textos principales
    def __init__(self):
        self.title = "PokéTEC" # Título principal del proyecto
        
        # Llamada a subclases
        self.titleScreen = Lang.TitleScreen(self)
        self.lobbyScreen = Lang.LobbyScreen(self)
        self.roundScreen = Lang.RoundScreen(self)
        self.gameScreen = Lang.GameScreen(self)
        self.resultsScreen = Lang.ResultsScreen(self)
        self.hallOfFameScreen = Lang.HallOfFameScreen(self)
        
        # Footer principal del proyecto
        self.copyright = "Copyright © 2026 Ignacio Apuy."
        
        # Mensaje en blanco
        self.default = "---"
    
    
    # Subclase para la pantalla de título
    class TitleScreen:
        def __init__(self, super):
            
            # Títulos
            self.title = "Bienvenido"
            self.description = self.concat(
                f"{super.title} es un proyecto basado en el videojuego Pokemon.",
                "\nEl objetivo de este proyecto es recrear el juego en Python utilizando Tkinter.",
            )
            
            # Subtítulos
            self.subtitle = "Instrucciones:"
            
            # Sección de instrucciones
            # Concat() se utiliza para unir los textos por línea
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
            
            # Sección de botones
            self.play_button = "Jugar"
            self.halloffame_button = "Salón de la fama"
            
            # Mensaje en blanco
            self.default = "---"
            
            
        
        # Función para concatenar texto por líneas
        def concat(self, *args):
            return "\n".join(args)
    
    
    # Subclase para la pantalla del lobby
    class LobbyScreen:
        def __init__(self, super):
            
            # Títulos
            self.title = "Bienvenido al Lobby"
            self.description = "Aquí puedes configurar tu nombre, avatar y seleccionar tu equipo inicial.\nEscribe tu nombre acá y dale a siguiente."
            
            # Sección del nombre
            self.name_label = "Nombre"
            self.next_button = "Siguiente"
            
            # Sección del avatar
            self.avatar_title = "Avatar"
            self.avatar_description = "Selecciona tu avatar."
            self.avatar_back = "◀" # Botones
            self.avatar_next = "▶" # Botones
            
            # Sección del equipo
            self.team_title = "Equipo"
            self.team_description = "Selecciona tu equipo."
            
            # Mensajes de error
            self.error_empty_name = "Debes escribir tu nombre."
            self.error_name_too_short = "El nombre debe tener al menos 3 caracteres."
            self.error_name_too_long = "El nombre debe tener menos de 15 caracteres."
            self.error_select_pokemon = "Debes seleccionar 3 pokemon."
            self.error_duplicate_pokemon = "Los pokemon deben ser distintos."
            
            # Mensaje en blanco
            self.default = "---"
    
    
    # Subclase para la pantalla de rondas
    class RoundScreen:
        def __init__(self, super):
            
            # Título
            self.title = "Ronda"
            self.description = "Elige con cuál Pokémon quieres pelear esta ronda."
            
            # Etiquetas
            self.player_label = "Jugador"
            self.score_label = "Puntaje"
            
            # Sección de selección
            self.select_pokemon = "Selecciona tu pokemon"
            self.continue_button = "Continuar"
            
            # Mensajes de error
            self.error_select = "Debes seleccionar un Pokémon."
            
            # Mensaje en blanco
            self.default = "---"
    
    
    # Subclase para la pantalla de combate
    class GameScreen:
        def __init__(self, super):
            
            # Título
            self.title = "Combate"
            
            # Acciones y botones
            self.actions_prompt = "Escoge un movimiento."
            self.actions_button = "Acciones"
            self.continue_button = "Continuar"
            
            # Etiquetas
            self.player_label = "Jugador"
            self.pokemon_label = "Pokémon"
            self.health_label = "Vida"
            
            # Mensajes por defecto
            self.default_action = "A luchar... \nEscoge una acción abajo."
            self.default_action_turn = "Tu turno...\nSelecciona una acción abajo."
            
            # --- Movimientos
            
            # Etiqueda de daño
            self.pkm_attack = ["hizo", "de daño."]
            
            # Resultados de daño
            self.pkm_action = "usó:"
            self.pkm_action_fail = "Pero"
            self.pkm_avoid = "esquivó el ataque."
            self.pkm_defend = "se defendió del ataque."
            
            # Nombres de estadísticas
            self.stat_dmg = "daño"
            self.stat_def = "defensa"
            
            # Etiqueta de estadísticas
            self.pkm_stat = ["aumentó su", "en"]
            self.pkm_stat_fail = ["Pero su", "no subió más."]
            
            
            # Etiquetas del jugador
            self.player_pref = "Tu"
            
            # Etiquetas del rival
            self.rival_pref = "El"
            self.rival_name = "rival"
            self.rival_thinking = "El rival esta pensando..."
            
        
            # El jugador gana
            self.player_win = ["Has derrotado al", "rival."]
            self.player_win_pkm = ["Ahora tienes a", "en tu equipo."]
            
            # El rival gana
            self.rival_win = "Has sido derrotado por tu rival."
            self.rival_win_pkm = ["Te han quitado a", "de tu equipo."]
            
            # Mensaje en blanco
            self.default = "---"
    
    
    # Subclase para la pantalla de resultados
    class ResultsScreen:
        def __init__(self, super):
            
            # Título
            self.title = "Resultados"
            
            # Etiquetas
            self.player_label = "Jugador"
            self.score_label = "Puntaje"
            self.team_label = "Equipo"
            
            # Mensaje de victoria
            self.victory = "¡VICTORIA!"
            self.victory_msg = "¡Felicidades! Tu resultado se guardará en el Salón de la Fama."
            
            # Mensaje de derrota
            self.defeat = "¡DERROTA!"
            self.defeat_msg = "Has perdido. Intenta de nuevo para entrar al Salón de la Fama."
            
            # Sección de botones            
            self.exit_button = "Salir"
            self.hall_of_fame_button = "Salón de la Fama"
            
            # Mensaje en blanco
            self.default = "---"
    
    
    # Subclase para la pantalla del salón de la fama
    class HallOfFameScreen:
        def __init__(self, super):
            
            # Títulos
            self.title = "Salón de la Fama"
            self.subtitle = "Top 10 jugadores"
            
            # Etiquetas de columnas
            self.player_column = "Jugador"
            self.team_column = "Equipo"
            self.score_column = "Puntaje"
            
            # Sección de botones
            self.back_button = "Volver"
            
            # Si no hay registros
            self.no_records = "No hay registros aún."
            
            # Mensaje en blanco
            self.default = "---"