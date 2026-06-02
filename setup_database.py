#!/usr/bin/env python
"""Database setup script - Initialize and populate the database"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from Infrastructure.database import init_db, SessionLocal
from Infrastructure.seeds import seed_database


def main():
    """Main setup function"""
    print("\n" + "="*60)
    print("PharmacyERP - Database Setup")
    print("="*60 + "\n")

    try:
        # Initialize database
        print("1. Initializing database tables...")
        init_db()

        # Seed initial data
        print("\n2. Loading initial data (seeds)...")
        db = SessionLocal()
        seed_database(db)
        db.close()

        print("\n" + "="*60)
        print("Database setup completed successfully!")
        print("="*60)
        print("\nDefault Credentials:")
        print("   Admin: admin@pharmacy.com / Admin123!")
        print("   Farmaceutico: farmaceutico@pharmacy.com / Farm123!")
        print("   Caixa: caixa@pharmacy.com / Caixa123!")
        print("   Estoquista: estoquista@pharmacy.com / Stock123!")
        print("\nStart the API with:")
        print("   uvicorn API.main:app --reload")
        print("\nAPI Documentation:")
        print("   http://localhost:8000/docs")
        print("="*60 + "\n")

    except Exception as e:
        print(f"\nError during setup: {e}")
        print("\nTroubleshooting:")
        print("   - Check DATABASE_URL in config.py")
        print("   - Ensure PostgreSQL is running")
        print("   - Check .env file for correct credentials")
        sys.exit(1)


if __name__ == "__main__":
    main()
