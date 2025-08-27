#!/usr/bin/env python3
"""
convert2ebook.py

Script Python pour convertir un ou plusieurs fichiers ODT en PDF et/ou ePub
en utilisant Pandoc (avec pypandoc). La génération PDF est optimisée si un
moteur LaTeX moderne comme XeLaTeX est installé.

Python script to convert one or multiple ODT files to PDF and/or ePub
using Pandoc (via pypandoc). PDF generation is optimized if a modern LaTeX
engine like XeLaTeX is installed.

Toutes les sorties console sont affichées en français et en anglais.
All console outputs are displayed in French and English.
"""

import sys
import os
import shutil

# Variable globale pour stocker le moteur PDF à utiliser
PDF_ENGINE = None

def msg(fr, en):
    return f"{fr} / {en}"

try:
    import pypandoc
except ImportError:
    print(msg("❌ Le module 'pypandoc' n'est pas installé.",
              "❌ The 'pypandoc' module is not installed."))
    print(msg("👉 Installe-le avec : pip install pypandoc",
              "👉 Install with: pip install pypandoc"))
    sys.exit(1)

def check_dependencies():
    global PDF_ENGINE
    if not shutil.which("pandoc"):
        print(msg("❌ Pandoc n'est pas installé ou introuvable dans le PATH.",
                  "❌ Pandoc is not installed or not in PATH."))
        print(msg("👉 Installe-le ici : https://pandoc.org/installing.html",
                  "👉 Install here: https://pandoc.org/installing.html"))
        sys.exit(1)
    else:
        print(msg("✅ Pandoc détecté", "✅ Pandoc detected"))

    # Détection du moteur LaTeX, priorité à xelatex pour la compatibilité Unicode
    if shutil.which("xelatex"):
        print(msg("✅ Moteur XeLaTeX détecté (PDF optimal avec support Unicode)",
                  "✅ XeLaTeX engine detected (optimal PDF with Unicode support)"))
        PDF_ENGINE = "xelatex"
    elif shutil.which("pdflatex") or shutil.which("lualatex"):
        print(msg("✅ Système LaTeX détecté (PDF optimal)",
                  "✅ LaTeX system detected (optimal PDF)"))
    else:
        print(msg("⚠️  Aucun moteur LaTeX détecté, la qualité du PDF sera basique",
                  "⚠️  No LaTeX engine detected, PDF quality will be basic"))
        print(msg("👉 Pour un meilleur résultat, installe TeX Live ou MikTeX",
                  "👉 For best results, install TeX Live or MikTeX"))

def convert_to_ebook(input_file: str, make_pdf: bool, make_epub: bool, output_dir: str):
    if not os.path.isfile(input_file):
        print(msg(f"❌ Fichier introuvable : {input_file}",
                  f"❌ File not found: {input_file}"))
        return

    base_name = os.path.splitext(os.path.basename(input_file))[0]

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    try:
        if make_pdf:
            pdf_file = os.path.join(output_dir, f"{base_name}.pdf")
            extra_args = ['--standalone']
            if PDF_ENGINE:
                extra_args.append(f'--pdf-engine={PDF_ENGINE}')
            
            pypandoc.convert_file(input_file, 'pdf', outputfile=pdf_file, extra_args=extra_args)
            print(msg(f"✅ PDF généré : {pdf_file}",
                      f"✅ PDF generated: {pdf_file}"))

        if make_epub:
            epub_file = os.path.join(output_dir, f"{base_name}.epub")
            pypandoc.convert_file(input_file, 'epub', outputfile=epub_file, extra_args=['--standalone'])
            print(msg(f"✅ ePub généré : {epub_file}",
                      f"✅ ePub generated: {epub_file}"))

    except Exception as e:
        print(msg(f"❌ Erreur pendant la conversion de {input_file} : {e}",
                  f"❌ Error converting {input_file} : {e}"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(msg("Usage: convert2ebook.py [--pdf|--epub] [--output dossier] <fichier1.odt> [fichier2.odt] ...",
                  "Usage: convert2ebook.py [--pdf|--epub] [--output folder] <file1.odt> [file2.odt] ..."))
        sys.exit(1)

    make_pdf = True
    make_epub = True
    output_dir = os.getcwd()
    args = sys.argv[1:]

    if "--pdf" in args:
        make_pdf = True
        make_epub = False
        args.remove("--pdf")

    if "--epub" in args:
        make_pdf = False
        make_epub = True
        args.remove("--epub")

    if "--output" in args:
        idx = args.index("--output")
        if idx + 1 >= len(args):
            print(msg("❌ L'option --output nécessite un chemin",
                      "❌ --output option requires a folder path"))
            sys.exit(1)
        output_dir = args[idx + 1]
        args.pop(idx)
        args.pop(idx)

    if not args:
        print(msg("❌ Aucun fichier fourni", "❌ No files provided"))
        sys.exit(1)

    check_dependencies()

    for file in args:
        convert_to_ebook(file, make_pdf, make_epub, output_dir)
