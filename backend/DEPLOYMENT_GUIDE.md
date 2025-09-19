# 🚀 Complete WhatsApp Chatbot Deployment Guide

## Step 1: Choose Your Deployment Platform

### Option A: Heroku (Easiest - Recommended for beginners)
### Option B: Railway (Modern alternative)
### Option C: DigitalOcean App Platform
### Option D: AWS/Google Cloud (Advanced)

---

## 🔥 OPTION A: HEROKU DEPLOYMENT (RECOMMENDED)

### 1. Create Heroku Account
- Go to [heroku.com](https://heroku.com)
- Sign up for free account
- Install Heroku CLI: `brew install heroku/brew/heroku` (Mac) or download from website

### 2. Prepare Your App
```bash
# Login to Heroku
heroku login

# Create new app (replace 'your-bot-name' with unique name)
heroku create your-medical-bot-name

# Add Python buildpack
heroku buildpacks:set heroku/python
```

### 3. Set Environment Variables on Heroku
```bash
# You'll get these from Twilio (Step 2)
heroku config:set TWILIO_ACCOUNT_SID=your_sid_here
heroku config:set TWILIO_AUTH_TOKEN=your_token_here
heroku config:set TWILIO_PHONE_NUMBER=whatsapp:+14155238886
```

### 4. Deploy to Heroku
```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Deploy
git push heroku main
```

Your app will be live at: `https://your-medical-bot-name.herokuapp.com`

---

## 📱 STEP 2: TWILIO WHATSAPP SETUP

### 1. Create Twilio Account
- Go to [twilio.com/console](https://console.twilio.com)
- Sign up (you get $15 free credit)
- Verify your phone number

### 2. Get WhatsApp Sandbox Access
- In Twilio Console → Messaging → Try it out → Send a WhatsApp message
- Follow instructions to join sandbox
- Note down your sandbox number (usually +1 415 523 8886)

### 3. Configure Webhook
- In WhatsApp Sandbox settings
- Set **Webhook URL** to: `https://your-medical-bot-name.herokuapp.com/webhook`
- Set **HTTP Method** to: `POST`
- Save configuration

### 4. Get Your Credentials
- Go to Console Dashboard
- Copy **Account SID** and **Auth Token**
- Update your Heroku config with these values

---

## 🔥 OPTION B: RAILWAY DEPLOYMENT (MODERN ALTERNATIVE)

### Method 1: Railway CLI (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Run deployment script
./deploy_railway.sh
```

### Method 2: GitHub Integration
- Push your code to GitHub repository
- Go to [railway.app](https://railway.app) and sign up
- Connect Railway to your GitHub repo
- Set environment variables in Railway dashboard
- Railway will auto-deploy

### 3. Set Environment Variables
- In Railway dashboard → Variables
- Add your Twilio credentials:
  - `TWILIO_ACCOUNT_SID`
  - `TWILIO_AUTH_TOKEN`
  - `TWILIO_PHONE_NUMBER=whatsapp:+14155238886`

### 4. Troubleshooting Railway Issues
If you get "Error creating build plan with Railpack":

**Option A: Use Render instead (more reliable)**
```bash
# Deploy to Render
git push origin main
# Go to render.com and connect your repo
```

**Option B: Fix Railway configuration**
- Ensure `nixpacks.toml` exists in your backend folder
- Check that `requirements.txt` is valid
- Try deploying with Railway CLI instead of GitHub integration

---

## 🚀 OPTION C: RENDER DEPLOYMENT (MOST RELIABLE)

### 1. Create Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub (free tier available)

### 2. Deploy from GitHub
- Push code to GitHub
- Connect Render to your repository
- Render auto-detects Python and uses `render.yaml`

### 3. Set Environment Variables
- In Render dashboard → Environment
- Add Twilio credentials

### 4. Benefits
- More reliable than Railway
- Better error messages
- Automatic HTTPS
- Good free tier

---

## 🔧 STEP 3: TESTING YOUR DEPLOYMENT

### 1. Test Health Endpoint
```bash
curl https://your-app-url.herokuapp.com/health
```

### 2. Test Chatbot Endpoint
```bash
curl -X POST https://your-app-url.herokuapp.com/test \
  -H "Content-Type: application/json" \
  -d '{"message": "I have fever"}'
```

### 3. Test WhatsApp
- Send "hi" to your Twilio WhatsApp number
- Should get welcome message back

---

## 🏥 STEP 4: PRODUCTION WHATSAPP (OPTIONAL)

### For Real WhatsApp Business Account:

1. **Apply for WhatsApp Business API**
   - Go to Twilio → WhatsApp → Request Access
   - Fill business verification form
   - Wait for approval (can take days/weeks)

2. **Get Verified Business Profile**
   - Need registered business
   - Business verification documents
   - Facebook Business Manager account

3. **Production Setup**
   - Get dedicated WhatsApp number
   - Complete business verification
   - Higher rate limits and features

---

## 🛠️ TROUBLESHOOTING

### Common Issues:

**1. "Application Error" on Heroku**
```bash
heroku logs --tail
```
Check logs for specific errors

**2. WhatsApp Messages Not Working**
- Verify webhook URL is correct
- Check Twilio error logs
- Ensure environment variables are set

**3. Model Not Loading**
- Check if model files are included in deployment
- Verify extract_model.py ran successfully

**4. Timeout Errors**
- Heroku free tier sleeps after 30min inactivity
- Consider upgrading to hobby tier ($7/month)

---

## 💰 COSTS BREAKDOWN

### Free Tier:
- **Heroku**: Free (with limitations)
- **Twilio**: $15 free credit
- **WhatsApp Sandbox**: Free forever

### Paid Options:
- **Heroku Hobby**: $7/month (no sleep)
- **Twilio WhatsApp**: ~$0.005 per message
- **Business WhatsApp**: $40+/month

---

## 🔒 SECURITY CONSIDERATIONS

1. **Never commit credentials to git**
2. **Use environment variables**
3. **Enable Twilio webhook validation**
4. **Add rate limiting for production**
5. **Monitor usage and costs**

---

## 📞 SUPPORT

If you get stuck:
1. Check Heroku/Railway logs
2. Check Twilio error logs
3. Test endpoints individually
4. Verify all environment variables

The sandbox is perfect for testing and personal use. Only upgrade to business WhatsApp if you need it for a real business with many users.Create a multilingual AI chatbot to educate rural and semi-urban populations about preventive healthcare, disease symptoms, and vaccination schedules. The chatbot should integrate with government health databases and provide real-time alerts for outbreaks.
