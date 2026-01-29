import os

IP_SERVIDOR = "192.168.0.80"
USUARIO = "sre"
CONTAINER = "meu-servidor"

def checar_e_recuperar():
    print(f"--- Verificando Saúde do Container: {CONTAINER} ---")
    
    # Comando para verificar se o container está 'running'
    cmd_check = f"ssh {USUARIO}@{IP_SERVIDOR} \"sudo docker inspect -f '{{{{.State.Running}}}}' {CONTAINER}\" 2>/dev/null"
    
    status = os.popen(cmd_check).read().strip()
    
    if status == "true":
        print(f"[OK] {CONTAINER} está operando normalmente. ✅")
    else:
        print(f"[ALERTA] {CONTAINER} está CAÍDO! Tentando recuperar... 🛠️")
        # Comando para tentar iniciar o container novamente
        os.system(f"ssh {USUARIO}@{IP_SERVIDOR} 'sudo docker start {CONTAINER}'")
        print(f"[INFO] Comando de reinicialização enviado.")

if __name__ == "__main__":
    checar_e_recuperar()