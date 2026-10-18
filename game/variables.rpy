# marca o capítulo atual e o período do dia
default capitulo_atual = 1
default periodo_atual = "manhã"

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