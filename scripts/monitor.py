import os

# CONFIGURAÇÕES
IP_SERVIDOR = "192.168.0.80"
USUARIO = "sre" # coloque o seu usuario do ubuntu aqui

def verificar_status():
    print(f"--- Verificando Servidor: {IP_SERVIDOR} ---")
    status = os.system(f"ping -c 1 {IP_SERVIDOR} > /dev/null 2>&1")
    
    if status == 0:
        print("[STATUS] Online! ✅")
        # Comando SSH para rodar o comando 'uptime' remotamente
        print("[INFO] Tempo de atividade no servidor:")
        os.system(f"ssh {USUARIO}@{IP_SERVIDOR} 'uptime -p'")
    else:
        print("[STATUS] Offline! ❌")

if __name__ == "__main__":
    verificar_status()
