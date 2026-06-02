"""Quick test to verify relationships and schema"""
from Domain.Base import Base
from Domain.Usuario import Usuario
from Domain.Venda import Venda, VendaItem
from Infrastructure.database import engine

# Create tables
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

# Test imports
print(f"Usuario model: {Usuario}")
print(f"Venda model: {Venda}")
print(f"VendaItem model: {VendaItem}")
print("\nAll models loaded correctly!")
