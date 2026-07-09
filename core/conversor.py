from tkinter import filedialog, messagebox
from pathlib import Path
import subprocess


def converter_imagens():

    arquivos = filedialog.askopenfilenames(
        title="Escolha as imagens",
        filetypes=[
            (
                "Imagens",
                "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"
            )
        ]
    )

    if not arquivos:
        return

    convertidos = 0

    try:

        for arquivo in arquivos:

            arquivo = Path(arquivo)

            destino = arquivo.with_suffix(".pdf")

            subprocess.run(
                [
                    "magick",
                    str(arquivo),
                    str(destino)
                ],
                check=True
            )

            convertidos += 1

        messagebox.showinfo(
            "Concluído",
            f"{convertidos} imagem(ns) convertida(s) para PDF."
        )

    except FileNotFoundError:

        messagebox.showerror(
            "Erro",
            "ImageMagick não foi encontrado."
        )

    except subprocess.CalledProcessError:

        messagebox.showerror(
            "Erro",
            "Erro durante a conversão."
        )