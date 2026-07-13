from tkinter import *
from tkinter import ttk

# Importações dos módulos desenvolvidos pelos parceiros de grupo
from figuras_base import Linha, Rabisco
from de_oo_1 import Retangulo, Oval, Circulo ,PoligonoRegular

# Dicionário para traduzir o nome em português para a cor que o Tkinter entende
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

# Variáveis globais
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
        # CORREÇÃO: Uso de **2 para elevar ao quadrado e **0.5 para raiz quadrada (Teorema de Pitágoras)
        figura_nova.raio = ((cx - x)**2 + (cy - y)**2)**0.5
    elif isinstance(figura_nova, PoligonoRegular):
        cx, cy = figura_nova.cx, figura_nova.cy
        # CORREÇÃO: Mesma correção matemática aplicada aqui
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
ttk.OptionMenu(frame, tipo_figura_var, 'Linha', 
              'Linha', 'Rabisco', 'Círculo', 'Retângulo', 'Oval', 'Polígono Regular').grid(
              column=1, row=0, sticky=W, **paddings)

# Cor da borda
ttk.Label(frame, text='Cor da Borda:').grid(column=2, row=0, sticky=W, **paddings)
cor_borda_var = StringVar(root)
ttk.OptionMenu(frame, cor_borda_var, 'Preto', *nomes_cores).grid(column=3, row=0, sticky=W, **paddings)

# Preenchimento
vai_preencher = BooleanVar(value=False)
ttk.Checkbutton(frame, text="Com Preenchimento", variable=vai_preencher).grid(column=4, row=0, sticky=W, **paddings)

# Cor do preenchimento
ttk.Label(frame, text='Cor do Preenchimento:').grid(column=5, row=0, sticky=W, **paddings)
cor_preench_var = StringVar(root)
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