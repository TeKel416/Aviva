
init python:
    # Posições "espalhadas" na mesa: (x, y, rotação, zoom)
    CARD_POSITIONS = [
        (0.25, 0.30, -18, 0.9),
        (0.45, 0.55,  12, 0.9),
        (0.65, 0.30,  -8, 0.9),
        (0.78, 0.60,  25, 0.9),
        (0.55, 0.78,  -5, 0.9),
        (0.32, 0.65,  20, 0.9),
        (0.72, 0.78, -15, 0.9),
        (0.20, 0.55, -25, 0.9),
    ]


transform card_reveal_anim:
    zoom 0.3 alpha 0.0
    linear 0.4 zoom 1.1 alpha 1.0
    linear 0.1 zoom 1.0


screen card_pick_screen():
    modal True
    add Solid("#3a2b1e")

    for px, py, rot, sc in CARD_POSITIONS:
        imagebutton:
            idle  Transform("card_back.png", rotate=rot, zoom=sc)
            hover Transform("card_back.png", rotate=rot, zoom=sc * 1.08, yoffset=-10)
            pos (px, py)
            anchor (0.5, 0.5)
            action Return(resolver_carta())

    frame:
        background "#000000a0"
        padding (20, 10)
        align (0.5, 0.05)
        text "Escolha uma carta do monte..." size 26 color "#fff"


screen card_reveal_screen(chave):
    modal True
    add Solid("#000")

    $ dados = CARD_DATABASE[chave]

    vbox:
        align (0.5, 0.45)
        spacing 30
        add Transform(dados["imagem"], zoom=1.2) at card_reveal_anim xalign 0.5
        vbox:
            xalign 0.5
            spacing 10
            text dados["nome"] size 40 color "#fff" xalign 0.5
            text dados["descricao"] size 22 color "#ccc" xalign 0.5 text_align 0.5

    textbutton "Continuar":
        align (0.5, 0.9)
        action Return()