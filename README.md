# convert2ebook.py

## Version Française

Script Python pour convertir un ou plusieurs fichiers ODT en PDF et/ou ePub.

### Fonctionnalités

- Convertit un fichier `.odt` en PDF et/ou ePub.
- Supporte plusieurs fichiers à la fois.
- Choix du dossier de sortie.
- Vérifie Pandoc et LaTeX (optionnel pour PDF).

### Prérequis

- Python 3
- [pypandoc](https://pypi.org/project/pypandoc/) : `pip install pypandoc`
- [Pandoc](https://pandoc.org/installing.html)
- LaTeX (optionnel pour PDF de meilleure qualité)

### Usage

\`\`\`bash
python convert2ebook.py [--pdf|--epub] [--output dossier] <fichier1.odt> [fichier2.odt] ...
\`\`\`

#### Options

\| Option          \| Description \|
\|-----------------\|-------------\|
\| `--pdf`         \| Génère uniquement le PDF \|
\| `--epub`        \| Génère uniquement le ePub \|
\| `--output DIR`  \| Dossier de sortie (par défaut : dossier courant) \|

#### Exemples

- PDF + ePub :  
\`\`\`bash
python convert2ebook.py mon_doc.odt
\`\`\`

- PDF seulement :  
\`\`\`bash
python convert2ebook.py --pdf mon_doc.odt
\`\`\`

- ePub seulement dans `ebooks/` :  
\`\`\`bash
python convert2ebook.py --epub --output ebooks mon_doc.odt
\`\`\`

- Plusieurs fichiers :  
\`\`\`bash
python convert2ebook.py doc1.odt doc2.odt --output ebooks
\`\`\`

---

**English version below**

---

## English Version

Python script to convert one or multiple ODT files to PDF and/or ePub.

### Features

- Convert `.odt` files to PDF and/or ePub.
- Supports multiple files in a single command.
- Allows specifying output folder.
- Checks for Pandoc and LaTeX (optional for PDF).

### Prerequisites

- Python 3
- [pypandoc](https://pypi.org/project/pypandoc/) : `pip install pypandoc`
- [Pandoc](https://pandoc.org/installing.html)
- LaTeX (optional for better PDF rendering)

### Usage

\`\`\`bash
python convert2ebook.py [--pdf|--epub] [--output folder] <file1.odt> [file2.odt] ...
\`\`\`

#### Options

\| Option          \| Description \|
\|-----------------\|-------------\|
\| `--pdf`         \| Generate PDF only \|
\| `--epub`        \| Generate ePub only \|
\| `--output DIR`  \| Output folder (default: current directory) \|

#### Examples

- PDF + ePub:  
\`\`\`bash
python convert2ebook.py my_doc.odt
\`\`\`

- PDF only:  
\`\`\`bash
python convert2ebook.py --pdf my_doc.odt
\`\`\`

- ePub only, output to `ebooks/`:  
\`\`\`bash
python convert2ebook.py --epub --output ebooks my_doc.odt
\`\`\`

- Multiple files:  
\`\`\`bash
python convert2ebook.py doc1.odt doc2.odt --output ebooks
\`\`\`
