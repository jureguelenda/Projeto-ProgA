# main.py
from modelo.modelo_desenho import ModeloDesenho
from visao.tela import TelaDesenho
from controlador.controlador_desenho import ControladorDesenho


def main():
    modelo = ModeloDesenho()
    visao = TelaDesenho()
    ControladorDesenho(modelo, visao)
    visao.mainloop()


if __name__ == "__main__":
    main()
