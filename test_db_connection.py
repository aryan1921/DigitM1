import os
import sys
import django

# Add the mysite directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mysite'))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.db import connection

def test_database_connection():
    """Test if the database is connected and accessible."""
    try:
        # Try to execute a simple query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result and result[0] == 1:
                print("✅ Database is connected successfully!")
                print(f"Database engine: {connection.settings_dict['ENGINE']}")
                print(f"Database name: {connection.settings_dict['NAME']}")
                return True
            else:
                print("❌ Database connection test failed - unexpected result")
                return False
    except Exception as e:
        print(f"❌ Database connection failed with error: {e}")
        return False

if __name__ == "__main__":
    test_database_connection()
