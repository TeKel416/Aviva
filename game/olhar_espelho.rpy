label cena_banheiro:
    scene bg_banheiro with fade

    "Você entra no banheiro e fecha a porta atrás de si."

    scene bg_espelho with dissolve

    "O espelho está na sua frente."

    menu:
        "O que fazer?"

        "Lavar o rosto":
            call banheiro_lavar_rosto
            return

        "Apenas observar seu reflexo":
            call banheiro_observar_reflexo
            return

        "Desviar o olhar e sair":
            $ marcar("evitou_espelho")
            "Você prefere não se encarar agora."
            scene bg_banheiro with dissolve
            "Sai do banheiro."
            return


# ───────────────────────────────────────────
label banheiro_lavar_rosto:
    "Você abre a torneira."

    play sound "water.ogg" fadein 0.5

    "Você lava o rosto."
    $ marcar("lavou_rosto")

    scene bg_espelho with dissolve

    "Você seca o rosto e sai."
    return

label banheiro_observar_reflexo:
    "Você encara o próprio reflexo por um instante."

    menu:
        "Sustentar o olhar ou desviar?"

        "Sustentar o olhar":
            $ marcar("sustentou_olhar")
            "Você continua olhando seu reflexo."

        "Desviar":
            $ marcar("desviou_olhar")
            "Você desvia o olhar."

    "Você sai do banheiro."
    return
