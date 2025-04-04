import subprocess
from pathlib import Path
from fastapi import APIRouter

router = APIRouter(tags=["Database"])

MIGRATIONS_DIR = Path(__file__).parent.parent / "migrations"

@router.post("/migrate")
def run_migrations():
    try:
        result = subprocess.run(
            [
                "docker-compose", "run", "--rm", "flyway", 
                "migrate"
            ],
            capture_output=True,
            text=True
        )
        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {"success": False, "error": str(e)}