# modelo/figuras/circulo.py
import math
from modelo.figura import Figura


class Circulo(Figura):
    def __init__(self, cx, cy, raio, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.cx, self.cy, self.raio = cx, cy, raio

    def atualizar(self, x, y):
        # Recalcula o raio dinamicamente com base na distância até o centro
        self.raio = math.hypot(x - self.cx, y - self.cy)

    def desenhar(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio,
                            self.cx + self.raio, self.cy + self.raio,
                            outline=self.cor_borda, fill=preenchimento, width=2)

    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio,
                            self.cx + self.raio, self.cy + self.raio,
                            outline="black", fill=preenchimento, dash=(4, 2), width=2)

    def is_completa(self):
        return self.raio > 0

    def to_dict(self):
        return {
            "tipo": "Circulo",
            "cx": self.cx, "cy": self.cy, "raio": self.raio,
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["cx"], dados["cy"], dados["raio"],
                    dados["cor_borda"], dados.get("cor_preenchimento"))
