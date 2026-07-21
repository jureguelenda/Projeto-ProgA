# modelo/persistencia.py
import json

from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, PoligonoRegular

# Fábrica de tipos: liga o nome gravado no JSON (figura.to_dict()["tipo"])
# à classe capaz de reconstruí-la via from_dict(). É a única "decisão de
# tipo" deste módulo — cada classe continua responsável por saber
# serializar/desserializar a si mesma.
_TIPOS_FIGURA = {
    "Linha": Linha,
    "Rabisco": Rabisco,
    "Retangulo": Retangulo,
    "Oval": Oval,
    "Circulo": Circulo,
    "PoligonoRegular": PoligonoRegular,
}


def salvar_desenho(modelo, caminho):
    """Grava todas as figuras concluídas do modelo em um arquivo JSON.

    A figura em construção (figura_nova) não é salva, pois ainda não é
    uma figura válida (is_completa() poderia ser falso)."""
    dados = [figura.to_dict() for figura in modelo.figuras]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


def abrir_desenho(modelo, caminho):
    """Lê um arquivo JSON e substitui o conteúdo do modelo pelas figuras nele descritas.

    Lança ValueError se o arquivo contiver um tipo de figura desconhecido
    ou dados incompletos, para que o chamador possa avisar o usuário."""
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    figuras = []
    for item in dados:
        tipo = item.get("tipo")
        classe = _TIPOS_FIGURA.get(tipo)
        if classe is None:
            raise ValueError(f"Tipo de figura desconhecido no arquivo: {tipo!r}")
        try:
            figuras.append(classe.from_dict(item))
        except KeyError as campo_faltante:
            raise ValueError(
                f"Dado ausente para reconstruir '{tipo}': {campo_faltante}"
            ) from campo_faltante

    modelo.carregar_figuras(figuras)
