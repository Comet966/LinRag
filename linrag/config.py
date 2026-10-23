import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Endpoint:
    base_url: str = ""
    api_key: str = ""
    model: str = ""

    @property
    def ready(self) -> bool:
        return bool(self.base_url and self.api_key and self.model)


@dataclass(frozen=True)
class Settings:
    data_dir: Path = Path("data")
    embed: Endpoint = Endpoint()
    timeout: float = 45
    batch_size: int = 16

    @classmethod
    def load(cls) -> "Settings":
        load_dotenv()

        def endpoint(prefix: str) -> Endpoint:
            return Endpoint(
                *(os.getenv(f"{prefix}_{key}", "").strip() for key in ("BASE_URL", "API_KEY", "MODEL"))
            )

        return cls(
            Path(os.getenv("DATA_DIR", "data")),
            endpoint("EMBED"),
            max(1, float(os.getenv("API_TIMEOUT", "45"))),
            max(1, int(os.getenv("EMBED_BATCH_SIZE", "16"))),
        )
