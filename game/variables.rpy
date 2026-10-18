# marca o capítulo atual e o período do dia
default capitulo_atual = 1
default periodo_atual = "manhã"

# ── Estado do timing game 

# Última rodada — o label lê isso após o call screen
default last_round_correct = 0
default last_round_wrong   = 0
default last_round_id      = None

# Totais acumulados na partida
default total_correct    = 0
default total_wrong      = 0
default minigame_history = {}

#marca eventos
init python:
    def marcar(evento):
        if not hasattr(store, 'flags'):
            store.flags = set()
        store.flags.add(evento)

    def aconteceu(evento):
        if not hasattr(store, 'flags'):
            return False
        return evento in store.flags