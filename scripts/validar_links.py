#!/usr/bin/env python3
"""Confere links Markdown relativos e URLs GitHub documentadas, sem rede."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
def validar():
    erros=[]
    for doc in ROOT.rglob("*.md"):
        texto=doc.read_text(encoding="utf-8")
        for destino in LINK.findall(texto):
            url=destino.split(" ",1)[0].strip("<>")
            if not url or url=="#":
                erros.append("{}: link vazio".format(doc.relative_to(ROOT)))
                continue
            parsed=urlsplit(url)
            if parsed.scheme in ("http","https","mailto"):
                continue
            if parsed.scheme:
                erros.append("{}: protocolo não suportado {}".format(doc.relative_to(ROOT),url))
                continue
            caminho=unquote(parsed.path)
            arquivo=(doc.parent/caminho).resolve() if caminho else doc.resolve()
            if not arquivo.is_relative_to(ROOT.resolve()) or not arquivo.exists():
                erros.append("{}: link não encontrado {}".format(doc.relative_to(ROOT),url))
    return erros
if __name__=="__main__":
    erros=validar()
    for erro in erros: print("ERRO:",erro,file=sys.stderr)
    print("Links locais válidos." if not erros else "{} link(s) inválido(s).".format(len(erros)))
    sys.exit(bool(erros))
