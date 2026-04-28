# Automação da Coca-Cola de Terça

**Objetivo:** Automatizar o aviso semanal (toda terça-feira) sobre de quem é a vez de pagar a Coca-Cola da equipe.

## Entradas (Inputs)
- A lista de pessoas no ciclo: `["Igor", "Hygor", "Felipe", "Pollys", "Victor", "Paulão"]`
- A data âncora do primeiro do ciclo (Igor): `2026-05-05`.
- `SLACK_WEBHOOK_URL` contida nas variáveis de ambiente (.env ou Github Secrets).

## Regras de Negócio (Lógica)
1. O ciclo de pessoas é fixo e contínuo.
2. A cada semana, avança-se uma pessoa. Após o "Paulão", a vez volta para o "Igor".
3. Para descobrir de quem é a vez sem guardar um banco de dados, o script calcula a diferença de semanas entre a data atual e a data âncora (05/05/2026).
4. O script faz o resto da divisão (`%`) pelo total de pessoas na lista para achar o índice exato, garantindo o ciclo infinito automático.
