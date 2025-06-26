#!/usr/bin/env python3
"""
Script de Teste - Verificação do Sistema
=======================================

Testa se todos os componentes estão funcionando corretamente.
"""

import os
import sys
from dotenv import load_dotenv

def test_imports():
    """Testa se todas as bibliotecas necessárias estão instaladas."""
    print("🔍 Testando imports...")
    
    try:
        import pandas as pd
        print("  ✅ pandas")
    except ImportError:
        print("  ❌ pandas - Execute: pip install pandas")
        return False
    
    try:
        import psycopg2
        print("  ✅ psycopg2")
    except ImportError:
        print("  ❌ psycopg2 - Execute: pip install psycopg2-binary")
        return False
    
    try:
        from sqlalchemy import create_engine
        print("  ✅ sqlalchemy")
    except ImportError:
        print("  ❌ sqlalchemy - Execute: pip install sqlalchemy")
        return False
    
    try:
        from langchain_openai import ChatOpenAI
        print("  ✅ langchain")
    except ImportError:
        print("  ❌ langchain - Execute: pip install langchain langchain-openai")
        return False
    
    try:
        from dotenv import load_dotenv
        print("  ✅ python-dotenv")
    except ImportError:
        print("  ❌ python-dotenv - Execute: pip install python-dotenv")
        return False
    
    return True

def test_env_file():
    """Testa se o arquivo .env existe e está configurado."""
    print("\n🔍 Testando arquivo .env...")
    
    if not os.path.exists('.env'):
        print("  ❌ Arquivo .env não encontrado")
        print("     Execute: cp .env.example .env")
        return False
    
    load_dotenv()
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("  ❌ DEEPSEEK_API_KEY não configurada")
        return False
    
    if api_key == 'your_deepseek_api_key_here' or api_key.startswith('sk-xxxxxxx'):
        print("  ❌ DEEPSEEK_API_KEY ainda com valor padrão")
        print("     Configure sua chave real do DeepSeek")
        return False
    
    print("  ✅ DEEPSEEK_API_KEY configurada")
    return True

def test_database_connection():
    """Testa conexão com o banco PostgreSQL."""
    print("\n🔍 Testando conexão com banco...")
    
    try:
        from analise_projetos import AnalisadorProjetosLeiDoBem
        
        analisador = AnalisadorProjetosLeiDoBem()
        if analisador.conectar_banco():
            print("  ✅ Conexão com PostgreSQL estabelecida")
            return True
        else:
            print("  ❌ Falha na conexão com PostgreSQL")
            return False
    except Exception as e:
        print(f"  ❌ Erro na conexão: {e}")
        return False

def test_langchain():
    """Testa se o LangChain está funcionando."""
    print("\n🔍 Testando LangChain...")
    
    try:
        from analise_langchain_deepseek import AnalisadorLeiDoBemLangChain
        
        analisador = AnalisadorLeiDoBemLangChain()
        if analisador.llm:
            print("  ✅ LangChain configurado com DeepSeek")
            return True
        else:
            print("  ❌ Falha na configuração do LangChain")
            return False
    except Exception as e:
        print(f"  ❌ Erro no LangChain: {e}")
        return False

def test_prompt_template():
    """Testa se o template de prompt foi carregado."""
    print("\n🔍 Testando template de prompt...")
    
    if not os.path.exists('prompt.md'):
        print("  ❌ Arquivo prompt.md não encontrado")
        return False
    
    try:
        with open('prompt.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) > 100:
            print("  ✅ Template de prompt carregado")
            return True
        else:
            print("  ❌ Template de prompt muito pequeno")
            return False
    except Exception as e:
        print(f"  ❌ Erro ao ler prompt.md: {e}")
        return False

def main():
    """Executa todos os testes."""
    print("🧪 TESTE DO SISTEMA - ANÁLISE LEI DO BEM")
    print("="*50)
    
    tests = [
        ("Imports das bibliotecas", test_imports),
        ("Arquivo .env", test_env_file),
        ("Template de prompt", test_prompt_template),
        ("Conexão com banco", test_database_connection),
        ("Configuração LangChain", test_langchain),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"  ❌ Erro inesperado: {e}")
            results.append((name, False))
    
    # Resumo
    print("\n" + "="*50)
    print("📋 RESUMO DOS TESTES")
    print("="*50)
    
    passed = 0
    for name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status} - {name}")
        if result:
            passed += 1
    
    print(f"\n📊 Resultado: {passed}/{len(results)} testes passaram")
    
    if passed == len(results):
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        print("O sistema está pronto para uso.")
        print("\nPróximos passos:")
        print("• Execute: python analise_simples.py")
        print("• Ou: python analise_langchain_deepseek.py")
    else:
        print("\n⚠️  ALGUNS TESTES FALHARAM!")
        print("Corrija os problemas antes de continuar.")
        print("\nPara instalar dependências:")
        print("• pip install -r requirements.txt")
        print("\nPara configurar .env:")
        print("• cp .env.example .env")
        print("• Edite .env com sua chave do DeepSeek")

if __name__ == "__main__":
    main()
