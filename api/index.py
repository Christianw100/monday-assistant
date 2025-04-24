import sys
import os
from pathlib import Path

# Agrega el path raíz al sys.path
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

# Importa app correctamente
from app import app

handler = app
