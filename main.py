import tkinter as tk
from tkinter import ttk

from core.conversor import converter_imagens
from core.pdf import juntar_pdfs
from core.separar import separar_pdf


# ----------------------
# Janela Principal
# ----------------------

root = tk.Tk()

root.title("Conversor PDF")
root.geometry("430x270")
root.resizable(False, False)


# ----------------------
# Tema
# ----------------------

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Botao.TButton",
    font=("Segoe UI", 13, "bold"),
    padding=15
)


# ----------------------
# Botão Converter Imagens
# ----------------------

btn_converter = ttk.Button(
    root,
    text="🖼️ Imagens para PDF",
    style="Botao.TButton",
    command=converter_imagens
)

btn_converter.pack(
    fill="x",
    padx=40,
    pady=(30, 10)
)


# ----------------------
# Botão Juntar PDFs
# ----------------------

btn_juntar = ttk.Button(
    root,
    text="📄 Juntar PDFs",
    style="Botao.TButton",
    command=juntar_pdfs
)

btn_juntar.pack(
    fill="x",
    padx=40,
    pady=10
)


# ----------------------
# Botão Separar PDF
# ----------------------

btn_separar = ttk.Button(
    root,
    text="✂️ Separar PDF",
    style="Botao.TButton",
    command=separar_pdf
)

btn_separar.pack(
    fill="x",
    padx=40,
    pady=10
)


# ----------------------
# Loop
# ----------------------

root.mainloop()