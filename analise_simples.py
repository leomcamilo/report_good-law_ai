#!/usr/bin/env python3
"""
Script Simples - Análise Lei do Bem com DeepSeek
===============================================

Script simplificado para análise rápida usando LangChain + DeepSeek.
"""

import os
import sys
from dotenv import load_dotenv
from analise_langchain_deepseek import AnalisadorLeiDoBemLangChain

# Carregar variáveis de ambiente
load_dotenv()

def verificar_configuracao():
    """Verifica se a configuração está correta."""
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key or api_key == 'your_deepseek_api_key_here':
        print("❌ ERRO: Chave da API do DeepSeek não configurada!")
        print("\n🔧 Para configurar:")
        print("1. Obtenha sua chave em: https://platform.deepseek.com/")
        print("2. Edite o arquivo .env")
        print("3. Substitua 'your_deepseek_api_key_here' pela sua chave")
        print("\nExemplo no .env:")
        print("DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx")
        return False
    return True

def analise_rapida():
    """Executa uma análise rápida com menos dados."""
    if not verificar_configuracao():
        return
    
    print("🚀 Executando análise rápida...")
    
    analisador = AnalisadorLeiDoBemLangChain()
    analise = analisador.executar_analise_completa(max_rows=30, salvar=True)
    
    if analise:
        print("\n✅ Análise concluída!")
        print("📄 Resultado salvo em arquivo .md")
    else:
        print("❌ Falha na análise")

def analise_completa():
    """Executa uma análise completa com mais dados."""
    if not verificar_configuracao():
        return
    
    print("🚀 Executando análise completa (pode demorar mais)...")
    
    analisador = AnalisadorLeiDoBemLangChain()
    analise = analisador.executar_analise_completa(max_rows=100, salvar=True)
    
    if analise:
        print("\n✅ Análise completa concluída!")
        print("📄 Resultado salvo em arquivo .md")
    else:
        print("❌ Falha na análise")

def analise_customizada():
    """Permite análise com parâmetros customizados."""
    if not verificar_configuracao():
        return
    
    print("🔧 Análise Customizada")
    print("======================")
    
    try:
        max_rows = int(input("Número de projetos para analisar (recomendado 30-100): ") or "50")
        salvar_arquivo = input("Salvar em arquivo? (s/N): ").lower().startswith('s')
        
        print(f"\n🚀 Executando análise de {max_rows} projetos...")
        
        analisador = AnalisadorLeiDoBemLangChain()
        analise = analisador.executar_analise_completa(max_rows=max_rows, salvar=salvar_arquivo)
        
        if analise:
            print(f"\n{'='*60}")
            print("📋 RESULTADO DA ANÁLISE")
            print(f"{'='*60}")
            print(analise[:2000] + "..." if len(analise) > 2000 else analise)
            print(f"\n{'='*60}")
            
            if salvar_arquivo:
                print("✅ Análise salva em arquivo!")
        else:
            print("❌ Falha na análise")
            
    except ValueError:
        print("❌ Número inválido!")
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário")

def main():
    """Menu principal."""
    print("🤖 Análise Lei do Bem com DeepSeek")
    print("===================================")
    print("1. Análise Rápida (30 projetos)")
    print("2. Análise Completa (100 projetos)")
    print("3. Análise Customizada")
    print("4. Verificar Configuração")
    print("0. Sair")
    
    while True:
        try:
            opcao = input("\nEscolha uma opção (0-4): ").strip()
            
            if opcao == "0":
                print("👋 Até logo!")
                break
            elif opcao == "1":
                analise_rapida()
            elif opcao == "2":
                analise_completa()
            elif opcao == "3":
                analise_customizada()
            elif opcao == "4":
                if verificar_configuracao():
                    print("✅ Configuração OK!")
                else:
                    print("❌ Configuração incompleta")
            else:
                print("❌ Opção inválida! Escolha 0-4.")
                
        except KeyboardInterrupt:
            print("\n👋 Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
