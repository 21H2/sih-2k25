# 🏥 WhatsApp Medical AI Chatbot - ASCII Flowcharts

## 🔄 **Main System Flow**

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                 WHATSAPP MEDICAL AI CHATBOT             │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                    USER SENDS MESSAGE                   │
                    │                  "I have fever and headache"           │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                     TWILIO RECEIVES                     │
                    │                   WhatsApp Message                      │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   WEBHOOK TRIGGERED                     │
                    │              POST /webhook (Flask API)                  │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   MESSAGE PROCESSING                    │
                    │              Extract text, clean, validate              │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │         MESSAGE TYPE?           │
                              └─────────────────────────────────┘
                                      │         │         │
                        ┌─────────────┘         │         └─────────────┐
                        ▼                       ▼                       ▼
            ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
            │    GREETING         │  │   MEDICAL QUERY     │  │     GOODBYE         │
            │   "hi", "hello"     │  │ "fever", "pain"     │  │  "bye", "thanks"    │
            └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                        │                       │                       │
                        ▼                       ▼                       ▼
            ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
            │   WELCOME MESSAGE   │  │    AI PROCESSING    │  │   GOODBYE MESSAGE   │
            │  "Welcome to..."    │  │   (See AI Flow)     │  │  "Take care..."     │
            └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                        │                       │                       │
                        └───────────┐           │           ┌───────────┘
                                    ▼           ▼           ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                  ADD MEDICAL DISCLAIMER                 │
                    │        "⚠️ This is AI-generated advice..."             │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   SEND VIA TWILIO                      │
                    │              twilio_client.messages.create()            │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                 USER RECEIVES RESPONSE                  │
                    │                    on WhatsApp                         │
                    └─────────────────────────────────────────────────────────┘
```

## 🤖 **AI Processing Flow (Hybrid System)**

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                   MEDICAL QUERY INPUT                   │
                    │              "I have chest pain during exercise"       │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   TEXT PREPROCESSING                    │
                    │           • Convert to lowercase                        │
                    │           • Remove special characters                   │
                    │           • Clean medical terminology                   │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │         USE_LLM = true?         │
                              └─────────────────────────────────┘
                                      │                   │
                                    YES │                 │ NO
                                        ▼                 ▼
                    ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
                    │         LLM AVAILABLE?          │   │      TRADITIONAL ML PATH        │
                    │    (OpenAI/Claude API Key)      │   │     (RandomForest Model)        │
                    └─────────────────────────────────┘   └─────────────────────────────────┘
                              │                   │                       │
                            YES │                 │ NO                    ▼
                                ▼                 ▼               ┌─────────────────┐
                    ┌─────────────────────┐   ┌─────────────────────┐   │   TF-IDF VECTOR │
                    │    LLM PROCESSING   │   │   FALLBACK TO ML    │   │   TRANSFORMATION │
                    │                     │   │                     │   └─────────────────┘
                    │  ┌───────────────┐  │   │  ┌───────────────┐  │           │
                    │  │ OpenAI GPT    │  │   │  │ RandomForest  │  │           ▼
                    │  │ - Medical     │  │   │  │ - Pattern     │  │   ┌─────────────────┐
                    │  │   Context     │  │   │  │   Matching    │  │   │  RANDOMFOREST   │
                    │  │ - Dynamic     │  │   │  │ - Pre-trained │  │   │   PREDICTION    │
                    │  │   Response    │  │   │  │   Responses   │  │   │                 │
                    │  └───────────────┘  │   │  └───────────────┘  │   │ • Fever advice  │
                    └─────────────────────┘   └─────────────────────┘   │ • Pain guidance │
                              │                       │                 │ • General tips  │
                              ▼                       ▼                 └─────────────────┘
                    ┌─────────────────────┐   ┌─────────────────────┐           │
                    │   LLM RESPONSE      │   │    ML RESPONSE      │           │
                    │                     │   │                     │           │
                    │ "Based on your      │   │ "Most chest pain    │           │
                    │  symptoms of chest  │   │  during exercise     │           │
                    │  pain during        │   │  requires medical    │           │
                    │  exercise, this     │   │  evaluation..."      │           │
                    │  could indicate..." │   │                     │           │
                    └─────────────────────┘   └─────────────────────┘           │
                              │                       │                         │
                              └───────────┐           │           ┌─────────────┘
                                          ▼           ▼           ▼
                              ┌─────────────────────────────────────────────────────────┐
                              │                 SUCCESS CHECK                           │
                              │            Response generated successfully?             │
                              └─────────────────────────────────────────────────────────┘
                                          │                           │
                                        YES │                         │ NO/ERROR
                                            ▼                         ▼
                              ┌─────────────────────────────┐   ┌─────────────────────────────┐
                              │      RETURN RESPONSE        │   │      ERROR RESPONSE         │
                              │   + Medical Disclaimer      │   │  "Sorry, please try again"  │
                              └─────────────────────────────┘   └─────────────────────────────┘
```

## 🚀 **Deployment Flow**

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                  DEVELOPMENT PHASE                      │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   LOCAL DEVELOPMENT                     │
                    │                                                         │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                    │  │   Python    │  │    Flask    │  │   ngrok     │     │
                    │  │ Environment │  │   Server    │  │  Tunnel     │     │
                    │  │   Setup     │  │  localhost  │  │  Public     │     │
                    │  │             │  │    :5000    │  │    URL      │     │
                    │  └─────────────┘  └─────────────┘  └─────────────┘     │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                     TESTING PHASE                       │
                    │                                                         │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                    │  │    Unit     │  │ Integration │  │  WhatsApp   │     │
                    │  │   Tests     │  │    Tests    │  │   Testing   │     │
                    │  │  API/ML     │  │  Twilio     │  │  End-to-End │     │
                    │  │ Functions   │  │  Webhook    │  │   Manual    │     │
                    │  └─────────────┘  └─────────────┘  └─────────────┘     │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │       DEPLOYMENT CHOICE         │
                              └─────────────────────────────────┘
                                      │         │         │
                        ┌─────────────┘         │         └─────────────┐
                        ▼                       ▼                       ▼
            ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
            │       HEROKU        │  │      RAILWAY        │  │       RENDER        │
            │                     │  │                     │  │                     │
            │ ┌─────────────────┐ │  │ ┌─────────────────┐ │  │ ┌─────────────────┐ │
            │ │ git push heroku │ │  │ │ railway deploy  │ │  │ │ GitHub connect  │ │
            │ │      main       │ │  │ │                 │ │  │ │   auto-deploy   │ │
            │ └─────────────────┘ │  │ └─────────────────┘ │  │ └─────────────────┘ │
            │                     │  │                     │  │                     │
            │ ┌─────────────────┐ │  │ ┌─────────────────┐ │  │ ┌─────────────────┐ │
            │ │ Config Vars     │ │  │ │ Environment     │ │  │ │ Environment     │ │
            │ │ TWILIO_*        │ │  │ │ Variables       │ │  │ │ Variables       │ │
            │ │ OPENAI_*        │ │  │ │                 │ │  │ │                 │ │
            │ └─────────────────┘ │  │ └─────────────────┘ │  │ └─────────────────┘ │
            └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                        │                       │                       │
                        └───────────┐           │           ┌───────────┘
                                    ▼           ▼           ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                 PRODUCTION READY                        │
                    │                                                         │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                    │  │   HTTPS     │  │  Webhook    │  │ Monitoring  │     │
                    │  │    URL      │  │ Configure   │  │   Logging   │     │
                    │  │  Available  │  │  in Twilio  │  │   Health    │     │
                    │  │             │  │   Console   │  │   Checks    │     │
                    │  └─────────────┘  └─────────────┘  └─────────────┘     │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                    LIVE WHATSAPP BOT                    │
                    │              Ready to receive and respond to             │
                    │                   medical queries 24/7                  │
                    └─────────────────────────────────────────────────────────┘
```

## 🔄 **Error Handling Flow**

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                    ERROR OCCURS                         │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │         ERROR TYPE?             │
                              └─────────────────────────────────┘
                                      │         │         │
                        ┌─────────────┘         │         └─────────────┐
                        ▼                       ▼                       ▼
            ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
            │    LLM API ERROR    │  │   TWILIO ERROR      │  │   SYSTEM ERROR      │
            │                     │  │                     │  │                     │
            │ • API Key Invalid   │  │ • Webhook Failed    │  │ • Server Down       │
            │ • Rate Limit        │  │ • Invalid Number    │  │ • Memory Error      │
            │ • Network Timeout   │  │ • Message Failed    │  │ • Import Error      │
            └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                        │                       │                       │
                        ▼                       ▼                       ▼
            ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
            │   FALLBACK TO ML    │  │   LOG ERROR &       │  │   LOG ERROR &       │
            │                     │  │   RETRY LOGIC       │  │   RETURN GENERIC    │
            │ Use RandomForest    │  │                     │  │     RESPONSE        │
            │ Traditional Model   │  │ Retry 3 times       │  │                     │
            │                     │  │ Different endpoint  │  │ "Please try again"  │
            └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
                        │                       │                       │
                        └───────────┐           │           ┌───────────┘
                                    ▼           ▼           ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   LOG TO SYSTEM                         │
                    │              • Error type and timestamp                 │
                    │              • User message (anonymized)                │
                    │              • Recovery action taken                    │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                 SEND RESPONSE TO USER                   │
                    │           "I apologize, but I'm having technical        │
                    │            difficulties. Please try again later."       │
                    └─────────────────────────────────────────────────────────┘
```

## 📊 **Data Processing Flow**

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                   RAW USER MESSAGE                      │
                    │        "My 5 year old has FEVER & won't eat!!!"        │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                  TEXT PREPROCESSING                     │
                    │                                                         │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                    │  │  Lowercase  │  │   Remove    │  │  Normalize  │     │
                    │  │ Conversion  │  │  Special    │  │ Whitespace  │     │
                    │  │             │  │ Characters  │  │             │     │
                    │  │ "my 5 year  │  │ "my 5 year  │  │ "my 5 year  │     │
                    │  │ old has     │  │ old has     │  │ old has     │     │
                    │  │ fever wont  │  │ fever wont  │  │ fever wont  │     │
                    │  │ eat"        │  │ eat"        │  │ eat"        │     │
                    │  └─────────────┘  └─────────────┘  └─────────────┘     │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                   KEYWORD EXTRACTION                    │
                    │                                                         │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
                    │  │   Medical   │  │     Age     │  │  Symptoms   │     │
                    │  │  Keywords   │  │  Detection  │  │  Severity   │     │
                    │  │             │  │             │  │             │     │
                    │  │ • "fever"   │  │ • "5 year"  │  │ • "wont eat"│     │
                    │  │ • "child"   │  │ • "old"     │  │ • urgency   │     │
                    │  │ • "eat"     │  │ • pediatric │  │   markers   │     │
                    │  └─────────────┘  └─────────────┘  └─────────────┘     │
                    └─────────────────────────────────────────────────────────┘
                                                │
                                                ▼
                              ┌─────────────────────────────────┐
                              │       PROCESSING PATH           │
                              └─────────────────────────────────┘
                                      │                   │
                                    LLM │                 │ Traditional ML
                                        ▼                 ▼
                    ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
                    │        LLM PROCESSING           │   │      TF-IDF VECTORIZATION       │
                    │                                 │   │                                 │
                    │ Context: "5-year-old child      │   │ ┌─────────────────────────────┐ │
                    │ with fever and loss of          │   │ │    Feature Extraction       │ │
                    │ appetite requires immediate     │   │ │                             │ │
                    │ medical attention..."           │   │ │ fever: 0.8                  │ │
                    │                                 │   │ │ child: 0.6                  │ │
                    │ Generate contextual response    │   │ │ eat: 0.4                    │ │
                    │ with age-appropriate advice     │   │ │ year: 0.3                   │ │
                    └─────────────────────────────────┘   │ │ old: 0.2                    │ │
                                                          │ └─────────────────────────────┘ │
                                                          │                                 │
                                                          │ ┌─────────────────────────────┐ │
                                                          │ │   RandomForest Prediction   │ │
                                                          │ │                             │ │
                                                          │ │ Match to trained patterns:  │ │
                                                          │ │ "Pediatric fever advice"    │ │
                                                          │ └─────────────────────────────┘ │
                                                          └─────────────────────────────────┘
                                      │                                   │
                                      └───────────┐           ┌───────────┘
                                                  ▼           ▼
                    ┌─────────────────────────────────────────────────────────┐
                    │                 RESPONSE GENERATION                     │
                    │                                                         │
                    │ "For a 5-year-old with fever who won't eat:            │
                    │                                                         │
                    │ • Monitor temperature closely                           │
                    │ • Offer small amounts of fluids frequently              │
                    │ • Contact pediatrician if fever >101°F                 │
                    │ • Seek immediate care if child is lethargic             │
                    │                                                         │
                    │ ⚠️ DISCLAIMER: This is general information only.        │
                    │ Always consult a pediatrician for child health issues." │
                    └─────────────────────────────────────────────────────────┘
```

These ASCII flowcharts provide a comprehensive visual representation of your WhatsApp Medical AI Chatbot's architecture and processes, perfect for presentations! 🚀