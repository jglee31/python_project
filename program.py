import os
from pathlib import Path
os.mkdir(Path.home() / "python")
with open(Path.home() / "python" / "example.txt", "w") as file:
    file.write("Hello, this is a sample text.")

