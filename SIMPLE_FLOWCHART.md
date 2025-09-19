# 🏥 WhatsApp Medical AI Chatbot - Simple Flowchart

## 🔄 **Main System Flow**

```
User Message → Twilio → Flask API → AI Processing → Response + Disclaimer → WhatsApp
     │             │         │           │              │                    │
  "I have       Webhook   Process    LLM/ML Model   Medical Advice      User receives
   fever"       Trigger    Text       Analysis       + Warning           response
```

## 🤖 **AI Decision Flow**

```
                Medical Query
                      │
                      ▼
              ┌───────────────┐
              │  LLM Available? │
              └───────────────┘
                  │       │
                YES │     │ NO
                    ▼     ▼
            ┌─────────┐ ┌─────────┐
            │   GPT   │ │RandomFor│
            │Response │ │est Model│
            └─────────┘ └─────────┘
                  │       │
                  └───┬───┘
                      ▼
              Medical Advice + Disclaimer
```

## 🚀 **Deployment Flow**

```
Local Dev → Test → Deploy → Configure → Live Bot
    │        │       │         │          │
 Python   API     Heroku/   Twilio     WhatsApp
 Flask    Test    Railway   Webhook    Messages
```

## 📊 **Technologies Used**

```
Frontend: WhatsApp (User Interface)
    │
Backend: Python + Flask (API Server)
    │
AI: OpenAI GPT + RandomForest ML
    │
Integration: Twilio (WhatsApp API)
    │
Deployment: Heroku/Railway (Cloud)
```