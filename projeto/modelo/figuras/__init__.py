# modelo/figuras/__init__.py
"""
Reexporta todas as figuras concretas (estados) para que o restante do
projeto possa importar com `from modelo.figuras import Linha, Circulo, ...`
em vez de precisar conhecer o arquivo individual de cada uma.
"""
from .linha import Linha
from .rabisco import Rabisco
from .retangulo import Retangulo
from .oval import Oval
from .circulo import Circulo
from .poligono_regular import PoligonoRegular

__all__ = [
    "Linha",
    "Rabisco",
    "Retangulo",
    "Oval",
    "Circulo",
    "PoligonoRegular",
]
