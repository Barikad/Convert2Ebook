# Convert2eBook

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandoc](https://img.shields.io/badge/Pandoc-Required-yellow.svg?style=for-the-badge&logo=pandoc)](https://pandoc.org/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/agpl-3.0)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg?style=for-the-badge&logo=linux)](https://www.linux.org/)

> **Note sur le Dépôt Officiel**
>
> Ce projet est maintenu sur le [GitLab de la Mairie de Villejuif](https://gitlab.villejuif.fr/J-COQBLIN/convert2ebook). Des miroirs en lecture seule peuvent exister sur d'autres plateformes (GitHub, etc.), mais cette instance est la seule source officielle. Toutes les contributions (tickets, requêtes de fusion) doivent y être soumises.
>
> ---
>
> **Note on the Official Repository**
>
> This project is maintained on the [Mairie de Villejuif's GitLab](https://gitlab.villejuif.fr/J-COQBLIN/convert2ebook). Read-only mirrors may exist on other platforms (GitHub, etc.), but this instance is the single source of truth. All contributions (issues, merge requests) must be submitted here.

[English Version below](#english-version)

## 🇫🇷 Version Française

### Objectif
`Convert2eBook` est un script en ligne de commande qui utilise la puissance de **Pandoc** pour convertir facilement un ou plusieurs documents au format `.odt` (OpenDocument Text) en fichiers `.pdf` et/ou `.epub`.

C'est l'outil idéal pour transformer rapidement vos manuscrits, rapports ou documents en formats prêts pour la lecture sur liseuse ou pour une distribution universelle.

### ✨ Fonctionnalités
- **Conversion Multiple :** Convertit un ou plusieurs fichiers `.odt` en une seule commande.
- **Formats Flexibles :** Génère des fichiers PDF, ePub, ou les deux simultanément.
- **Support Unicode Amélioré (PDF) :** Utilise automatiquement le moteur `xelatex` s'il est disponible pour une prise en charge complète des caractères spéciaux et internationaux.
- **Sortie Personnalisée :** Permet de spécifier un répertoire de sortie pour organiser vos fichiers convertis.
- **Vérification des Dépendances :** Contrôle la présence de `Pandoc` et `LaTeX` pour assurer un fonctionnement optimal.
- **Multi-plateforme :** Fonctionne sur Windows, macOS et Linux.

### 🛠️ Prérequis
Avant de lancer le script, assurez-vous que les outils suivants sont installés sur votre système :

1.  **Python 3.6+**
2.  **Pandoc :** L'outil de conversion de documents universel.
    -   *Instructions d'installation :* [pandoc.org/installing.html](https://pandoc.org/installing.html)
3.  **(Fortement Recommandé pour les PDF) Une distribution LaTeX :** Pour générer des PDF de haute qualité avec une prise en charge complète des caractères Unicode (accents, alphabets non-latins, etc.).
    -   *Windows :* [MiKTeX](https://miktex.org/)
    -   *macOS :* [MacTeX](https://www.tug.org/mactex/)
    -   *Linux (Debian/Ubuntu) :* `sudo apt-get install texlive-full`

*Note : Sans LaTeX, la conversion PDF ne fonctionnera pas ou produira un résultat de qualité inférieure via un autre moteur de Pandoc.*

### 🚀 Installation
1.  Clonez ce dépôt ou téléchargez le script `convert2ebook.py`.
2.  Installez la dépendance Python nécessaire via `pip` :
    ```bash
    pip install pypandoc
    ```

### 📖 Utilisation
Le script s'utilise directement en ligne de commande.

```bash
python convert2ebook.py [OPTIONS] <fichier1.odt> [fichier2.odt...]
```

**Options :**

| Option | Description |
|---|---|
| `--pdf` | Génère **uniquement** le(s) fichier(s) PDF. |
| `--epub` | Génère **uniquement** le(s) fichier(s) ePub. |
| `--output <dossier>` | Spécifie le répertoire où les fichiers convertis seront sauvegardés. Par défaut, ils sont créés dans le répertoire courant. |

*Note : Si ni `--pdf` ni `--epub` ne sont spécifiés, les deux formats seront générés.*

### 💡 Exemples

1.  **Convertir un fichier en PDF et ePub :**
    ```bash
    python convert2ebook.py "Mon Document.odt"
    ```

2.  **Convertir un fichier en PDF uniquement :**
    ```bash
    python convert2ebook.py --pdf "Mon Document.odt"
    ```

3.  **Convertir plusieurs fichiers en ePub et les placer dans un dossier `Sortie` :**
    ```bash
    python convert2ebook.py --epub --output Sortie "Chapitre 1.odt" "Chapitre 2.odt"
    ```

### ⚖️ Licence
Ce projet est sous licence AGPLv3. Voir le fichier `LICENSE` pour plus de détails.

---
<a name="english-version"></a>

## 🇬🇧 English Version

### Objective
`Convert2eBook` is a command-line script that leverages the power of **Pandoc** to easily convert one or more `.odt` (OpenDocument Text) documents into `.pdf` and/or `.epub` files.

It's the ideal tool to quickly transform your manuscripts, reports, or documents into formats ready for e-readers or universal distribution.

### ✨ Features
- **Batch Conversion:** Convert one or more `.odt` files in a single command.
- **Flexible Formats:** Generate PDF, ePub, or both formats simultaneously.
- **Enhanced Unicode Support (PDF):** Automatically uses the `xelatex` engine if available for full support of special and international characters.
- **Custom Output:** Allows specifying an output directory to organize your converted files.
- **Dependency Check:** Checks for `Pandoc` and `LaTeX` to ensure optimal performance.
- **Cross-platform:** Works on Windows, macOS, and Linux.

### 🛠️ Prerequisites
Before running the script, ensure the following tools are installed on your system:

1.  **Python 3.6+**
2.  **Pandoc:** The universal document converter.
    -   *Installation instructions:* [pandoc.org/installing.html](https://pandoc.org/installing.html)
3.  **(Strongly Recommended for PDFs) A LaTeX distribution:** To generate high-quality PDFs with full support for Unicode characters (accents, non-Latin alphabets, etc.).
    -   *Windows:* [MiKTeX](https://miktex.org/)
    -   *macOS:* [MacTeX](https://www.tug.org/mactex/)
    -   *Linux (Debian/Ubuntu):* `sudo apt-get install texlive-full`

*Note: Without LaTeX, PDF conversion will either fail or produce a lower-quality result through another Pandoc engine.*

### 🚀 Installation
1.  Clone this repository or download the `convert2ebook.py` script.
2.  Install the required Python dependency using `pip`:
    ```bash
    pip install pypandoc
    ```

### 📖 Usage
The script is used directly from the command line.

```bash
python convert2ebook.py [OPTIONS] <file1.odt> [file2.odt...]
```

**Options:**

| Option | Description |
|---|---|
| `--pdf` | Generates PDF file(s) **only**. |
| `--epub` | Generates ePub file(s) **only**. |
| `--output <directory>` | Specifies the directory where the converted files will be saved. By default, they are created in the current directory. |

*Note: If neither `--pdf` nor `--epub` is specified, both formats will be generated.*

### 💡 Examples

1.  **Convert a file to both PDF and ePub:**
    ```bash
    python convert2ebook.py "My Document.odt"
    ```

2.  **Convert a file to PDF only:**
    ```bash
    python convert2ebook.py --pdf "My Document.odt"
    ```

3.  **Convert multiple files to ePub and place them in an `Output` folder:**
    ```bash
    python convert2ebook.py --epub --output Output "Chapter 1.odt" "Chapter 2.odt"
    ```

### ⚖️ Licence
This project is licensed under the AGPLv3 License. See the `LICENSE` file for more details.