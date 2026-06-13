from typing import Dict, List


def clean_image_urls(urls: List[str]) -> List[str]:
    cleaned = []
    for url in urls:
        url = str(url).strip()
        if url.startswith("http://") or url.startswith("https://"):
            cleaned.append(url)
    return cleaned


def attach_images_to_product_payload(product_payload: Dict, image_urls: List[str]) -> Dict:
    product_payload = dict(product_payload)
    product_payload["images"] = [{"src": url} for url in clean_image_urls(image_urls)]
    return product_payload
