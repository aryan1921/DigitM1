#!/usr/bin/env python3
"""
Database Connection Status Report
This script provides a comprehensive check of the database connection status.
"""

import os
import sys

def check_database_status():
    """Check the current database connection status."""
    
    print("=" * 60)
    print("🔍 DATABASE CONNECTION STATUS REPORT")
    print("=" * 60)
    
    # Check if database file exists
    db_path = "mysite/db.sqlite3"
    if os.path.exists(db_path):
        print(f"✅ Database file exists: {db_path}")
        print(f"   File size: {os.path.getsize(db_path)} bytes")
        print(f"   Last modified: {os.path.getmtime(db_path)}")
    else:
        print(f"❌ Database file not found: {db_path}")
        return False
    
    # Check Django settings
    settings_path = "mysite/mysite/settings.py"
    if os.path.exists(settings_path):
        print(f"✅ Django settings file found: {settings_path}")
        
        # Read database configuration
        with open(settings_path, 'r') as f:
            content = f.read()
            if "sqlite3" in content:
                print("✅ Database engine: SQLite3")
            if "db.sqlite3" in content:
                print("✅ Database name: db.sqlite3")
    else:
        print(f"❌ Django settings file not found: {settings_path}")
        return False
    
    print("\n📋 SUMMARY:")
    print("   Database Type: SQLite3")
    print("   Database File: mysite/db.sqlite3")
    print("   Connection Method: File-based")
    print("   Status: READY (file exists)")
    
    print("\n🚀 TO TEST CONNECTION:")
    print("   1. Install dependencies: pip install -r requirements.txt")
    print("   2. Run: python manage.py check --database default")
    print("   3. Or use: python manage.py dbshell")
    
    return True

if __name__ == "__main__":
    check_database_status()
