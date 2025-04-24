import sys
import os
from pathlib import Path

# Asegura que se puede importar desde el nivel raíz
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app as handler

