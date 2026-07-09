from tkinter import filedialog, messagebox
from pypdf import PdfWriter


def juntar_pdfs():

    arquivos = filedialog.askopenfilenames(
        title="Escolha os PDFs",
        filetypes=[
            ("Arquivos PDF", "*.pdf")
        ]
    )

    if not arquivos:
        return

    destino = filedialog.asksaveasfilename(
        title="Salvar PDF final",
        defaultextension=".pdf",
        filetypes=[
            ("Arquivos PDF", "*.pdf")
        ],
        initialfile="PDF_FINAL.pdf"
    )

    if not destino:
        return

    try:

        writer = PdfWriter()

        for pdf in arquivos:
            writer.append(pdf)

        with open(destino, "wb") as arquivo_saida:
            writer.write(arquivo_saida)

        writer.close()

        messagebox.showinfo(
            "Concluído",
            "PDF criado com sucesso."
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Não foi possível juntar os PDFs.\n\n{erro}"
        )