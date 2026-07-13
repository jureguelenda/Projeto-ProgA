from abc import ABC, abstractmethod

class Figura(ABC):
    """Classe base abstrata para todas as figuras."""
    def __init__(self, cor_borda, cor_preenchimento=None):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    @abstractmethod
    def desenhar(self, canvas):
        """Desenha a figura definitiva no canvas."""
        pass

    @abstractmethod
    def desenhar_preview(self, canvas):
        """Desenha a versão de preview (tracejado) no canvas."""
        pass

    @abstractmethod
    def is_completa(self):
        """Verifica se a figura está completa."""
        pass

class Linha(Figura):
    """Representa uma linha comum."""
    def __init__(self, x1, y1, x2, y2, cor_borda):
        super().__init__(cor_borda)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def desenhar(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda)

    def desenhar_preview(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="gray", dash=(4, 2))

    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)

class Rabisco(Figura):
    """Representa um desenho à mão livre (rabisco)."""
    def __init__(self, pontos, cor_borda):
        super().__init__(cor_borda)
        self.pontos = pontos[:] # Cópia segura da lista de pontos

    def desenhar(self, canvas):
        if len(self.pontos) >= 2:
            coordenadas_planas = [coord for pt in self.pontos for coord in pt]
            canvas.create_line(coordenadas_planas, fill=self.cor_borda)

    def desenhar_preview(self, canvas):
        if len(self.pontos) >= 2:
            coordinates_planas = [coord for pt in self.pontos for coord in pt]
            canvas.create_line(coordinates_planas, fill="gray", dash=(4, 2))

    def is_completa(self):
        return len(self.pontos) > 1
