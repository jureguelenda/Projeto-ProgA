from tkinter import *
from tkinter import ttk

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

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    # Pega as cores dos OptionMenus baseando-se no dicionário
    c_borda = CORES_MAP[cor_borda_var.get()]
    c_preenchimento = CORES_MAP[cor_preench_var.get()] if vai_preencher.get() else ''

    if tipo in ['Linha', 'Retângulo', 'Oval']:
        tag = 'retangulo' if tipo == 'Retângulo' else tipo.lower()
        figura_nova = (tag, (event.x, event.y, event.x, event.y), c_borda, c_preenchimento)
    elif tipo == 'Círculo':
        figura_nova = ("circulo", (event.x, event.y, 0), c_borda, c_preenchimento)
    else: # Rabisco
        figura_nova = ("rabisco", [(event.x, event.y)], c_borda)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
        
    tipo = figura_nova[0]
    
    if tipo == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif tipo in ["linha", "retangulo", "oval"]:
        figura_nova = (tipo, (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    elif tipo == "circulo":
        cx, cy = figura_nova[1][0], figura_nova[1][1]
        raio = ((cx - event.x)**2 + (cy - event.y)**2) ** 0.5
        figura_nova = ("circulo", (cx, cy, raio), figura_nova[2], figura_nova[3])
        
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    global figura_nova
    if figura_nova and not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()
    figura_nova = None

def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        tipo = figura[0]
        
        if tipo == "linha":
            _, values, cb, _ = figura
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cb)
        elif tipo == "retangulo":
            _, values, cb, cp = figura
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cb, fill=cp)
        elif tipo == "oval":
            _, values, cb, cp = figura
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=cb, fill=cp)
        elif tipo == "circulo":
            _, (cx, cy, r), cb, cp = figura
            canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline=cb, fill=cp)
        elif tipo == "rabisco":
            _, values, cb = figura
            canvas.create_line(values, fill=cb)

def desenhar_figura_nova():
    if figura_nova is None:
        return
        
    tipo = figura_nova[0]
    if tipo == "linha":
        _, values, _, _ = figura_nova
        canvas.create_line(values[0], values[1], values[2], values[3], fill="gray", dash=(4, 2))
    elif tipo == "retangulo":
        _, values, _, cp = figura_nova
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline="black", fill=cp, dash=(4, 2))
    elif tipo == "oval":
        _, values, _, cp = figura_nova
        canvas.create_oval(values[0], values[1], values[2], values[3], outline="black", fill=cp, dash=(4, 2))
    elif tipo == "circulo":
        _, (cx, cy, r), _, cp = figura_nova
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black", fill=cp, dash=(4, 2))
    elif tipo == "rabisco":
        _, values, _ = figura_nova
        canvas.create_line(values, fill="gray", dash=(4, 2))

def incompleta(figura):
    fig = figura[0]
    values = figura[1]
    if fig in ["linha", "retangulo", "oval"]:
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "circulo":
        return values[2] == 0 
    elif fig == "rabisco":
        return len(values) <= 1


#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

nomes_cores = list(CORES_MAP.keys())

root = Tk()
root.title("projeto prog A")
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5} 

# label ferramenta
label = ttk.Label(frame, text='Linha ou Rabisco:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu ferramenta
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu
option_menu = ttk.OptionMenu(frame, tipo_figura_var, 'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retângulo', 'Oval')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Configuração da Cor da Borda
label_borda = ttk.Label(frame, text='Cor da Borda:')
label_borda.grid(column=2, row=0, sticky=W, **paddings)

cor_borda_var = StringVar(root)
option_menu_borda = ttk.OptionMenu(frame, cor_borda_var, 'Preto', *nomes_cores)
option_menu_borda.grid(column=3, row=0, sticky=W, **paddings)

# Ativador de preenchimento
vai_preencher = BooleanVar(value=False)
chk_preencher = ttk.Checkbutton(frame, text="Com Preenchimento", variable=vai_preencher)
chk_preencher.grid(column=4, row=0, sticky=W, **paddings)

# Configuração da Cor do Preenchimento
label_preench = ttk.Label(frame, text='Cor do Preenchimento:')
label_preench.grid(column=5, row=0, sticky=W, **paddings)

cor_preench_var = StringVar(root)
option_menu_preench = ttk.OptionMenu(frame, cor_preench_var, 'Vermelho', *nomes_cores)
option_menu_preench.grid(column=6, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=650, height=600)
canvas.grid(column=0, row=1, columnspan=7, sticky=W, **paddings)

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()