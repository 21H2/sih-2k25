# 🚀 QUICK START - Get Your WhatsApp Bot Running in 10 Minutes!

## 🎯 The Fastest Way (Choose One):

### Option 1: Heroku (Recommended - Free)
```bash
# Run the automated deployment script
./deploy.sh
```
That's it! The script handles everything.

### Option 2: Railway (Modern Alternative)
1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Connect GitHub repo
4. Add environment variables in Railway dashboard
5. Deploy automatically

---

## 📱 WhatsApp Setup (2 minutes):

### 1. Get Twilio Account (Free)
- Go to [twilio.com](https://twilio.com)
- Sign up (get $15 free credit)
- Go to Console Dashboard
- Copy **Account SID** and **Auth Token**

### 2. WhatsApp Sandbox
- Console → Messaging → Try WhatsApp
- Join sandbox by texting the code to +1 415 523 8886
- Set webhook URL to: `https://your-app.herokuapp.com/webhook`
- Set method to: POST

### 3. Test It!
- Text "hi" to +1 415 523 8886
- Should get welcome message back
- Try: "I have fever and headache"

---

## 🏠 Local Testing (Optional):

```bash
# Setup locally
./local_setup.sh

# Start server
python3 whatsapp_bot.py

# In another terminal, expose to internet
ngrok http 5000

# Use ngrok URL for Twilio webhook
```

---

## 🎉 You're Done!

Your medical AI chatbot is now live on WhatsApp!

**Sandbox Limitations:**
- Only you can chat with it
- Twilio number (+1 415 523 8886)
- Perfect for testing and personal use

**To go live with real WhatsApp:**
- Apply for WhatsApp Business API (takes time)
- Need business verification
- Costs money but reaches anyone

---

## 🆘 Need Help?

**Common Issues:**
- **"Application Error"**: Check `heroku logs --tail`
- **No WhatsApp response**: Verify webhook URL
- **Model errors**: Run `python3 extract_model.py`

**Test URLs:**
- Health: `https://your-app.herokuapp.com/health`
- Test: `https://your-app.herokuapp.com/test`

**Support:**
- Check DEPLOYMENT_GUIDE.md for detailed steps
- All logs are available in your hosting platform
- Twilio console shows message delivery status