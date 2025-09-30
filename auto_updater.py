import requests
import zipfile
import io
import shutil
import tempfile
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

GITHUB_REPO = "JAPB970312/Generador_Constancias"
API_COMMITS = f"https://api.github.com/repos/{GITHUB_REPO}/commits/main"
DOWNLOAD_ZIP = f"https://github.com/{GITHUB_REPO}/archive/refs/heads/main.zip"


def get_remote_commit_sha():
    """Obtiene el último commit SHA del branch main en GitHub."""
    r = requests.get(API_COMMITS, timeout=10)
    r.raise_for_status()
    return r.json()[0]["sha"]


def download_and_extract_update(target_dir: str):
    """
    Descarga la última versión del repositorio y actualiza el directorio local.
    ⚠ Nota: Si la app está empaquetada como EXE, este método solo descarga la
    actualización. El usuario debe reinstalar manualmente.
    """
    logger.info("Descargando actualización desde GitHub...")
    r = requests.get(DOWNLOAD_ZIP, stream=True, timeout=30)
    r.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(r.content)) as zf, tempfile.TemporaryDirectory() as td:
        zf.extractall(td)
        root = Path(td) / os.listdir(td)[0]
        for item in root.iterdir():
            dest = Path(target_dir) / item.name
            if item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            else:
                shutil.copy(item, dest)

    logger.info("Actualización aplicada en %s", target_dir)
