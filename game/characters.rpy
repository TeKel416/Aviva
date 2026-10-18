# ═══════════════════════════════════════════════════════
#  PERSONAGENS — definições globais
# ═══════════════════════════════════════════════════════

# Protagonista Aviva
define a = Character(
    "Aviva",
    image="aviva",
    who_color="#a8c8ff",
)

# Pensamentos da Aviva (sem sprite, itálico)
define a_pensamento = Character(
    None,                     # sem nome exibido
    what_italic=True,
    what_color="#b8c8e8",
)

# Coadjuvantes
define constantine = Character("Constantine", who_color="#ffcc66")
define cliente    = Character("Cliente")
define nous       = Character("Nous", who_color="#a8e8a8")
define perpetus   = Character("Perpetus", who_color="#ddaaff")