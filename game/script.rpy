define aviva = Character("Aviva")

label start:
    scene bg quarto happy
    show aviva happy
    "Aviva..."

    $setupTimingGame()
    call screen caldeirao

    return


image aviva work:
    "aviva_anim/aviva work 01.png"
    pause 0.1
    "aviva_anim/aviva work 02.png"
    pause 0.1
    "aviva_anim/aviva work 03.png"
    pause 0.1
    "aviva_anim/aviva work 04.png"
    pause 0.1
    "aviva_anim/aviva work 05.png"
    pause 0.1
    "aviva_anim/aviva work 06.png"
    pause 0.1
    repeat

image aviva sad:
    "aviva_anim/aviva sad 01.png"
    pause 0.9
    "aviva_anim/aviva sad 02.png"
    pause 0.9
    repeat

image aviva neutral:
    "aviva_anim/aviva neutral 01.png"
    pause 0.7
    "aviva_anim/aviva neutral 02.png"
    pause 0.7
    repeat

image aviva happy:
    "aviva_anim/aviva happy 01.png"
    pause 0.5
    "aviva_anim/aviva happy 02.png"
    pause 0.5
    repeat

image ampulheta:
    "ampulheta_anim/ampulheta 1.png"
    pause 0.3
    "ampulheta_anim/ampulheta 2.png"
    pause 0.3
    "ampulheta_anim/ampulheta 3.png"
    pause 0.3
    "ampulheta_anim/ampulheta 4.png"
    pause 0.3
    repeat