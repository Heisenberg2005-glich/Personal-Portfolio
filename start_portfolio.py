#!/usr/bin/env python3
"""
Simple portfolio deployment script.
This will start your portfolio website locally.
"""

import os
import sys
import subprocess
import time

def main():
    print("🚀 Starting Portfolio Website...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('backen/backend.py'):
        print("❌ Please run this script from the Portfolio root directory")
        return
    
    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed!")
    except subprocess.CalledProcessError:
        print("⚠️  Some dependencies might not be installed, but continuing...")
    
    # Start the server
    print("\n🌐 Starting Flask server...")
    print("📍 Your portfolio will be available at: http://localhost:5000")
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

if __name__ == "__main__":
    main()

