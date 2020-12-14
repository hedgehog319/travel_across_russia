from os import system
from pathlib import Path

file = Path(__file__).parent.absolute()


system(f"postgres -D {file} -p 6666")
