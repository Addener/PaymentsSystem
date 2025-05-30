# PaymentsSystem
### Стек технологий:
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org)
[![MYSQL](https://img.shields.io/badge/-MySQL-464646?style=flat-square&logo=MYSQL)](https://www.mysql.org)
### Цель проекта:
Имитация webhook от банка, путем создания backend-сервиса, который:

- принимает входящие webhook-и от банка
- обрабатывает их
- корректно начисляет баланс организации по ИНН

### POST `/api/webhook/bank/`

Webhook принимает JSON следующего формата:

```json
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}

```
### Поведение

- Если операция уже была (`operation_id`) — ничего не делает, возвращает `200 OK`
Требуется защита от дублей, то есть если приходит тот же самый вебхук, мы не должны заново пополнять баланс
- Если новая:
  - создаёт `Payment`
  - начисляет сумму на баланс организации с `payer_inn`
  - логирует изменение баланса (в отдельную таблицу или просто `print` / `log`)

---

##№ GET `/api/organizations/<inn>/balance/`

Возвращает текущий баланс организации по ИНН:

```json
{
  "inn": "1234567890",
  "balance": 145000
}

```

### Автор работы

Алексей Ужва

VK: [@uzhvaaa](https://vk.com/uzhvaaa)
