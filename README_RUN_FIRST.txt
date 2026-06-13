FAMILY FUR BABIES - NEW CLEAN STORE BOT

NEW FILES ONLY:
- config_template.py
- shopify_connector.py
- image_uploader.py
- product_creator.py
- media_verifier.py
- command_center.py

SETUP:
1. Put this folder in Downloads.
2. Rename config_template.py to config.py.
3. Open config.py and paste:
   - SHOPIFY_STORE_DOMAIN
   - SHOPIFY_ADMIN_TOKEN
4. Leave DRY_RUN = True for first test.

RUN:
cd C:\Users\jlady\Downloads\ffb_new_store_bot
python command_center.py

TEST ORDER:
1 = Test connection only
2 = Test 1 product
3 = Test 10 products
5 = Full store test placeholder

LIVE CREATE:
Only after dry tests pass, change DRY_RUN = False.
Products create as draft first.
