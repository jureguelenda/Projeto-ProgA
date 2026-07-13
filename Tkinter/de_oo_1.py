import math
from figuras_base import Figura  # Importa a classe abstrata criada pelo Integrante A

class Retangulo(Figura):
    """Representa um retângulo."""
    
    def _init_(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        super()._init_(cor_borda, cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def desenhar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                               outline=self.cor_borda, fill=self.cor_preenchimento)
    
    def desenhar_preview(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                               outline="black", fill=self.cor_preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)


class Oval(Figura):
    """Representa um oval/elipse."""
    
    def _init_(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        super()._init_(cor_borda, cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def desenhar(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                          outline=self.cor_borda, fill=self.cor_preenchimento)
    
    def desenhar_preview(self, canvas):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                          outline="black", fill=self.cor_preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)


class Circulo(Figura):
    """Representa um círculo."""
    
    def _init_(self, cx, cy, raio, cor_borda, cor_preenchimento=None):
        super()._init_(cor_borda, cor_preenchimento)
        self.cx = cx
        self.cy = cy
        self.raio = raio
    
    def desenhar(self, canvas):
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio, 
                          self.cx + self.raio, self.cy + self.raio,
                          outline=self.cor_borda, fill=self.cor_preenchimento)
    
    def desenhar_preview(self, canvas):
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio, 
                          self.cx + self.raio, self.cy + self.raio,
                          outline="black", fill=self.cor_preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return self.raio > 0


class PoligonoRegular(Figura):
    """Representa um polígono regular."""
    
    def _init_(self, cx, cy, raio, num_lados, cor_borda, cor_preenchimento=None):
        super()._init_(cor_borda, cor_preenchimento)
        self.cx = cx
        self.cy = cy
        self.raio = raio
        self.num_lados = num_lados
        self.pontos = self._calcular_pontos()
    
    def _calcular_pontos(self):
        pontos = []
        lados = max(3, self.num_lados)
        angulo = 2 * math.pi / lados
        for i in range(lados):
            x = self.cx + self.raio * math.cos(i * angulo)
            y = self.cy + self.raio * math.sin(i * angulo)
            pontos.extend([x, y])
        return pontos
    
    def desenhar(self, canvas):
        canvas.create_polygon(self.pontos, outline=self.cor_borda, 
                             fill=self.cor_preenchimento if self.cor_preenchimento else "", width=2)
    
    def desenhar_preview(self, canvas):
        canvas.create_polygon(self.pontos, outline="black", 
                             fill=self.cor_preenchimento if self.cor_preenchimento else "", dash=(4, 2), width=2)
    
    def is_completa(self):
        return self.raio > 0 and self.num_lados >= 3