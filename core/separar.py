from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def separar_pdf():

    arquivo = filedialog.askopenfilename(
        title="Escolha o PDF para separar",
        filetypes=[
            ("Arquivos PDF", "*.pdf")
        ]
    )

    if not arquivo:
        return


    try:

        arquivo = Path(arquivo)

        pasta_destino = arquivo.parent / f"{arquivo.stem}_separado"

        pasta_destino.mkdir(exist_ok=True)


        leitor = PdfReader(arquivo)


        for numero, pagina in enumerate(leitor.pages, start=1):

            escritor = PdfWriter()

            escritor.add_page(pagina)


            destino = pasta_destino / f"{arquivo.stem}_pagina_{numero}.pdf"


            with open(destino, "wb") as pdf_saida:
                escritor.write(pdf_saida)


        messagebox.showinfo(
            "Concluído",
            f"PDF separado com sucesso!\n\nArquivos salvos em:\n{pasta_destino}"
        )


    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Não foi possível separar o PDF.\n\n{erro}"
        )