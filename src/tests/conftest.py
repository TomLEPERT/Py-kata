import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # racine du repo
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))