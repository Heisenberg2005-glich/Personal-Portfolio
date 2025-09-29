#!/usr/bin/env python3
"""
Cloud Deployment Helper for Portfolio Website
This script helps you deploy your portfolio to various cloud platforms.
"""

import os
import sys
import subprocess
import json

def create_github_repo():
    """Instructions for creating GitHub repository"""
    print("🐙 GitHub Repository Setup")
    print("=" * 40)
    print("1. Go to https://github.com/new")
    print("2. Repository name: Personal-Portfolio")
    print("3. Make it PUBLIC (required for free hosting)")
    print("4. Don't initialize with README")
    print("5. Click 'Create repository'")
    print("\nThen run these commands:")
    print("git init")
    print("git add .")
    print("git commit -m 'Initial portfolio commit'")
    print("git branch -M main")
    print("git remote add origin https://github.com/Heisenberg2005-glich/Personal-Portfolio.git")
    print("git push -u origin main")

def deploy_to_render():
    """Instructions for Render.com deployment"""
    print("\n🚀 Render.com Deployment")
    print("=" * 40)
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Use these settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn backen.backend:app")
    print("   - Environment: Python 3")
    print("   - Plan: Free")
    print("6. Click 'Create Web Service'")
    print("\nYour site will be live at: https://your-app-name.onrender.com")

def deploy_to_railway():
    """Instructions for Railway deployment"""
    print("\n🚂 Railway Deployment")
    print("=" * 40)
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Click 'Deploy from GitHub repo'")
    print("4. Select your Personal-Portfolio repository")
    print("5. Railway will auto-detect and deploy")
    print("\nYour site will be live at: https://your-app-name.railway.app")

def create_zip_package():
    """Create a zip file for manual upload"""
    print("\n📦 Creating deployment package...")
    try:
        subprocess.run(['zip', '-r', 'portfolio-deployment.zip', 'deployment_package/'], check=True)
        print("✅ Created portfolio-deployment.zip")
        print("📁 You can upload this file to any hosting service!")
    except subprocess.CalledProcessError:
        print("❌ Error creating zip file")
        print("💡 You can manually zip the 'deployment_package' folder")

def main():
    print("🌐 Portfolio Cloud Deployment Helper")
    print("=" * 50)
    print("Choose your deployment method:")
    print("1. GitHub + Render.com (Recommended)")
    print("2. GitHub + Railway")
    print("3. Create ZIP package for manual upload")
    print("4. Show all options")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        create_github_repo()
        deploy_to_render()
    elif choice == "2":
        create_github_repo()
        deploy_to_railway()
    elif choice == "3":
        create_zip_package()
    elif choice == "4":
        create_github_repo()
        deploy_to_render()
        deploy_to_railway()
        create_zip_package()
    else:
        print("❌ Invalid choice")
        return
    
    print("\n🎉 Deployment instructions completed!")
    print("📖 Check DEPLOY_INSTRUCTIONS.md for more details")

if __name__ == "__main__":
    main()

