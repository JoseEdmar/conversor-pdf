# Conversor PDF

Aplicativo desktop desenvolvido em Python para conversão e gerenciamento de arquivos PDF.

## Funcionalidades

- 🖼️ Converter imagens para PDF usando ImageMagick
- 📄 Juntar múltiplos arquivos PDF em um único arquivo
- ✂️ Separar páginas de um PDF em arquivos individuais
- Interface gráfica simples utilizando Tkinter
- Processamento totalmente local

## Tecnologias utilizadas

- Python
- Tkinter
- ImageMagick
- pypdf

## Estrutura do projeto

```
ConversorPDF/
│
├── main.py
│
├── core/
│   ├── conversor.py
│   ├── pdf.py
│   └── separar.py
│
├── requirements.txt
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/JoseEdmar/conversor-pdf.git
```

Entre na pasta do projeto:

```bash
cd conversor-pdf
```

Crie o ambiente virtual:

```bash
python -m venv env
```

Ative o ambiente virtual:

Windows:

```bash
env\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Também é necessário instalar o ImageMagick:

https://imagemagick.org/

Após a instalação, verifique:

```bash
magick -version
```

## Executando

Execute o aplicativo:

```bash
python main.py
```

## Dependências

O arquivo `requirements.txt` contém:

```
pypdf
```

## Autor

José Edmar Constantino Gouveia

GitHub:
https://github.com/JoseEdmar