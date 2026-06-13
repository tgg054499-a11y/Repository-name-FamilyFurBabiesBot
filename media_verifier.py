from typing import Dict, List


def verify_product_payload(product_payload: Dict) -> List[str]:
    problems = []
    if not product_payload.get("title"):
        problems.append("Missing title")
    if not product_payload.get("body_html"):
        problems.append("Missing description")
    variants = product_payload.get("variants", [])
    if not variants:
        problems.append("Missing variant/price")
    else:
        try:
            price = float(variants[0].get("price", 0))
            if price <= 0:
                problems.append("Price must be above 0")
        except Exception:
            problems.append("Invalid price")
    for img in product_payload.get("images", []):
        src = img.get("src", "")
        if src and not (src.startswith("http://") or src.startswith("https://")):
            problems.append(f"Bad image URL: {src}")
    return problems


def print_verification(title: str, problems: List[str]) -> bool:
    if problems:
        print(f"❌ {title}: NEEDS FIX")
        for p in problems:
            print("   -", p)
        return False
    print(f"✅ {title}: VERIFIED")
    return True
