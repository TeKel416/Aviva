define WORK_GOOD_THRESHOLD  = 10

# ═══════════════════════════════════════════
#  CAPÍTULO 1 — MANHÃ
# ═══════════════════════════════════════════
label c1_manha:
    scene bg quarto neutral with fade

    a_pensamento  "Vamos começar o dia. Preciso me arrumar."
    call cena_banheiro

    return


# ═══════════════════════════════════════════
#  CAPÍTULO 1 — TARDE
# ═══════════════════════════════════════════
label c1_tarde:
    $ print(">>> [C1_TARDE] Entrou no label c1_tarde.")
    # ─── Reação do cliente ───
    if last_round_correct >= WORK_GOOD_THRESHOLD:
        $ print(">>> [C1_TARDE] Cliente: Bom.")
        cliente "Hm… não ficou muito bom. Mas irei levar."
        a"Desculpa. Volte sempre."
    else:
        $ print(">>> [C1_TARDE] Cliente: Ruim.")
        cliente "Não foi isso que eu pedi!"
        a "Perdão, irei consertar."

    show constantine neutral
    "Constantine se aproxima."

    if last_round_correct >= WORK_GOOD_THRESHOLD:
        constantine "Está indo bem! Se continuar com esse ritmo, conseguirá ser o funcionário do mês como eu!"
        a "Agradeço o elogio."
        $ marcar("constantine_elogiou")
    else:
        constantine "Ouvi que não conseguiu bater sua meta... Você tem talento. Se focar no serviço como eu, acredito que consegue recuperar!"
        a "Agradeço o elogio. Irei focar."
        $ marcar("constantine_aconselhou")

    return


# ═══════════════════════════════════════════
#  CAPÍTULO 1 — NOITE
# ═══════════════════════════════════════════
label c1_noite:
    scene bg_quarto_noite with fade
    show nous neutral

    a "Nous, meu querido gato! Obrigada pela companhia."
    return

label cena_cartas:
    scene black with fade
    a "Eu gosto de tarô. Vou conferir a tiragem!"

    call screen card_pick_screen
    $ chave = _return

    play sound "card_flip.ogg"
    call screen card_reveal_screen(chave)
    $ marcar("tirou_carta_" + chave)

    "Você guarda a carta."

    return