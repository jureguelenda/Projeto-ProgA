# modelo/modelo_desenho.py
class ModeloDesenho:
    """
    Contexto (Context) do padrão State.

    Não conhece o tipo concreto da figura em construção — apenas mantém
    uma referência a ela (self._figura_nova, o "estado atual") e delega
    todo o comportamento de interação a esse objeto.
    """

    def __init__(self):
        self._figuras = []
        self._figura_nova = None

    @property
    def figuras(self):
        return self._figuras

    @property
    def figura_nova(self):
        return self._figura_nova

    @figura_nova.setter
    def figura_nova(self, figura):
        self._figura_nova = figura

    def iniciar_figura(self, figura):
        """Define o estado corrente: a figura que passa a estar em construção."""
        self._figura_nova = figura

    def atualizar_figura_atual(self, x, y):
        """Delega a atualização/preview ao estado (figura) corrente."""
        if self._figura_nova is not None:
            self._figura_nova.atualizar(x, y)

    def adicionar_ponto_atual(self, x, y):
        """Delega a adição de ponto ao estado corrente (Rabisco/PoligonoRegular)."""
        if self._figura_nova is not None:
            self._figura_nova.adicionar_ponto(x, y)

    def finalizar_figura_atual(self, x, y):
        """Delega a finalização ao estado corrente e efetiva a transição:
        se a figura ficou completa, ela sai do estado 'em construção' e
        passa a integrar a lista de figuras concluídas."""
        if self._figura_nova is not None:
            self._figura_nova.finalizar(x, y)
            self.confirmar_figura()

    def confirmar_figura(self):
        """Move a figura corrente para a lista de concluídas (se válida) e
        retorna o contexto ao estado 'sem figura em construção'."""
        self.adicionar_figura(self._figura_nova)
        self._figura_nova = None

    def adicionar_figura(self, figura):
        if figura and figura.is_completa():
            self._figuras.append(figura)

    def limpar_temporaria(self):
        self._figura_nova = None

    def carregar_figuras(self, figuras):
        """Substitui todo o conteúdo do desenho pelas figuras fornecidas
        (usado por Abrir) e descarta qualquer figura em construção."""
        self._figuras = list(figuras)
        self._figura_nova = None
