label cena_banheiro:
    scene bg espelho with fade

    "Você entra no banheiro e fecha a porta atrás de si."

    scene bg espelho with dissolve

    "O espelho está na sua frente."

    menu:
        "O que fazer?"

        "Observar seu reflexo":
            call banheiro_observar_reflexo
            return

        "Desviar o olhar e sair":
            $ marcar("evitou_espelho")
            "Você prefere não se encarar agora."
            hide aviva with fade
            "Você sai do banheiro."
            return


# ───────────────────────────────────────────
label banheiro_observar_reflexo:
    show aviva espelho neutral with fade:
        yalign 0.3
        xalign 0.5
        zoom 0.7
    "Você encara o próprio reflexo por um instante."

    menu:
        "Sustentar o olhar ou desviar?"

        "Sustentar o olhar":
            show aviva espelho neutral olheiras with dissolve:
                yalign 0.3
                xalign 0.5
                zoom 0.7
            $ marcar("sustentou_olhar")
            "Você continua olhando seu reflexo."

        "Desviar":
            hide aviva with fade
            $ marcar("desviou_olhar")
            "Você desvia o olhar."

    hide aviva with fade
    "Você sai do banheiro."
    return
