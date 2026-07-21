# modelo/figura.py
from abc import ABC, abstractmethod


class Figura(ABC):
    """
    Interface de Estado (State) do padrão de projeto State.

    Cada subclasse concreta (em modelo/figuras/) representa o comportamento
    (estado) de uma figura sendo construída/desenhada. O Contexto
    (ModeloDesenho) delega a ela toda a lógica de reação aos eventos do
    mouse e de renderização, sem precisar saber qual é o tipo concreto da
    figura corrente.
    """

    # Flag polimórfica: indica se este estado se constrói por múltiplos
    # cliques + duplo-clique (como o Polígono) em vez de clique+arrasto+solta
    # (como as demais figuras). O Controlador usa isso, não isinstance().
    interacao_por_cliques = False

    def __init__(self, cor_borda, cor_preenchimento=None):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    # ---- Comportamento dependente do estado: interação ----
    def atualizar(self, x, y):
        """Atualiza a figura conforme o mouse se move (preview). Estado
        concreto sobrescreve quando suporta arraste/atualização contínua."""
        pass

    def adicionar_ponto(self, x, y):
        """Adiciona um novo ponto à figura. Usado por estados que se
        constroem por múltiplos cliques (Rabisco, PoligonoRegular)."""
        pass

    def finalizar(self, x, y):
        """Ação executada ao concluir a interação. Por padrão, apenas
        delega para atualizar(); estados que precisam de comportamento
        diferente (ex.: PoligonoRegular) sobrescrevem."""
        self.atualizar(x, y)

    # ---- Comportamento dependente do estado: renderização ----
    @abstractmethod
    def desenhar(self, canvas):
        pass

    @abstractmethod
    def desenhar_preview(self, canvas):
        pass

    @abstractmethod
    def is_completa(self):
        pass

    # ---- Comportamento dependente do estado: persistência (Salvar/Abrir) ----
    @abstractmethod
    def to_dict(self):
        """Serializa esta figura para um dicionário (usado por Salvar)."""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, dados):
        """Reconstrói uma figura deste tipo a partir de um dicionário (usado por Abrir)."""
        pass
