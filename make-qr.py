#!/usr/bin/env python3
"""Génère le QR code pointant vers le notebook JupyterLite.

Usage :
    python make-qr.py "https://MON-COMPTE.github.io/MON-DEPOT/notebooks/index.html?path=ic-gaussien.ipynb"

Produit le fichier  qr-code-notebook-jupyterlite.png  (à placer dans le dossier images/ des slides).
"""
import sys
import qrcode

URL_PAR_DEFAUT = (
    "https://MON-COMPTE.github.io/MON-DEPOT/notebooks/index.html?path=ic-gaussien.ipynb"
)

url = sys.argv[1] if len(sys.argv) > 1 else URL_PAR_DEFAUT

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code-notebook-jupyterlite.png")
print("QR code écrit -> qr-code-notebook-jupyterlite.png")
print("URL encodée :", url)
