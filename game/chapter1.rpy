
# ═══════════════════════════════════════════
#  CAPÍTULO 1 — MANHÃ
# ═══════════════════════════════════════════
label c1_manha:
    scene bg quarto neutral with fade

    "Você acorda com o sol batendo na janela."

    a "Vamos começar o dia. Preciso me arrumar."
    call cena_banheiro
    return


# ═══════════════════════════════════════════
#  CAPÍTULO 1 — TARDE
# ═══════════════════════════════════════════
label c1_tarde:
    scene bg_rua with fade

    "A tarde chega e você decide o que fazer."

    label cena_cartas:
    scene black with fade
    "Sobre a mesa, um baralho está espalhado."

    call screen card_pick_screen
    $ chave = _return

    play sound "card_flip.ogg"
    call screen card_reveal_screen(chave)
    $ marcar("tirou_carta_" + chave)

    "Você guarda a carta."
    return



# ═══════════════════════════════════════════
#  CAPÍTULO 1 — NOITE
# ═══════════════════════════════════════════
label c1_noite:
    scene bg_quarto_noite with fade

    "A noite cai. Você reflete sobre o dia."


    return