# 🏥 WhatsApp Medical AI Chatbot - Backend

> Transform your ML notebook into a production-ready WhatsApp chatbot that provides medical advice using AI/ML models.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![Twilio](https://img.shields.io/badge/Twilio-WhatsApp-red.svg)](https://twilio.com)
[![Deploy](https://img.shields.io/badge/Deploy-Heroku-purple.svg)](https://heroku.com)

## 🚀 Quick Start

```bash
# Clone and setup
git clone <your-repo>
cd backend

# One-command deployment
./deploy.sh

# Or setup locally
./local_setup.sh
python3 whatsapp_bot.py
```

## 📱 Features

- 🤖 **AI-Powered Medical Advice** - Uses trained ML models for symptom analysis
- 📲 **WhatsApp Integration** - Full Twilio WhatsApp Business API integration
- 🏥 **Medical Safety** - Built-in disclaimers and safety warnings
- 🔍 **Smart Text Processing** - Advanced NLP preprocessing for medical queries
- 📊 **Health Monitoring** - API endpoints for system health checks
- 🚀 **Production Ready** - Scalable Flask app with proper error handling

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   WhatsApp      │───▶│   Twilio     │───▶│   Flask App     │
│   User          │    │   Webhook    │    │   /webhook      │
└─────────────────┘    └──────────────┘    └─────────────────┘
                                                     │
                                            ┌─────────────────┐
                                            │   ML Model      │
                                            │   RandomForest  │
                                            └─────────────────┘
```

## 📁 Project Structure

```
backend/
├── whatsapp_bot.py          # Main Flask application
├── extract_model.py         # ML model extraction from notebook
├── ml.ipynb                 # Original Jupyter notebook
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku deployment config
├── runtime.txt              # Python version specification
├── deploy.sh                # One-click Heroku deployment
├── local_setup.sh           # Local development setup
├── test_chatbot.py          # Testing utilities
├── .env.example             # Environment variables template
└── README.md                # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- Twilio Account (free tier available)
- Git

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your Twilio credentials

# Extract ML model
python extract_model.py

# Start development server
python whatsapp_bot.py
```

### Production Deployment

#### Option 1: Heroku (Recommended)
```bash
./deploy.sh
```

#### Option 2: Railway
```bash
# Push to GitHub, then connect to Railway
git add . && git commit -m "Deploy" && git push origin main
```

#### Option 3: Manual Heroku
```bash
heroku create your-app-name
heroku config:set TWILIO_ACCOUNT_SID=your_sid
heroku config:set TWILIO_AUTH_TOKEN=your_token
heroku config:set TWILIO_PHONE_NUMBER=whatsapp:+14155238886
git push heroku main
```

## ⚙️ Configuration

### Environment Variables
```bash
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=whatsapp:+14155238886
FLASK_ENV=production
PORT=5000
```

### Twilio WhatsApp Setup
1. Create [Twilio account](https://twilio.com)
2. Go to Console → Messaging → WhatsApp
3. Join sandbox: text code to +1 415 523 8886
4. Set webhook URL: `https://your-app.herokuapp.com/webhook`
5. Set HTTP method: `POST`

## 🔌 API Endpoints

### WhatsApp Webhook
```http
POST /webhook
Content-Type: application/x-www-form-urlencoded

Body=user_message&From=whatsapp:+1234567890
```

### Health Check
```http
GET /health

Response:
{
  "status": "healthy",
  "model_loaded": true,
  "twilio_configured": true
}
```

### Test Chatbot
```http
POST /test
Content-Type: application/json

{
  "message": "I have fever and headache"
}
```

## 🤖 ML Model

The chatbot uses a **RandomForest classifier** trained on medical Q&A data:

- **Input**: User symptoms/medical queries
- **Processing**: TF-IDF vectorization with medical text preprocessing
- **Output**: Medical advice with safety disclaimers
- **Accuracy**: ~70% on test data

### Model Files
- `medical_model.pkl` - Trained RandomForest model
- `vectorizer.pkl` - TF-IDF vectorizer
- `model_metadata.json` - Model performance metrics

## 📊 Usage Examples

### Conversation Flow
```
User: "Hi"
Bot: "🏥 Welcome to Medical AI Assistant! I can help with health questions..."

User: "I have fever and headache"
Bot: "Most fever encountered in general practice are viral... 
     ⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only."

User: "Bye"
Bot: "Thank you for using Medical AI Assistant. Take care! 🏥"
```

## 🧪 Testing

```bash
# Test locally
python test_chatbot.py

# Test deployed app
curl https://your-app.herokuapp.com/health

# Test chatbot endpoint
curl -X POST https://your-app.herokuapp.com/test \
  -H "Content-Type: application/json" \
  -d '{"message": "I have stomach pain"}'
```

## 🔒 Security & Compliance

- ⚠️ **Medical Disclaimers**: All responses include safety warnings
- 🔐 **Environment Variables**: Sensitive data stored securely
- 📝 **Logging**: Comprehensive request/response logging
- 🚫 **Rate Limiting**: Built-in Twilio rate limits
- 🏥 **Medical Ethics**: Encourages professional consultation

## 📈 Monitoring & Scaling

### Heroku Monitoring
```bash
# View logs
heroku logs --tail

# Scale dynos
heroku ps:scale web=2

# Monitor performance
heroku addons:create newrelic:wayne
```

### Key Metrics
- Response time < 2 seconds
- 99.9% uptime target
- Message delivery rate
- Model prediction accuracy

## 🛠️ Troubleshooting

### Common Issues

**1. "Application Error" on Heroku**
```bash
heroku logs --tail
# Check for missing environment variables or model files
```

**2. WhatsApp Messages Not Working**
- Verify webhook URL is correct and accessible
- Check Twilio console for delivery errors
- Ensure environment variables are set

**3. Model Loading Errors**
```bash
python extract_model.py
# Re-extract model from notebook
```

**4. Local Development Issues**
```bash
# Install missing dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.11+
```

## 💰 Cost Breakdown

### Free Tier
- **Heroku**: Free (with sleep after 30min inactivity)
- **Twilio**: $15 free credit (~3000 messages)
- **WhatsApp Sandbox**: Free forever

### Production Costs
- **Heroku Hobby**: $7/month (no sleep)
- **Twilio WhatsApp**: $0.005 per message
- **WhatsApp Business API**: $40+/month (for verified business)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This chatbot provides **informational medical advice only**. It is not a substitute for professional medical diagnosis, treatment, or advice. Always consult qualified healthcare professionals for medical concerns.

## 🆘 Support

- 📖 **Documentation**: Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- 🚀 **Quick Start**: See [QUICK_START.md](QUICK_START.md)
- 🐛 **Issues**: Open GitHub issue
- 💬 **Discussions**: GitHub Discussions tab

---

Made with ❤️ for healthcare accessibility