<p align="center">
  <img src="https://github.com/diegopereiracruz/Encontrar-PDF/blob/main/print.jpg?raw=true" alt="Interface da Aplicação"/>
</p>

# Encontrar PDF
Um buscador de arquivos PDF que realiza uma varredura no conteúdo de cada arquivo e procura pela palavra especificada no campo superior.
A busca é feita na pasta especificada, selecionada pelo botão "Escolher pasta...".

## Instalação
###### Windows
Baixe o executável na página [releases](https://github.com/diegopereiracruz/Encontrar-PDF/releases/tag/Windows).

###### Linux
Clone o repositório:
```sh
mkdir ~/git-clones && cd ~/git-clones && 
git clone https://github.com/diegopereiracruz/Encontrar-PDF.git && 
cd Encontrar-PDF
```

Crie um ambiente virtual:
``` sh
pip3 install virtualenv &&
virtualenv venv &&
source venv/bin/activate
```

Instale as dependencias em requirements.txt e o PyPDF2:
``` sh
pip3 install -r requirements.txt &&
pip3 install PyPDF2
```

Instale o Tkinter:
``` sh
sudo apt install python3-tk
```

Execute o programa:
``` sh
python3 Encontrar-PDF.py
```


## Autor
Github: [Diego Pereira Cruz](https://github.com/diegopereiracruz/)
