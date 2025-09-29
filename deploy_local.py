#!/usr/bin/env python3
"""
Local deployment script for the portfolio website.
This script will help you run your website locally and prepare it for deployment.
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'backen/backend.py',
        'frontend/index.html',
        'frontend/about.html',
        'frontend/technicalSkills.html',
        'frontend/education.html',
        'frontend/projects.html',
        'frontend/certifications.html',
        'requirements.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found!")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def start_server():
    """Start the Flask development server"""
    print("🚀 Starting portfolio website...")
    print("📍 Your website will be available at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Change to the backen directory and run the Flask app
        os.chdir('backen')
        subprocess.run([sys.executable, 'backend.py'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def create_deployment_package():
    """Create a deployment package with all necessary files"""
    print("📦 Creating deployment package...")
    
    # Create a deployment directory
    deploy_dir = Path("deployment_package")
    deploy_dir.mkdir(exist_ok=True)
    
    # Copy all necessary files
    files_to_copy = [
        'backen/backend.py',
        'frontend/',
        'requirements.txt',
        'render.yaml',
        'README.md',
        'DEPLOYMENT.md'
    ]
    
    for item in files_to_copy:
        if os.path.isdir(item):
            # Copy directory
            subprocess.run(['cp', '-r', item, str(deploy_dir)], check=True)
        else:
            # Copy file
            subprocess.run(['cp', item, str(deploy_dir)], check=True)
    
    print(f"✅ Deployment package created in: {deploy_dir}")
    print("📁 You can now upload this folder to any hosting service!")

def main():
    """Main deployment function"""
    print("🚀 Portfolio Website Deployment Helper")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('backen/backend.py'):
        print("❌ Please run this script from the Portfolio root directory")
        return
    
    # Check requirements
    if not check_requirements():
        print("❌ Please fix missing files before deploying")
        return
    
    print("\n🎯 Choose an option:")
    print("1. Run website locally")
    print("2. Create deployment package")
    print("3. Both")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice in ['1', '3']:
        # Install dependencies
        if not install_dependencies():
            return
        
        # Start server
        start_server()
    
    if choice in ['2', '3']:
        # Create deployment package
        create_deployment_package()
    
    print("\n🎉 Deployment process completed!")
    print("📖 Check DEPLOYMENT.md for detailed deployment instructions")

if __name__ == "__main__":
    main()
