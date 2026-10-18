# **** SCRIPT INFO ****
#
# This is a remake of the "chest unlock" timing minigame from the Youtube tutorial series, as that one has been broken since 
# Ren'Pys Sprite Manager got bugged around 8.5.0 version launch and haven't been fixed yet (as of 2026-09-01). This one includes 
# managing different chests in different scenes to remember which ones have been unlocked previously.
# Adjust and expand on it with your own code as fitting for your game.
# Also read the post for the code over at the Patreon post for the script to learn more about it.
#
# This script is a Patreon exclusive one only available to patrons in the tier "Supporter" or higher.
#
# URL to Patreon page: https://www.patreon.com/ess_renpy_tutorials
#
# The script comes with no warranty that it will work as the Ren'Py engine updates/changes.
#
# Please, do not redistribute this script for download anywhere. If you wish to share it with others, please link to the Patreon page as specified in this file where they can join to download it themselves.
#
# For questions, bugs or help with the script please contact me on Patreon.
#
# You may use and adapt this script for your game for personal or commercial purposes.
#
# Background art provided for free by mugenjohncel on the lemmasoft forums: https://lemmasoft.renai.us/forums/viewtopic.php?t=17302

init python:
    def get_spoon_image():
        #Retorna o caminho da imagem da colher com base no ciclo + estado global
        frame = store.SPOON_FRAMES[store.spoon_index % len(store.SPOON_FRAMES)]

        # Sucessos globais "ao vivo": total acumulado + acertos desta rodada
        sucessos_globais = store.total_correct + store.correct_timing_count

        if sucessos_globais >= store.spoon_colorless_threshold:
            suffix = "colorless"
        else:
            suffix = "color"

        return "caldeirao/colher_%s_%s.png" % (frame, suffix)

    def setupTimingGame():
        global safe_zone_pos, slider_pos
        global wrong_timing_count, correct_timing_count
        global timing_check, slider_movement_dir
        global timing_game_finished, run_timing_game
        global spoon_index

        max_pos = slider_bar_size[0] - safe_zone_size[0]
        safe_zone_pos = (int(max_pos/2), 0)
        
        # Set variables below to initial values. This is so we can use this function to reset
        # the game as well as setting it up for the first time.
        slider_pos = (0, 0)
        wrong_timing_count = 0
        correct_timing_count = 0
        timing_check        = False
        slider_movement_dir = "right"
        timing_game_finished = False
        run_timing_game     = False
        spoon_index          = 0

        # Hide the "game over" screen in case this function is called to reset the game.
        renpy.hide_screen("lost_timing_game")

    def startTimingGame():
        #Reset + inicia. Use isso no clique do baú / on 'show' do caldeirão.
        setupTimingGame()
        store.run_timing_game = True

    def moveSliderThumb(current_chest_game):
        # This function manages the logic of the timing game. It moves the slider from side to side and
        # checks if the player has pressed the button when the thumb is overlapping the safe zone, and then
        # does things accordingly.
        global slider_pos, timing_check, slider_movement_dir
        global wrong_timing_count, correct_timing_count
        global run_timing_game, timing_game_finished
        global spoon_index                                 
        
        # Padding for the zone detection logic so the thumb needs to be at least x amount of
        # pixels within the zone to be counted as a win.
        safe_zone_padding = 5

        if timing_check:
            # Player has pressed the space button to attempt at stopping the thumb in the green zone.
            # Here we check if they have managed to, and do things accordingly.
            timing_check = False
            # Calculate what the max x-position for the thumb can be to be counted as within the safe zone.
            # For that we need to know what the size of the safe zone is and its pixel x-coordinate.
            max_thumb_xpos = safe_zone_pos[0] + safe_zone_size[0] - slider_thumb_size[0]

            if max_thumb_xpos - safe_zone_padding > slider_pos[0] > safe_zone_pos[0] + safe_zone_padding:
                # SUCCESS! The thumb is within the green safe zone. We'll set the "run_timing_game" variable to False, play a "success" sound
                # and then append the scene name which had a chest unlocked to the list.
                #run_timing_game = False
                # ACERTO
                correct_timing_count += 1
                spoon_index = (spoon_index + 1) % len(store.SPOON_FRAMES)
                renpy.music.play(channel="sound", filenames="open-door.ogg", relative_volume=0.5)
            else:
                # ERRO
                wrong_timing_count += 1
                if not renpy.music.is_playing(channel="sound"):
                    renpy.music.play(channel="sound", filenames="error.ogg", relative_volume=0.5)
                #renpy.retain_after_load()
        
        # ─── Fim de rodada: 20 cliques totais ───
        if correct_timing_count + wrong_timing_count >= timing_clicks_limit:
            run_timing_game      = False
            timing_game_finished = True

            # camada 2 — sobrevive ao próximo setupTimingGame()
            store.last_round_correct = correct_timing_count
            store.last_round_wrong   = wrong_timing_count
            store.last_round_id      = current_chest_game

            # camada 3 — acumulado no save
            store.total_correct += correct_timing_count
            store.total_wrong   += wrong_timing_count

            hist = store.minigame_history.get(
                current_chest_game, {"correct": 0, "wrong": 0, "runs": 0}
            )
            hist["correct"] += correct_timing_count
            hist["wrong"]   += wrong_timing_count
            hist["runs"]    += 1
            store.minigame_history[current_chest_game] = hist

        #if wrong_timing_count == 3:
            # GAME OVER! The player has missed the safe zone 3 times which means they've now lost the game.
            # We'll set the "run_timing_game" variable to False which will make below if statement no longer
            # run its code and thus effectively stopping the thumb from moving.
            #run_timing_game = False
            #renpy.retain_after_load()
            #renpy.show_screen("lost_timing_game")

        if run_timing_game:
            # As long as "run_timing_game" is True we'll keep moving the thumb back and forth
            # according to the speed set in the "slider_speed" variable.
            if slider_movement_dir == "right" and slider_pos[0] < slider_bar_size[0] - slider_thumb_size[0]:
                xpos = slider_pos[0] + slider_speed
                slider_pos = (xpos, 0)
            elif slider_movement_dir == "right" and slider_pos[0] >= slider_bar_size[0] - slider_thumb_size[0]:
                slider_movement_dir = "left"
            elif slider_movement_dir == "left" and slider_pos[0] > 0:
                xpos = slider_pos[0] - slider_speed
                slider_pos = (xpos, 0)
            elif slider_movement_dir == "left" and slider_pos[0] <= 0:
                slider_movement_dir = "right"


transform chest_opened_anim:
    alpha 0.0
    parallel:
        easein 3.0 zoom 1.1
    parallel:
        easein 2.0 alpha 1.0

screen chest_game_1():
    key "K_SPACE" action SetVariable("timing_check", True)
    add "trabalho.png"

    if not "chest_game_1" in chests_opened:
        # This chest hasn't been opened yet because it's not in the "chests_opened" list, so we show the clickable closed chest.
        imagebutton auto "chest-closed-%s.png" action SetVariable("run_timing_game", True) pos(0.5, 0.35) anchor (0.5, 0.0)
    else:
        # This chest has been opened already so we show the unlocked chest.
        add "chest-opened.png":
            pos(0.5, 0.35)
            anchor(0.5, 0.0) 
            at chest_opened_anim

    showif run_timing_game:
        # Only show the slider bar if the game has been activated.
        frame:
            xfill True
            ysize 150
            yalign 0.0
            padding (0, 0)
            background Frame("timing_bg.png", 0, 0)
            add "timing_star.png":
                anchor (0, 0.5)
                pos (slider_pos[0], 75)

    # This button is only used as a simple showcase of how you can have several scenes with different chests to unlock,
    # and how each scene will show if its chest has been unlocked previously or not.
    showif not run_timing_game:
        button:
            align(0.9, 0.1)
            background "#fff"
            text "Scene 2" size 25 color "#000"
            action [Hide("chest_game_1"), Function(setupTimingGame), Show("chest_game_2")]
    
    
    use timing_minigame(current_scene = "chest_game_1")

    showif timing_game_finished:
        frame:
            align (0.5, 0.85)

            textbutton "Continuar":
                text_size 28
                text_color "#fff"
                action Return()

screen caldeirao():
    key "K_SPACE" action SetVariable("timing_check", True)
    add "trabalho.png"

    image "caldeirao/caldeirao_color.png":
        pos(0.5, 0.20) 
        anchor (0.5, 0.0)
    add get_spoon_image():
        pos (0.5, 0.20)
        anchor (0.5, 0.0)
    
    on "show" action SetVariable("run_timing_game", True)

    showif run_timing_game:
        frame:
            xfill True
            ysize 150
            yalign 0.0
            padding (0, 0)
            background Frame("timing_bg.png", 40, 0)
            add "timing_star.png":
                anchor (0, 0.5)
                pos (slider_pos[0], 75)
    use timing_minigame(current_scene = "caldeirao")

    showif timing_game_finished:
        frame:
            align (0.5, 0.85)
            textbutton "Continuar":
                text_size 28
                text_color "#fff"
                action Return()

screen timing_minigame(current_scene):
    if run_timing_game:
        frame:
            background "#fff"
            align (0.5, 0.2)
            padding(5, 5)
            text "Erros: %s" % (wrong_timing_count) color "#000" size 20 align (0.5, 0.5)
    
        timer 0.01 action Function(moveSliderThumb, current_scene) repeat True

define slider_bar_size = (1920, 35)
define slider_thumb_size = (24, 33)
define safe_zone_size = (325, 35)
define timing_clicks_limit = 20

default SPOON_FRAMES = ("esq", "frente", "dir", "baixo")
default safe_zone_pos = None
default slider_pos = (0, 0)
default slider_speed = 25
default timing_check = False
default slider_movement_dir = "right"
default wrong_timing_count   = 0
default correct_timing_count = 0
default run_timing_game      = False
default timing_game_finished = False
default chests_opened        = []
default spoon_colorless_threshold = 10
default spoon_index = 0