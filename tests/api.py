from typing import Optional, Dict
import httpx


def test_user_api(name: str, q: Optional[str] = None) -> Dict[str, str]:
    r = httpx.get(f'http://127.0.0.1:8000/api/user?name={name}')
    return r.json()

test_user_api("santo")

