# modelo/figuras/retangulo.py
from modelo.figura import Figura


class Retangulo(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def atualizar(self, x, y):
        self.x2, self.y2 = x, y

    def desenhar(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                 outline=self.cor_borda, fill=preenchimento, width=2)

    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                 outline="black", fill=preenchimento, dash=(4, 2), width=2)

    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)

    def to_dict(self):
        return {
            "tipo": "Retangulo",
            "x1": self.x1, "y1": self.y1, "x2": self.x2, "y2": self.y2,
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["x1"], dados["y1"], dados["x2"], dados["y2"],
                    dados["cor_borda"], dados.get("cor_preenchimento"))
