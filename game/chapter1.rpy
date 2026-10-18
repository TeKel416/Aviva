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
    scene bg_rua with fade

    # ─── Reação do cliente ───
    if last_round_correct >= WORK_GOOD_THRESHOLD:
        cliente "Hm… não ficou muito bom. Mas irei levar."
        a"Desculpa. Volte sempre."
    else:
        cliente "Não foi isso que eu pedi!"
        a "Perdão, irei consertar."

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