# modelo/figuras/poligono_regular.py
from modelo.figura import Figura


class PoligonoRegular(Figura):
    interacao_por_cliques = True

    def __init__(self, pontos_iniciais, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.pontos = list(pontos_iniciais)  # [(x1, y1), (x2, y2), ...]
        self.ponto_atual = None              # posição do mouse para a linha elástica

    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))

    def atualizar(self, x, y):
        self.ponto_atual = (x, y)

    def desenhar(self, canvas):
        if len(self.pontos) >= 3:
            coords = [coord for ponto in self.pontos for coord in ponto]
            preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
            canvas.create_polygon(coords, outline=self.cor_borda, fill=preenchimento, width=2)
        elif len(self.pontos) == 2:
            canvas.create_line(self.pontos[0][0], self.pontos[0][1],
                                self.pontos[1][0], self.pontos[1][1], fill=self.cor_borda, width=2)

    def desenhar_preview(self, canvas):
        if self.pontos:
            coords = [coord for ponto in self.pontos for coord in ponto]
            if self.ponto_atual:
                coords.extend(self.ponto_atual)
            if len(coords) >= 4:
                canvas.create_line(coords, fill="gray", width=2, dash=(4, 4))

    def is_completa(self):
        return len(self.pontos) >= 2

    def to_dict(self):
        return {
            "tipo": "PoligonoRegular",
            "pontos": self.pontos,
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento,
        }

    @classmethod
    def from_dict(cls, dados):
        pontos = [tuple(ponto) for ponto in dados["pontos"]]
        return cls(pontos, dados["cor_borda"], dados.get("cor_preenchimento"))
