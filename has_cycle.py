def has_cycle(head):
    if (head == None): #Mostra que a lista esta vazia e retorna falso
        return False
    else:
        index = head #Pego o valor de cada elemento
        nextIndex = head.next #E do proximo elemento
        while (index != nextIndex) :
            if (nextIndex == None or nextIndex.next == None):
                return False #Aqui termina o laco se a cauda nao tiver apontamento e todos os elementos foram diferentes um do outro
            else: #E neste caso o laco continua mas sempre andando pra direita em pares e verificando se ha elementos iguais e nao houver termina o laco e retorno um verdadeiro
                index = index.next;
                nextIndex = nextIndex.next.next;
        return True
