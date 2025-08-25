from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)
                
import src.c.d
print("I am b2.py under a")
