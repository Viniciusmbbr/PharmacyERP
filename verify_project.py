#!/usr/bin/env python
"""Project verification script - Check if all components are properly configured"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def check_imports():
    """Check if all required modules can be imported"""
    print("\n🔍 Verificando imports...")

    modules = [
        ("fastapi", "FastAPI"),
        ("sqlalchemy", "SQLAlchemy"),
        ("pydantic", "Pydantic"),
        ("jose", "python-jose"),
        ("bcrypt", "bcrypt"),
        ("uvicorn", "uvicorn"),
    ]

    failed = []
    for module, display_name in modules:
        try:
            __import__(module)
            print(f"  ✅ {display_name}")
        except ImportError as e:
            print(f"  ❌ {display_name}: {e}")
            failed.append(display_name)

    return len(failed) == 0


def check_structure():
    """Check if required files and folders exist"""
    print("\n📁 Verificando estrutura de pastas...")

    required = [
        "API/main.py",
        "API/schemas.py",
        "API/exceptions.py",
        "API/middleware.py",
        "API/routes/auth_routes.py",
        "API/routes/medicamentos.py",
        "API/websocket/manager.py",
        "Application/services/auth_service.py",
        "Application/services/medicamento_service.py",
        "Domain/Base.py",
        "Domain/Usuario.py",
        "Domain/Venda.py",
        "Domain/Medicamento.py",
        "Infrastructure/database.py",
        "Infrastructure/seeds.py",
        "config.py",
        "Requirements.txt",
    ]

    failed = []
    for file_path in required:
        path = Path(file_path)
        if path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (não encontrado)")
            failed.append(file_path)

    return len(failed) == 0


def check_domain_models():
    """Check if domain models can be imported"""
    print("\n🏗️ Verificando modelos de domínio...")

    models = [
        ("Domain.Base", "Base"),
        ("Domain.Usuario", "Usuario"),
        ("Domain.Medicamento", "Medicamento"),
        ("Domain.Lote", "Lote"),
        ("Domain.Fornecedor", "Fornecedor"),
        ("Domain.Compra", "Compra"),
        ("Domain.Venda", "Venda"),
        ("Domain.Alerta", "Alerta"),
    ]

    failed = []
    for module_name, class_name in models:
        try:
            module = __import__(module_name, fromlist=[class_name])
            cls = getattr(module, class_name)
            print(f"  ✅ {class_name}")
        except (ImportError, AttributeError) as e:
            print(f"  ❌ {class_name}: {e}")
            failed.append(class_name)

    return len(failed) == 0


def check_services():
    """Check if service classes can be imported"""
    print("\n⚙️ Verificando serviços...")

    services = [
        ("Application.services.auth_service", "AuthService"),
        ("Application.services.medicamento_service", "MedicamentoService"),
        ("Application.services.lote_service", "LoteService"),
        ("Application.services.fornecedor_service", "FornecedorService"),
        ("Application.services.compra_service", "CompraService"),
        ("Application.services.venda_service", "VendaService"),
        ("Application.services.alerta_service", "AlertaService"),
        ("Application.services.relatorio_service", "RelatorioService"),
    ]

    failed = []
    for module_name, class_name in services:
        try:
            module = __import__(module_name, fromlist=[class_name])
            cls = getattr(module, class_name)
            print(f"  ✅ {class_name}")
        except (ImportError, AttributeError) as e:
            print(f"  ❌ {class_name}: {e}")
            failed.append(class_name)

    return len(failed) == 0


def check_configuration():
    """Check if configuration is properly set"""
    print("\n⚙️ Verificando configurações...")

    try:
        from config import (
            DATABASE_URL, JWT_SECRET_KEY, JWT_ALGORITHM,
            ACCESS_TOKEN_EXPIRE_MINUTES, CORS_ORIGINS, DEBUG
        )
        print(f"  ✅ DATABASE_URL: {DATABASE_URL[:50]}...")
        print(f"  ✅ JWT_ALGORITHM: {JWT_ALGORITHM}")
        print(f"  ✅ ACCESS_TOKEN_EXPIRE_MINUTES: {ACCESS_TOKEN_EXPIRE_MINUTES}")
        print(f"  ✅ DEBUG: {DEBUG}")
        print(f"  ✅ CORS_ORIGINS: {len(CORS_ORIGINS)} origins")
        return True
    except Exception as e:
        print(f"  ❌ Erro ao carregar configurações: {e}")
        return False


def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("🏥 PharmacyERP - Project Verification")
    print("="*60)

    results = {
        "Imports": check_imports(),
        "Estrutura": check_structure(),
        "Modelos de Domínio": check_domain_models(),
        "Serviços": check_services(),
        "Configuração": check_configuration(),
    }

    print("\n" + "="*60)
    print("📊 Resultado da Verificação")
    print("="*60)

    for check_name, passed in results.items():
        status = "✅ PASSOU" if passed else "❌ FALHOU"
        print(f"{check_name}: {status}")

    all_passed = all(results.values())

    print("\n" + "="*60)
    if all_passed:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("\n🚀 Próximos passos:")
        print("   1. python setup_database.py")
        print("   2. uvicorn API.main:app --reload")
        print("   3. Acessar http://localhost:8000/docs")
        print("="*60 + "\n")
        return 0
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        print("\n💡 Verificar:")
        print("   1. Dependências instaladas (pip install -r Requirements.txt)")
        print("   2. Estrutura de pastas correta")
        print("   3. Variáveis de ambiente (.env)")
        print("="*60 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
