# 📁 File Arranger

A lightweight, colorful, and interactive command-line utility written in Python to automatically organize and sort messy directories by file types.

---

## ✨ Features

- **Automated Sorting:** Instantly categorizes files into dedicated folders (`Image`, `Video`, `Audio`, `Executables`, `Python`, and `Others`).
- **Interactive CLI:** Clean and colorful terminal interface powered by `colorama`.
- **Safe Handling:** Uses robust path manipulation via Python's built-in `pathlib`.
- **Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.

---

## 🛠️ Prerequisites

Make sure you have Python installed along with the `colorama` library. You can install colorama via pip:

```bash
pip install colorama
```

---

## 🚀 Usage

1. Clone or download the script.
2. Run the script from your terminal:

```bash
python file_arranger.py
```

3. Choose **Option 1** when prompted.
4. Paste the absolute or relative path of the directory you want to organize.

---

## 📂 Folder Structure Created

When you run the script on a directory, it automatically creates the following categorized subfolders (if they don't already exist):

| Category | Extensions Handled |
| :--- | :--- |
| **Image** | `.jpg`, `.jpeg`, `.png`, `.webp` |
| **Video** | `.mp4`, `.mkv` |
| **Audio** | `.mp3` |
| **Executables** | `.exe` |
| **Python** | `.py` |
| **Others** | Any other file types |

---

## 🐛 Bug Fixes & Improvements

- **Fixed Boolean Evaluation Bug:** Fixed an issue where using `or` incorrectly evaluated non-empty string literals as truthy, causing all files to dump into the Image folder. Replaced with `.endswith()` tuple matching.
- **Case-Insensitive Check:** Ensured file extensions are evaluated reliably regardless of uppercase/lowercase naming conventions.

---

## 📄 License

This project is open-source and free to use for personal productivity enhancements.
