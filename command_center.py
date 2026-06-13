from shopify_connector import ShopifyConnector
from product_creator import build_product, sample_products
from media_verifier import verify_product_payload, print_verification


def create_products(count: int):
    shop = ShopifyConnector()
    products = sample_products()[:count]
    created = 0
    blocked = 0

    print("========================================")
    print(" FAMILY FUR BABIES - NEW COMMAND CENTER ")
    print("========================================")
    shop.test_connection()
    print(f"Mode: {'DRY RUN SAFE TEST' if shop.dry_run else 'LIVE SHOPIFY CREATE'}")
    print(f"Products queued: {len(products)}")
    print("----------------------------------------")

    for i, item in enumerate(products, 1):
        payload = build_product(item)
        problems = verify_product_payload(payload)
        ok = print_verification(payload.get("title", f"Product {i}"), problems)
        if not ok:
            blocked += 1
            continue
        result = shop.create_product(payload)
        created += 1
        if result.get("product", {}).get("id"):
            print("   Shopify ID:", result["product"]["id"])
        print("----------------------------------------")

    print("DONE")
    print("Created/ready:", created)
    print("Blocked:", blocked)


def menu():
    print("\nChoose test:")
    print("1 = Test connection only")
    print("2 = Test 1 product")
    print("3 = Test 10 products")
    print("4 = List recent Shopify products")
    print("5 = Full store test placeholder")
    choice = input("Enter number: ").strip()

    if choice == "1":
        ShopifyConnector().test_connection()
    elif choice == "2":
        create_products(1)
    elif choice == "3":
        create_products(10)
    elif choice == "4":
        shop = ShopifyConnector()
        print(shop.list_recent_products(10))
    elif choice == "5":
        print("Full store test will run after 1-product and 10-product tests pass.")
    else:
        print("Bad choice. Run again and pick 1-5.")


if __name__ == "__main__":
    menu()
