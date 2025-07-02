#!/usr/bin/env python3
"""
Script de teste para verificar a configuração do Claude
=======================================================
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

def testar_configuracao():
    """Testa se a configuração do Claude está correta"""
    print("🔧 Testando configuração do Claude...")
    
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Verificar se a chave API está configurada
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY não encontrada no arquivo .env")
        print("📝 Configure sua chave API no arquivo .env")
        return False
    
    if api_key == "sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxx":
        print("❌ Chave API ainda é o exemplo. Configure sua chave real no arquivo .env")
        return False
    
    try:
        # Tentar inicializar o modelo
        llm = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            anthropic_api_key=api_key,
            temperature=0.3,
            max_tokens=100
        )
        
        print("✅ Modelo Claude configurado com sucesso")
        print("🔑 Chave API válida")
        print("🤖 Modelo: claude-3-5-sonnet-20241022")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao configurar Claude: {e}")
        return False

if __name__ == "__main__":
    if testar_configuracao():
        print("\n🎉 Configuração OK! O script principal está pronto para usar.")
    else:
        print("\n⚠️ Configure o arquivo .env antes de executar o script principal.")
