import os
import json
import urllib.request
from datetime import datetime, date

# 1. Configurações base
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
ANCHOR_DATE = date(2026, 5, 5) # 05/05/2026 cai numa terça, e é a vez do Igor
PEOPLE = ["Igor", "Hygor", "Felipe", "Pollys", "Victor", "Paulão"]

def main():
    if not WEBHOOK_URL:
        print("Erro: A variável de ambiente SLACK_WEBHOOK_URL não está configurada.")
        return

    # 2. Descobrir quantas semanas se passaram desde a data âncora
    today = date.today()
    delta = today - ANCHOR_DATE
    weeks_passed = delta.days // 7

    # 3. Descobrir o índice da pessoa (usando módulo para o ciclo infinito)
    # Se weeks_passed for 0, index é 0 (Igor)
    # Se weeks_passed for 5, index é 5 (Paulão)
    # Se weeks_passed for 6, index é 0 (Igor de novo)
    person_index = weeks_passed % len(PEOPLE)
    payer = PEOPLE[person_index]

    # 4. Enviar mensagem para o Slack
    message = f"🥤 *Chegou a Terça da Coca!* 🥤\n\nHoje é o dia oficial! Quem vai pagar a Coca de hoje é: *{payer}*! :tada: :money_with_wings:\n\nJá vai preparando o bolso e o Pix!"

    payload = {
        "text": message
    }

    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(f"Mensagem enviada com sucesso! Pagador: {payer}")
            else:
                print(f"Falha ao enviar mensagem. Status code: {response.status}")
    except Exception as e:
        print(f"Erro ao enviar webhook: {e}")

if __name__ == "__main__":
    main()
