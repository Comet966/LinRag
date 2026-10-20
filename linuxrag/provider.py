import httpx
import numpy as np

from .config import Endpoint


class ProviderError(RuntimeError):
    pass


class Provider:
    def __init__(self, timeout: float = 45, transport=None):
        self.timeout = timeout
        self.transport = transport

    def post(self, endpoint: Endpoint, route: str, payload: dict) -> dict:
        if not endpoint.ready:
            raise ProviderError("模型配置不完整，请检查地址、密钥和模型名。")
        try:
            with httpx.Client(timeout=self.timeout, transport=self.transport) as client:
                response = client.post(
                    f"{endpoint.base_url.rstrip('/')}/{route}",
                    headers={"Authorization": f"Bearer {endpoint.api_key}"},
                    json={"model": endpoint.model, **payload},
                )
                response.raise_for_status()
                result = response.json()
                if not isinstance(result, dict):
                    raise TypeError("Expected object")
                return result
        except httpx.TimeoutException as exc:
            raise ProviderError("模型服务请求超时，请稍后重试。") from exc
        except httpx.HTTPStatusError as exc:
            # Do not return upstream response bodies, URLs or credentials to clients.
            raise ProviderError(f"模型服务返回 HTTP {exc.response.status_code}，请检查配置或配额。") from exc
        except (httpx.RequestError, httpx.InvalidURL, ValueError, TypeError) as exc:
            raise ProviderError("模型服务连接失败或响应格式无效。") from exc

    def embeddings(self, endpoint: Endpoint, texts: list[str]) -> np.ndarray:
        payload = self.post(endpoint, "embeddings", {"input": texts, "encoding_format": "float"})
        try:
            rows = sorted(payload["data"], key=lambda item: item["index"])
            if [row["index"] for row in rows] != list(range(len(texts))):
                raise ValueError("Embedding indices mismatch")
            vectors = np.asarray([row["embedding"] for row in rows], dtype=np.float32)
            if vectors.ndim != 2 or not vectors.shape[1] or not np.isfinite(vectors).all():
                raise ValueError("Invalid vectors")
            norms = np.linalg.norm(vectors, axis=1, keepdims=True)
            if (norms == 0).any():
                raise ValueError("Zero vectors")
            return vectors / norms
        except (KeyError, TypeError, ValueError) as exc:
            raise ProviderError("向量响应无效：数量、维度或数值不正确。") from exc
