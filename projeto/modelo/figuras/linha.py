# modelo/figuras/linha.py
from modelo.figura import Figura


class Linha(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda):
        super().__init__(cor_borda)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def atualizar(self, x, y):
        self.x2, self.y2 = x, y

    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, width=2)

    def desenhar_preview(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="gray", dash=(4, 2), width=2)

    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)

    def to_dict(self):
        return {
            "tipo": "Linha",
            "x1": self.x1, "y1": self.y1, "x2": self.x2, "y2": self.y2,
            "cor_borda": self.cor_borda,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["x1"], dados["y1"], dados["x2"], dados["y2"], dados["cor_borda"])
