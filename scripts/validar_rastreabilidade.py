#!/usr/bin/env python3
"""Valida rastreabilidade entre diretrizes da PSI, riscos e controles ISO."""
import re
import sys
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parents[1] / "PSI_Clinica_Viver_Bem_v1.2.md"
CONTROLE = re.compile(r"^A\.(?:5|6|7|8)\.\d{1,2}$")
RISCO = re.compile(r"^R-\d{2}$")

def validar(texto):
    problemas = []
    headings = set(re.findall(r"^###\s+(4\.\d+)\.", texto, re.M))
    headings.add("5")
    secao = re.search(r"^## 9\.[^\n]*\n(.*?)(?=^## 10\.|\Z)", texto, re.M | re.S)
    if not secao:
        return ["Seção 9 não encontrada"]
    linhas = [linha for linha in secao.group(1).splitlines() if linha.startswith("|")]
    linhas = [linha for linha in linhas if not re.fullmatch(r"[|:\-\s]+", linha)]
    if len(linhas) < 2:
        return ["Tabela de rastreabilidade vazia"]
    citadas, riscos = set(), set()
    for numero, linha in enumerate(linhas[1:], 1):
        celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(celulas) != 3:
            problemas.append("Linha {}: esperadas três colunas".format(numero))
            continue
        nome, ids, controles = celulas
        citadas.update(re.findall(r"(?<!\d)(4\.\d+)(?!\d)", nome))
        if re.search(r"(?<!\d)5\.(?!\d)", nome):
            citadas.add("5")
        tokens_risco = [s.strip() for s in ids.split(",")]
        tokens_controle = [s.strip() for s in controles.split(",")]
        if not tokens_risco or not all(RISCO.fullmatch(s) for s in tokens_risco):
            problemas.append("Linha {}: IDs de risco inválidos".format(numero))
        riscos.update(s for s in tokens_risco if RISCO.fullmatch(s))
        if not tokens_controle or not all(CONTROLE.fullmatch(s) for s in tokens_controle):
            problemas.append("Linha {}: formato de controle ISO inválido".format(numero))
    for nome in sorted(headings - citadas):
        problemas.append("Seção sem rastreabilidade: {}".format(nome))
    for risco in sorted({"R-{:02d}".format(i) for i in range(1, 11)} - riscos):
        problemas.append("Risco não citado: {}".format(risco))
    return problemas

def main():
    problemas = validar(ARQUIVO.read_text(encoding="utf-8"))
    if problemas:
        for problema in problemas:
            print("ERRO: {}".format(problema), file=sys.stderr)
        return 1
    print("Rastreabilidade válida: seções 4.x e 5, riscos R-01 a R-10 e controles ISO.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
