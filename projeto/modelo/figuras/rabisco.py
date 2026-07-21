# modelo/figuras/rabisco.py
from modelo.figura import Figura


class Rabisco(Figura):
    def __init__(self, pontos, cor_borda):
        super().__init__(cor_borda)
        self.pontos = pontos[:]

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

    def atualizar(self, x, y):
        # Em um rabisco, "atualizar" equivale a acrescentar mais um ponto ao traço
        self.adicionar_ponto(x, y)

    def desenhar(self, canvas):
        if len(self.pontos) >= 2:
            coordenadas_planas = [coord for pt in self.pontos for coord in pt]
            canvas.create_line(coordenadas_planas, fill=self.cor_borda, width=2)

    def desenhar_preview(self, canvas):
        if len(self.pontos) >= 2:
            coordenadas_planas = [coord for pt in self.pontos for coord in pt]
            canvas.create_line(coordenadas_planas, fill="gray", dash=(4, 2), width=2)

    def is_completa(self):
        return len(self.pontos) > 1

    def to_dict(self):
        return {
            "tipo": "Rabisco",
            "pontos": self.pontos,
            "cor_borda": self.cor_borda,
        }

    @classmethod
    def from_dict(cls, dados):
        pontos = [tuple(ponto) for ponto in dados["pontos"]]
        return cls(pontos, dados["cor_borda"])
