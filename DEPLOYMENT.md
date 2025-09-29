# 🚀 Portfolio Website Deployment Guide

## 📋 **Deployment Options**

### **Option 1: Render.com (Recommended)**

1. **Sign up** at [render.com](https://render.com)
2. **Connect your GitHub** account
3. **Create a new Web Service**
4. **Configure the service:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backen.backend:app`
   - **Environment**: Python 3
   - **Plan**: Free

### **Option 2: Railway**

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect GitHub** repository
3. **Deploy** automatically
4. **Configure environment variables** if needed

### **Option 3: Heroku**

1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-portfolio-name`
4. **Deploy**: `git push heroku main`

## 🔧 **Pre-Deployment Checklist**

- ✅ **requirements.txt** created
- ✅ **render.yaml** configured
- ✅ **backend.py** updated for production
- ✅ **All dependencies** listed
- ✅ **Static files** properly configured

## 📁 **Project Structure for Deployment**

```
Portfolio/
├── backen/
│   └── backend.py          # Flask app (production ready)
├── frontend/
│   ├── index.html
│   ├── about.html
│   ├── technicalSkills.html
│   ├── education.html
│   ├── projects.html
│   ├── certifications.html
│   └── style/              # CSS files
├── requirements.txt        # Python dependencies
├── render.yaml            # Render.com config
└── README.md
```

## 🌐 **After Deployment**

Your website will be available at:
- **Render**: `https://your-app-name.onrender.com`
- **Railway**: `https://your-app-name.railway.app`
- **Heroku**: `https://your-app-name.herokuapp.com`

## 🔄 **Updating Your Website**

1. **Make changes** to your code
2. **Commit changes**: `git add . && git commit -m "Update portfolio"`
3. **Push to GitHub**: `git push origin main`
4. **Auto-deploy** will trigger on the platform

## 🛠️ **Troubleshooting**

### **Common Issues:**

1. **Static files not loading**
   - Check file paths in backend.py
   - Ensure CSS/JS files are in correct directories

2. **Port issues**
   - Use environment variable: `PORT`
   - Set host to `0.0.0.0`

3. **Dependencies missing**
   - Add all required packages to requirements.txt
   - Include gunicorn for production

## 📞 **Support**

If you encounter issues:
1. Check the deployment logs
2. Verify all files are committed
3. Ensure requirements.txt is complete
4. Check static file paths

---

**Your portfolio is ready for deployment!** 🎉
