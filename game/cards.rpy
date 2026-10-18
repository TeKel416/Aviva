init python:
    CARD_DATABASE = {
        "Enforcado": {
            "imagem": "card_enforcado.png",
            "nome": "O Enforcado",
            "descricao": "Ele está de cabeça para baixo por escolha. Porque sabe que ver o mundo de baixo para cima revela o que o olhar convencional esconde.",
        },
        "Torre": {
            "imagem": "card_torre.png",
            "nome": "A Torre",
            "descricao": "As estruturas que A Torre derruba geralmente já estavam rachadas há muito tempo — construídas sobre ilusões, medo ou conformidade",
        },
        "Mago": {
            "imagem": "card_mago.png",
            "nome": "O Mago",
            "descricao": "O Mago é aquele que conhece os segredos do universo e possui a capacidade de transformar pensamento em ação.",
        },
        "Mundo": {
            "imagem": "card_mundo.png",
            "nome": "O Mundo",
            "descricao": "É a carta da completude, da integração total, do ciclo finalizado e da jornada humana chegando à sua plenitude.",
        },
    }

    def resolver_carta():
        #Decide a carta com base nas escolhas anteriores
        flags = getattr(store, 'flags', set())

        # ── Prioridade: condições mais específicas primeiro ──
        if "sustentou_olhar" in flags:
            return "Enforcado"

        if "evitou_espelho" in flags:
            return "Torre"

        if "lavou_rosto" in flags:
            return "Mundo"

        return "Mago"
