import tkinter as tk

from core.conversor import converter_imagens
from core.pdf import juntar_pdfs
from core.separar import separar_pdf


# ----------------------
# Janela Principal
# ----------------------

root = tk.Tk()

root.title("Conversor PDF")
root.geometry("430x300")
root.resizable(False, False)

root.configure(
    bg="#f0f0f0"
)


# ----------------------
# Configuração dos botões
# ----------------------

config_botao = {
    "font": ("Segoe UI", 13, "bold"),
    "fg": "black",
    "relief": "flat",
    "cursor": "hand2",
    "height": 2
}


# ----------------------
# Botão Converter Imagens
# ----------------------

btn_converter = tk.Button(
    root,
    text="🖼️ Imagens para PDF",
    bg="#4CAF50",
    activebackground="#45a049",
    command=converter_imagens,
    **config_botao
)

btn_converter.pack(
    fill="x",
    padx=40,
    pady=(35, 10)
)


# ----------------------
# Botão Juntar PDFs
# ----------------------

btn_juntar = tk.Button(
    root,
    text="📄 Juntar PDFs",
    bg="#2196F3",
    activebackground="#1976D2",
    command=juntar_pdfs,
    **config_botao
)

btn_juntar.pack(
    fill="x",
    padx=40,
    pady=10
)


# ----------------------
# Botão Separar PDF
# ----------------------

btn_separar = tk.Button(
    root,
    text="✂️ Separar PDF",
    bg="#FF9800",
    activebackground="#F57C00",
    command=separar_pdf,
    **config_botao
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