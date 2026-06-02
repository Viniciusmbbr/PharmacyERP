import os
import re

routes_dir = r"C:\Users\Vinicius\Desktop\ERPPharmacy\API\routes"

for filename in os.listdir(routes_dir):
    if filename.endswith(".py") and filename != "websocket_routes.py":
        filepath = os.path.join(routes_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove response_model=PaginatedResponse[...]
        content = re.sub(
            r'@router\.get\("", response_model=PaginatedResponse\[.*?\]\)',
            '@router.get("")',
            content
        )
        
        # Also fix other routers
        content = re.sub(
            r', response_model=PaginatedResponse\[.*?\]',
            '',
            content
        )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}")
        else:
            print(f"⏭️  {filename} (no changes needed)")

print("\n✅ All files fixed!")
