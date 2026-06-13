from typing import Dict, List

try:
    import config
except Exception:
    config = None


def money(value: float) -> str:
    return f"{value:.2f}"


def build_product(item: Dict) -> Dict:
    title = item["title"].strip()
    price = float(item.get("price", 19.99))
    category = item.get("category", "Pet Supplies")
    tags: List[str] = []
    if config:
        tags.extend(getattr(config, "BASE_TAGS", []))
    tags.extend(item.get("tags", []))
    tags.append(category)

    body_html = f"""
    <h2>{title}</h2>
    <p>{item.get('description', 'Helpful pet product selected for Family Fur Babies customers.')}</p>
    <ul>
      <li>Designed for pet comfort, care, or convenience</li>
      <li>Great for pet parents who want simple problem-solving products</li>
      <li>Ships from selected supplier after order processing</li>
    </ul>
    """.strip()

    images = []
    for url in item.get("image_urls", []):
        if url:
            images.append({"src": url})

    return {
        "title": title,
        "body_html": body_html,
        "vendor": getattr(config, "DEFAULT_VENDOR", "Family Fur Babies") if config else "Family Fur Babies",
        "product_type": item.get("product_type", getattr(config, "DEFAULT_PRODUCT_TYPE", "Pet Supplies") if config else "Pet Supplies"),
        "status": item.get("status", getattr(config, "DEFAULT_STATUS", "draft") if config else "draft"),
        "tags": ", ".join(sorted(set(tags))),
        "variants": [{
            "option1": "Default Title",
            "price": money(price),
            "inventory_management": None,
            "requires_shipping": True,
        }],
        "images": images,
    }


def sample_products() -> List[Dict]:
    return [
        {
            "title": "No-Spill Pet Travel Water Bowl",
            "category": "Travel & Outdoor",
            "price": 24.99,
            "description": "A simple travel bowl that helps reduce spills during car rides, walks, and outdoor trips.",
            "tags": ["Dogs", "Cats", "Travel", "Problem Solver"],
            "image_urls": [],
        },
        {
            "title": "Aquarium Gravel Cleaning Siphon Kit",
            "category": "Fish & Aquarium",
            "price": 18.99,
            "description": "Helps fish owners clean aquarium gravel and remove dirty water with less mess.",
            "tags": ["Fish", "Aquarium", "Cleaning", "Problem Solver"],
            "image_urls": [],
        },
        {
            "title": "Pet Hair Laundry Catcher Balls",
            "category": "Home Cleaning",
            "price": 14.99,
            "description": "Reusable laundry balls made to help collect loose pet hair from clothes and blankets.",
            "tags": ["Dogs", "Cats", "Cleaning", "Bundle Ready"],
            "image_urls": [],
        },
        {
            "title": "Slow Feeder Puzzle Bowl",
            "category": "Feeding",
            "price": 21.99,
            "description": "A feeding bowl that slows fast eating and gives pets a more engaging meal routine.",
            "tags": ["Dogs", "Feeding", "Problem Solver"],
            "image_urls": [],
        },
        {
            "title": "Cat Window Perch Hammock",
            "category": "Cats",
            "price": 29.99,
            "description": "A cozy window perch for cats who love watching outside and resting in the sun.",
            "tags": ["Cats", "Comfort", "Home"],
            "image_urls": [],
        },
        {
            "title": "Dog Paw Cleaner Cup",
            "category": "Grooming",
            "price": 16.99,
            "description": "Portable paw cleaner cup for muddy walks and quick cleanup before pets come inside.",
            "tags": ["Dogs", "Grooming", "Cleaning"],
            "image_urls": [],
        },
        {
            "title": "Bird Cage Seed Catcher Skirt",
            "category": "Birds",
            "price": 13.99,
            "description": "Mesh seed catcher that helps reduce scattered bird seed around the cage.",
            "tags": ["Birds", "Cleaning", "Problem Solver"],
            "image_urls": [],
        },
        {
            "title": "Reptile Humidity Hide Cave",
            "category": "Reptiles",
            "price": 22.99,
            "description": "Hide cave made to support reptile comfort, shedding, and humidity needs.",
            "tags": ["Reptiles", "Habitat", "Comfort"],
            "image_urls": [],
        },
        {
            "title": "Rabbit Hay Feeder Bag",
            "category": "Small Animals",
            "price": 15.99,
            "description": "Hanging hay feeder bag that helps keep hay cleaner and reduces cage mess.",
            "tags": ["Rabbits", "Small Animals", "Feeding"],
            "image_urls": [],
        },
        {
            "title": "Pet First Aid Travel Pouch",
            "category": "Safety",
            "price": 19.99,
            "description": "Compact organizer pouch for carrying basic pet care and travel safety supplies.",
            "tags": ["Safety", "Travel", "Dogs", "Cats"],
            "image_urls": [],
        },
    ]
