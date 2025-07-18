#!/usr/bin/env python3
"""Infrastructure IA - Script de démarrage"""
import subprocess
import sys

def main():
    print("� Démarrage Infrastructure IA")
    try:
        subprocess.run(["docker", "compose", "up", "-d"], check=True)
        print("✅ Services démarrés!")
        print("�� n8n: http://localhost:5678")
        print("� Qdrant: http://localhost:6333") 
        print("� Ollama: http://localhost:11434")
        print("� Baserow: http://localhost:8080")
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
