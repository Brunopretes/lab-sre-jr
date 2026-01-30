import os
import urllib.request
import urllib.parse
import ssl

# ================= CONFIGURAÇÕES =================
IP_SERVIDOR = "000.000.0.00"
USUARIO = "sre"
CONTAINER = "meu-servidor"

# COLOQUE SEUS DADOS AQUI
TELEGRAM_TOKEN = "SEU-TOKEN-AQUI"
TELEGRAM_CHAT_ID = "SEU-CHAT-ID-AQUI"
# =================================================

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    # Organiza os dados para envio via POST (mais robusto)
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mensagem,
        'parse_mode': 'Markdown' # Permite usar negrito/emojis melhor
    }
    
    data = urllib.parse.urlencode(params).encode('utf-8')
    
    print(f"[DEBUG] Tentando notificar Telegram...")
    
    try:
        # Criamos um contexto SSL que ignora erros de certificado se houver (comum em redes locais)
        context = ssl._create_unverified_context()
        
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10, context=context) as response:
            if response.getcode() == 200:
                print("[INFO] Alerta enviado ao Telegram! 📱")
    except Exception as e:
        print(f"[ERRO] Falha crítica no Telegram: {e}")

def checar_e_recuperar():
    print(f"\n--- 🔎 Verificando Saúde: {CONTAINER} ---")
    
    # Comando SSH para checar status
    cmd_check = f"ssh {USUARIO}@{IP_SERVIDOR} \"sudo docker inspect -f '{{{{.State.Running}}}}' {CONTAINER}\" 2>/dev/null"
    
    try:
        status = os.popen(cmd_check).read().strip()
        
        if status == "true":
            print(f"[OK] {CONTAINER} operando normalmente. ✅")
        else:
            print(f"[ALERTA] {CONTAINER} está FORA DO AR!")
            
            # 1. Envia Alerta de Queda
            enviar_alerta(f"🚨 *ALERTA SRE*\nO container `{CONTAINER}` no servidor `{IP_SERVIDOR}` caiu!")
            
            # 2. Tenta Recuperação
            print(f"[INFO] Iniciando tentativa de recuperação...")
            os.system(f"ssh {USUARIO}@{IP_SERVIDOR} 'sudo docker start {CONTAINER}'")
            
            # 3. Verifica se subiu e avisa
            status_pos = os.popen(cmd_check).read().strip()
            if status_pos == "true":
                enviar_alerta(f"✅ *RECUPERADO*\nO container `{CONTAINER}` já está online novamente.")
                print("[INFO] Recuperação concluída com sucesso.")
            else:
                enviar_alerta(f"❌ *FALHA NA RECUPERAÇÃO*\nO container `{CONTAINER}` não subiu automaticamente!")
                
    except Exception as e:
        print(f"[ERRO] Falha na comunicação SSH: {e}")

if __name__ == "__main__":
    checar_e_recuperar()