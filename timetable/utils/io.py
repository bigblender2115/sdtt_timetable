import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "templates"

def load_template(name: str) -> pd.DataFrame:
    """Load a CSV template by name (without extension)."""
    return pd.read_csv(DATA_DIR / f"{name}_template.csv")
