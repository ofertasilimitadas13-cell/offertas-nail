import os
import time
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Memória para não repetir ofertas
ofertas_enviadas = set()

# Lista inicial de ofertas de unhas
OFERTAS_UNHAS = [
    {
        "id": "unha_001",
        "titulo": "💅 *KIT GEL UV UNHAS DE FIBRA COMPLETO*",
        "desc": "Kit profissional com cabine LED, géis e acessórios!",
        "link": "https://shopee.com.br"
    },
    {
        "id": "unha_002",
        "titulo": "✨ *LIXA ELÉTRICA PARA UNHAS E MANICURE*",
        "desc": "Ideal para acabamento, remoção de gel e polimento.",
        "link": "https://shopee.com.br"
    },
    {
        "id": "unha_003",
        "titulo": "🎨 *KIT ESMALTES EM GEL - CORES LINDAS*",
        "desc": "Alta durabilidade e brilho intenso para suas unhas.",
        "link": "https://shopee.com.br"
    }
]

def enviar_mensagem_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Erro ao enviar: {e}")

def postar_proxima_oferta():
    global ofertas_enviadas
    for oferta in OFERTAS_UNHAS:
        if oferta["id"] not in ofertas_enviadas:
            mensagem = (
                f"{oferta['titulo']}\n\n"
                f"📦 {oferta['desc']}\n\n"
                f"🛒 *Compre aqui:* {oferta['link']}"
            )
            enviar_mensagem_telegram(mensagem)
            ofertas_enviadas.add(oferta["id"])
            print(f"Postado: {oferta['id']}")
            return
            
    print("Todas as ofertas da lista já foram postadas!")

if __name__ == "__main__":
    print("Bot de Unhas rodando...")
    while True:
        postar_proxima_oferta()
        # Posta a cada 1 hora (3600 segundos)
        time.sleep(3600)
