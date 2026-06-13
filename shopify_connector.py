import json
import time
import urllib.error
import urllib.request
from typing import Any, Dict, Optional

try:
    import config
except Exception:
    config = None


class ShopifyConnector:
    def __init__(self, store_domain: Optional[str] = None, token: Optional[str] = None, api_version: Optional[str] = None, dry_run: Optional[bool] = None):
        if config is None and (not store_domain or not token):
            raise RuntimeError("Missing config.py. Rename config_template.py to config.py and add your Shopify token.")
        self.store_domain = store_domain or config.SHOPIFY_STORE_DOMAIN
        self.token = token or config.SHOPIFY_ADMIN_TOKEN
        self.api_version = api_version or getattr(config, "API_VERSION", "2025-04")
        self.dry_run = getattr(config, "DRY_RUN", True) if dry_run is None else dry_run
        self.base_url = f"https://{self.store_domain}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": self.token,
        }

    def request(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if self.dry_run and method.upper() in {"POST", "PUT", "DELETE"}:
            print(f"[DRY RUN] {method} {path}")
            if payload:
                print(json.dumps(payload, indent=2)[:3000])
            return {"dry_run": True, "path": path, "payload": payload}

        data = None if payload is None else json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.base_url + path,
            data=data,
            headers=self._headers(),
            method=method.upper(),
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Shopify HTTP {e.code}: {body}") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"Shopify connection error: {e}") from e

    def test_connection(self) -> bool:
        if self.dry_run:
            print("[DRY RUN] Connection settings loaded.")
            print(f"Store: {self.store_domain}")
            return True
        data = self.request("GET", "/shop.json")
        print("Connected:", data.get("shop", {}).get("name", self.store_domain))
        return True

    def create_product(self, product_payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.request("POST", "/products.json", {"product": product_payload})

    def get_product(self, product_id: int) -> Dict[str, Any]:
        return self.request("GET", f"/products/{product_id}.json")

    def list_recent_products(self, limit: int = 10) -> Dict[str, Any]:
        return self.request("GET", f"/products.json?limit={limit}&order=created_at%20desc")
