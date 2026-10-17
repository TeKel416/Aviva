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
    def setupTimingGame():
        global safe_zone_pos
        global slider_pos
        global wrong_timing_count

        max_pos = slider_bar_size[0] - safe_zone_size[0]
        safe_zone_pos = (int(max_pos/2), 0)
        
        # Set variables below to initial values. This is so we can use this function to reset
        # the game as well as setting it up for the first time.
        slider_pos = (0, 0)
        wrong_timing_count = 0

        # Hide the "game over" screen in case this function is called to reset the game.
        renpy.hide_screen("lost_timing_game")

    def moveSliderThumb(current_chest_game):
        # This function manages the logic of the timing game. It moves the slider from side to side and
        # checks if the player has pressed the button when the thumb is overlapping the safe zone, and then
        # does things accordingly.
        global slider_pos
        global timing_check
        global slider_movement_dir
        global wrong_timing_count
        global run_timing_game
        
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
                renpy.music.play(channel = "sound", filenames = "open-door.ogg", relative_volume = 0.5)
                #chests_opened.append(current_chest_game)
                #renpy.retain_after_load()
            else:
                # ERROR! The thumb is not within the safe zone. We add 1 to the "wrong_timing_count" variable to keep track
                # of how many times they've missed it and play an error sound.
                wrong_timing_count += 1
                # Play an error sound.
                if not renpy.music.is_playing(channel = "sound"):
                    renpy.music.play(channel = "sound", filenames = "error.ogg", relative_volume = 0.5)
            
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

screen lost_timing_game():
    modal True

    frame:
        background "#ffffffb6"
        align(0.5, 0.5)
        xfill True
        ysize 80
        text "You lost :(" size 40 color "#000" align (0.5, 0.5)
    
    dismiss action Function(setupTimingGame)

screen chest_game_1():
    key "K_SPACE" action SetVariable("timing_check", True)
    add "background.png"

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
            align(slider_bar_align_x, slider_bar_align_y)
            padding(0, 0)
            background "slider-bar.png"
            xysize slider_bar_size
            add "safe-zone.png" pos safe_zone_pos
            add "slider.png" pos slider_pos

    # This button is only used as a simple showcase of how you can have several scenes with different chests to unlock,
    # and how each scene will show if its chest has been unlocked previously or not.
    showif not run_timing_game:
        button:
            align(0.9, 0.1)
            background "#fff"
            text "Scene 2" size 25 color "#000"
            action [Hide("chest_game_1"), Function(setupTimingGame), Show("chest_game_2")]
    
    use timing_minigame(current_scene = "chest_game_1")

screen chest_game_2():
    key "K_SPACE" action SetVariable("timing_check", True)
    add "background-2.png"

    if "chest_game_2" not in chests_opened:
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
            align(slider_bar_align_x, slider_bar_align_y)
            padding(0, 0)
            background "slider-bar.png"
            xysize slider_bar_size
            add "safe-zone.png" pos safe_zone_pos
            add "slider.png" pos slider_pos
    
    # This button is only used as a simple showcase of how you can have several scenes with different chests to unlock,
    # and how each scene will show if its chest has been unlocked previously or not.
    showif not run_timing_game:
        button:
            align(0.9, 0.1)
            background "#fff"
            text "Scene 1" size 25 color "#000"
            action [Hide("chest_game_2"), Function(setupTimingGame), Show("chest_game_1")]
    
    use timing_minigame(current_scene = "chest_game_2")

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
define safe_zone_size = (150, 35)

default safe_zone_pos = None
default slider_pos = (0, 0)
default slider_bar_align_x = 0.5
default slider_bar_align_y = 1
default slider_speed = 25
default timing_check = False
default slider_movement_dir = "right"
default wrong_timing_count = 0
default chests_opened = []
default run_timing_game = False