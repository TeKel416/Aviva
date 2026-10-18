label start:
    scene bg black

    stop music

    voice "aviva-sussuros.mp3"
    "Aviva...{p=5.5}{nw}"
    
    play music "aviva-neutro.mp3" fadein 1.0
    call c1_manha
    
    a "Preciso seguir o que Perpetus diz. Preciso trabalhar para alcançar meu sonho."
    scene trabalho with fade

    $setupTimingGame()
    call screen caldeirao

    $ print(">>> [START] Acabou a caldeirao. last_round_correct:", last_round_correct)
    
    call c1_tarde

    $ print(">>> [START] Acabou o c1_tarde.")

    call c1_noite

    $ print(">>> [START] Acabou o c1_noite.")

    call cena_cartas

    $ print(">>> [START] Acabou o c1.")

    return

# --- Animações de Aviva ---
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