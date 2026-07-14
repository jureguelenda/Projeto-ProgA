from abc import ABC, abstractmethod
import math
from tkinter import *
from tkinter import ttk

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
            coordenadas_planas = [coord for pt in self.pontos for coord in pt]
            canvas.create_line(coordenadas_planas, fill="gray", dash=(4, 2))

    def is_completa(self):
        return len(self.pontos) > 1


class Retangulo(Figura):
    """Representa um retângulo."""
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def desenhar(self, canvas):
        # Se cor_preenchimento for None, usamos string vazia "" para o Tkinter entender que é transparente
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                               outline=self.cor_borda, fill=preenchimento)
    
    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                               outline="black", fill=preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)


class Oval(Figura):
    """Representa um oval/elipse."""
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def desenhar(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                          outline=self.cor_borda, fill=preenchimento)
    
    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                          outline="black", fill=preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return not (self.x1 == self.x2 and self.y1 == self.y2)


class Circulo(Figura):
    """Representa um círculo."""
    def __init__(self, cx, cy, raio, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
        self.cx = cx
        self.cy = cy
        self.raio = raio

    def desenhar(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio, 
                          self.cx + self.raio, self.cy + self.raio,
                          outline=self.cor_borda, fill=preenchimento)
    
    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_oval(self.cx - self.raio, self.cy - self.raio, 
                          self.cx + self.raio, self.cy + self.raio,
                          outline="black", fill=preenchimento, dash=(4, 2))
    
    def is_completa(self):
        return self.raio > 0


class PoligonoRegular(Figura):
    """Representa um polígono regular."""
    def __init__(self, cx, cy, raio, num_lados, cor_borda, cor_preenchimento=None):
        super().__init__(cor_borda, cor_preenchimento)
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
            # Rotaciona um pouco (- pi/2) para que o polígono comece apontando para cima
            x = self.cx + self.raio * math.cos(i * angulo - math.pi / 2)
            y = self.cy + self.raio * math.sin(i * angulo - math.pi / 2)
            pontos.extend([x, y])
        return pontos
    
    def desenhar(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_polygon(self.pontos, outline=self.cor_borda, 
                             fill=preenchimento, width=2)
    
    def desenhar_preview(self, canvas):
        preenchimento = self.cor_preenchimento if self.cor_preenchimento else ""
        canvas.create_polygon(self.pontos, outline="black", 
                             fill=preenchimento, dash=(4, 2), width=2)
    
    def is_completa(self):
        return self.raio > 0 and self.num_lados >= 3


# Tradução de nomes de cores em português para Hexadecimal
CORES_MAP = {
    "Preto": "#000000",
    "Branco": "#FFFFFF",
    "Cinza": "#7F7F7F",
    "Vermelho": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarelo": "#FFFF00",
    "Rosa": "#FF00FF",
    "Ciano": "#00FFFF",
    "Laranja": "#FFA500"
}

figuras = []        
figura_nova = None 

def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    c_borda = CORES_MAP[cor_borda_var.get()]
    c_preenchimento = CORES_MAP[cor_preench_var.get()] if vai_preencher.get() else None

    x, y = event.x, event.y
    
    if tipo == 'Linha':
        figura_nova = Linha(x, y, x, y, c_borda)
    elif tipo == 'Retângulo':
        figura_nova = Retangulo(x, y, x, y, c_borda, c_preenchimento)
    elif tipo == 'Oval':
        figura_nova = Oval(x, y, x, y, c_borda, c_preenchimento)
    elif tipo == 'Círculo':
        figura_nova = Circulo(x, y, 0, c_borda, c_preenchimento)
    elif tipo == 'Rabisco':
        figura_nova = Rabisco([(x, y)], c_borda)
    elif tipo == 'Polígono Regular':
        figura_nova = PoligonoRegular(x, y, 0, 5, c_borda, c_preenchimento)  # 5 lados por padrão
    else:
        figura_nova = None


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
        
    x, y = event.x, event.y
    
    if isinstance(figura_nova, Rabisco):
        figura_nova.pontos.append((x, y))
    elif isinstance(figura_nova, Linha):
        figura_nova.x2 = x
        figura_nova.y2 = y
    elif isinstance(figura_nova, Retangulo):
        figura_nova.x2 = x
        figura_nova.y2 = y
    elif isinstance(figura_nova, Oval):
        figura_nova.x2 = x
        figura_nova.y2 = y
    elif isinstance(figura_nova, Circulo):
        cx, cy = figura_nova.cx, figura_nova.cy
        figura_nova.raio = ((cx - x)**2 + (cy - y)**2)**0.5
    elif isinstance(figura_nova, PoligonoRegular):
        cx, cy = figura_nova.cx, figura_nova.cy
        figura_nova.raio = ((cx - x)**2 + (cy - y)**2)**0.5
        figura_nova.pontos = figura_nova._calcular_pontos()
    
    desenhar_figuras()
    desenhar_figura_nova()


def incluir_figura_nova(event): 
    global figura_nova
    if figura_nova and figura_nova.is_completa(): 
        figuras.append(figura_nova) 
    desenhar_figuras()
    figura_nova = None


def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar(canvas)


def desenhar_figura_nova():
    if figura_nova is None:
        return
    figura_nova.desenhar_preview(canvas)


# ====================== INTERFACE ======================
nomes_cores = list(CORES_MAP.keys())

root = Tk()
root.title("Desenho OO - Projeto Prog A")

frame = Frame(root)
paddings = {'padx': 5, 'pady': 5} 

# Tipo de figura
ttk.Label(frame, text='Tipo de Figura:').grid(column=0, row=0, sticky=W, **paddings)
tipo_figura_var = StringVar(root)
# Configura 'Linha' como o valor inicial padrão na própria variável
tipo_figura_var.set('Linha')
ttk.OptionMenu(frame, tipo_figura_var, 'Linha', 
              'Linha', 'Rabisco', 'Círculo', 'Retângulo', 'Oval', 'Polígono Regular').grid(
              column=1, row=0, sticky=W, **paddings)

# Cor da borda
ttk.Label(frame, text='Cor da Borda:').grid(column=2, row=0, sticky=W, **paddings)
cor_borda_var = StringVar(root)
cor_borda_var.set('Preto')
ttk.OptionMenu(frame, cor_borda_var, 'Preto', *nomes_cores).grid(column=3, row=0, sticky=W, **paddings)

# Preenchimento
vai_preencher = BooleanVar(value=False)
ttk.Checkbutton(frame, text="Com Preenchimento", variable=vai_preencher).grid(column=4, row=0, sticky=W, **paddings)

# Cor do preenchimento
ttk.Label(frame, text='Cor do Preenchimento:').grid(column=5, row=0, sticky=W, **paddings)
cor_preench_var = StringVar(root)
cor_preench_var.set('Vermelho')
ttk.OptionMenu(frame, cor_preench_var, 'Vermelho', *nomes_cores).grid(column=6, row=0, sticky=W, **paddings)

# Canvas
canvas = Canvas(frame, bg='white', width=650, height=600)
canvas.grid(column=0, row=1, columnspan=7, sticky=W, **paddings)

frame.pack()

# Bindings
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
