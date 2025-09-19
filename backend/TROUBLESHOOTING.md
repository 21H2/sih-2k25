# 🛠️ Troubleshooting Guide

## 🚂 Railway Deployment Issues

### Error: "Error creating build plan with Railpack"

This is a common Railway issue. Here are solutions:

#### Solution 1: Use Railway CLI (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Use our deployment script
./deploy_railway.sh
```

#### Solution 2: Switch to Render (Most Reliable)
```bash
# Push to GitHub
git add . && git commit -m "Deploy" && git push origin main

# Go to render.com and connect your repo
# Render will use the render.yaml file automatically
```

#### Solution 3: Fix Railway Configuration
1. Ensure these files exist in your backend folder:
   - `nixpacks.toml`
   - `requirements.txt`
   - `railway.json`

2. Check your `requirements.txt` for syntax errors:
```bash
# Test locally
pip install -r requirements.txt
```

3. Try manual Railway deployment:
```bash
railway login
railway init
railway up
```

---

## 🏗️ Heroku Deployment Issues

### Error: "Application Error"
```bash
# Check logs
heroku logs --tail --app your-app-name

# Common fixes:
heroku config:set TWILIO_ACCOUNT_SID=your_sid
heroku config:set TWILIO_AUTH_TOKEN=your_token
```

### Error: "No web processes running"
```bash
# Scale up web dyno
heroku ps:scale web=1 --app your-app-name
```

### Error: "Module not found"
```bash
# Ensure Procfile exists with correct content
echo "web: gunicorn whatsapp_bot:app" > Procfile
git add . && git commit -m "Fix Procfile" && git push heroku main
```

---

## 🤖 Model Loading Issues

### Error: "Model files not found"
```bash
# Extract model locally first
python extract_model.py

# Check if files were created
ls -la *.pkl

# If files exist, ensure they're committed to git
git add *.pkl
git commit -m "Add model files"
git push origin main
```

### Error: "Pickle loading failed"
```bash
# Regenerate model files
rm *.pkl *.json
python extract_model.py

# Test model loading
python -c "
import pickle
with open('medical_model.pkl', 'rb') as f:
    model = pickle.load(f)
print('Model loaded successfully!')
"
```

---

## 📱 WhatsApp Integration Issues

### Messages not being received
1. **Check Twilio Console**
   - Go to Console → Monitor → Logs
   - Look for webhook delivery failures

2. **Verify Webhook URL**
   - Must be HTTPS (not HTTP)
   - Must end with `/webhook`
   - Must be publicly accessible

3. **Test Webhook URL**
```bash
# Test if your app is accessible
curl https://your-app.herokuapp.com/health

# Should return: {"status": "healthy", ...}
```

### Messages not being sent
1. **Check Twilio Credentials**
```bash
# Verify environment variables
heroku config --app your-app-name
# Should show TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
```

2. **Check Twilio Balance**
   - Ensure you have credit in your Twilio account
   - Sandbox is free but has limitations

3. **Verify Phone Number Format**
   - Should be: `whatsapp:+14155238886` (for sandbox)
   - Include `whatsapp:` prefix

---

## 🔧 Local Development Issues

### Error: "Port already in use"
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
export PORT=8000
python whatsapp_bot.py
```

### Error: "Module not found"
```bash
# Install requirements
pip install -r requirements.txt

# Or create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Error: "Environment variables not found"
```bash
# Create .env file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

---

## 🧪 Testing Issues

### Health check fails
```bash
# Test locally
python whatsapp_bot.py
# In another terminal:
curl http://localhost:5000/health
```

### Model prediction fails
```bash
# Test model directly
python -c "
from whatsapp_bot import MedicalChatbot
bot = MedicalChatbot()
response = bot.get_medical_advice('I have fever')
print(response)
"
```

---

## 🌐 Network and SSL Issues

### SSL Certificate errors
- Ensure your deployment platform provides HTTPS
- Twilio requires HTTPS for webhooks
- Use ngrok for local testing: `ngrok http 5000`

### Timeout errors
```bash
# Increase timeout in Procfile
echo "web: gunicorn whatsapp_bot:app --timeout 120" > Procfile
```

---

## 📊 Performance Issues

### Slow response times
1. **Optimize model loading**
   - Model loads once at startup
   - Check if model files are too large

2. **Increase server resources**
   - Heroku: Upgrade to hobby dyno ($7/month)
   - Railway/Render: Upgrade plan

3. **Add caching**
   - Cache common responses
   - Use Redis for session storage

### Memory issues
```bash
# Check memory usage
heroku logs --tail | grep "Memory"

# Optimize model size
# Consider using smaller ML models
```

---

## 🔍 Debugging Steps

### 1. Check Application Logs
```bash
# Heroku
heroku logs --tail --app your-app-name

# Railway
railway logs

# Render
# Check logs in Render dashboard
```

### 2. Test Each Component
```bash
# Test health endpoint
curl https://your-app.herokuapp.com/health

# Test chatbot endpoint
curl -X POST https://your-app.herokuapp.com/test \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}'
```

### 3. Verify Environment Variables
```bash
# Heroku
heroku config --app your-app-name

# Railway
railway variables

# Should show all required variables
```

---

## 🆘 Getting Help

### 1. Check Common Issues First
- Review this troubleshooting guide
- Check deployment platform status pages
- Verify Twilio service status

### 2. Gather Information
Before asking for help, collect:
- Error messages (full stack trace)
- Platform logs
- Environment configuration
- Steps to reproduce

### 3. Where to Get Help
- **GitHub Issues**: For code-related problems
- **Platform Support**: For deployment issues
- **Twilio Support**: For WhatsApp integration issues

### 4. Emergency Fallback
If nothing works, try the Docker approach:
```bash
# Build and run locally
docker build -t medical-chatbot .
docker run -p 8080:8080 --env-file .env medical-chatbot
```

---

## ✅ Success Checklist

Before considering your deployment successful:

- [ ] Health endpoint returns 200 OK
- [ ] Test endpoint processes messages
- [ ] Twilio webhook is configured correctly
- [ ] WhatsApp sandbox responds to "hi"
- [ ] Medical queries return appropriate responses
- [ ] All environment variables are set
- [ ] Logs show no critical errors

---

**Remember: The sandbox is perfect for testing. Only upgrade to production WhatsApp if you need it for real business use!**