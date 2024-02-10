import fitz

def extrair_texto_pdf(caminho_pdf):
    texto = ''
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto
