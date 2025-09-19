# 🏠 Run WhatsApp Bot Locally + Connect to WhatsApp

## 🚀 Quick Local Setup (5 minutes)

### Step 1: Setup Python Environment
```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Setup Environment Variables
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your credentials
nano .env  # or use any text editor
```

**Edit `.env` file:**
```bash
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=whatsapp:+14155238886
FLASK_ENV=development
PORT=5000
```

### Step 3: Extract ML Model
```bash
# This creates the AI model files
python extract_model.py
```

### Step 4: Start the Bot
```bash
# Start Flask server
python whatsapp_bot.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Model loaded successfully
```

### Step 5: Test Locally
```bash
# In another terminal, test the bot
curl http://localhost:5000/health

# Test chatbot
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "I have fever"}'
```

---

## 📱 Connect to WhatsApp (Using ngrok)

Your bot is running locally, but WhatsApp needs a public URL. We'll use ngrok:

### Step 1: Install ngrok
```bash
# Mac
brew install ngrok

# Or download from: https://ngrok.com/download
```

### Step 2: Expose Local Server
```bash
# In a new terminal (keep your bot running)
ngrok http 5000
```

You'll see something like:
```
Forwarding    https://abc123.ngrok.io -> http://localhost:5000
```

**Copy that HTTPS URL!** (e.g., `https://abc123.ngrok.io`)

### Step 3: Get Twilio Credentials
1. Go to [twilio.com](https://twilio.com) and sign up (free $15 credit)
2. Go to Console Dashboard
3. Copy **Account SID** and **Auth Token**
4. Update your `.env` file with these values

### Step 4: Setup WhatsApp Sandbox
1. In Twilio Console → **Messaging** → **Try it out** → **Send a WhatsApp message**
2. You'll see a sandbox number like: `+1 415 523 8886`
3. Follow instructions to join (text a code to that number)
4. Set **Webhook URL** to: `https://abc123.ngrok.io/webhook` (your ngrok URL + /webhook)
5. Set **HTTP Method** to: **POST**
6. Save configuration

### Step 5: Test WhatsApp Integration
1. Send **"hi"** to the Twilio WhatsApp number (`+1 415 523 8886`)
2. You should get a welcome message back!
3. Try: **"I have fever and headache"**
4. The bot should respond with medical advice

---

## 🔧 Troubleshooting Local Setup

### Bot won't start
```bash
# Check Python version (need 3.11+)
python --version

# Check if port is free
lsof -ti:5000 | xargs kill -9

# Restart bot
python whatsapp_bot.py
```

### Model loading errors
```bash
# Regenerate model
rm *.pkl *.json
python extract_model.py

# Check if files were created
ls -la *.pkl
```

### WhatsApp not responding
1. **Check ngrok is running** - Should show forwarding URL
2. **Check webhook URL** - Must be HTTPS, must end with `/webhook`
3. **Check Twilio logs** - Console → Monitor → Logs
4. **Check your bot logs** - Should show incoming messages

### Environment variable issues
```bash
# Test if variables are loaded
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('SID:', os.getenv('TWILIO_ACCOUNT_SID'))
print('Token:', os.getenv('TWILIO_AUTH_TOKEN'))
"
```

---

## 🎯 Complete Local Development Workflow

### Terminal 1: Run the Bot
```bash
cd backend
source venv/bin/activate
python whatsapp_bot.py
```

### Terminal 2: Expose with ngrok
```bash
ngrok http 5000
```

### Terminal 3: Test and Debug
```bash
# Test health
curl http://localhost:5000/health

# Test bot
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"message": "test message"}'

# Watch logs
tail -f app.log  # if you have logging to file
```

---

## 🚀 When Ready to Deploy

Once everything works locally:

### Option 1: Heroku
```bash
./deploy.sh
```

### Option 2: Render
```bash
git add . && git commit -m "Deploy" && git push origin main
# Then connect repo at render.com
```

### Option 3: Railway
```bash
./deploy_railway.sh
```

---

## 💡 Pro Tips

1. **Keep ngrok running** - Each restart gives you a new URL
2. **Use ngrok paid plan** - Gets you a fixed URL ($8/month)
3. **Test thoroughly locally** - Much faster than deploying each change
4. **Check Twilio logs** - Great for debugging webhook issues
5. **Use environment variables** - Never hardcode credentials

---

## 🎉 Success Checklist

- [ ] Bot starts without errors
- [ ] Health endpoint returns 200 OK
- [ ] Model loads successfully
- [ ] ngrok exposes public URL
- [ ] Twilio webhook configured
- [ ] WhatsApp responds to "hi"
- [ ] Medical queries work
- [ ] Ready to deploy!

**You're now running a full WhatsApp medical AI chatbot locally! 🏥🤖**