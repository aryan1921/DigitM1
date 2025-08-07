#!/usr/bin/env python3
import os
import sys

# Change to the mysite directory
os.chdir('mysite')

# Add the mysite directory to the Python path
sys.path.insert(0, os.getcwd())

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

try:
    import django
    django.setup()
    
    from django.db import connection
    
    # Test database connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
    if result and result[0] == 1:
        print("✅ Database Connection Status: CONNECTED")
        print(f"   Database Engine: {connection.settings_dict['ENGINE']}")
        print(f"   Database Name: {connection.settings_dict['NAME']}")
        print(f"   Database Size: {os.path.getsize('db.sqlite3')} bytes")
        
        # Test if we can access models
        from myapp.models import Product
        product_count = Product.objects.count()
        print(f"   Products in database: {product_count}")
        
    else:
        print("❌ Database Connection Status: FAILED")
        
except ImportError as e:
    print(f"❌ Django not found: {e}")
    print("   Please ensure Django is installed and virtual environment is activated")
    
except Exception as e:
    print(f"❌ Database connection error: {e}")

print("\n📊 Database Configuration Summary:")
print("   Engine: SQLite3")
print("   File: db.sqlite3")
print("   Location: mysite/db.sqlite3")
