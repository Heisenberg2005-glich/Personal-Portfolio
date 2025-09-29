#!/usr/bin/env python3
"""
Portfolio Website Starter Script
Run this to start your portfolio website locally.
"""

import os
import sys
import subprocess

def main():
    print("🚀 Starting Portfolio Website...")
    print("=" * 50)
    
    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True)
        print("✅ Dependencies installed!")
    except:
        print("⚠️  Installing dependencies...")
    
    # Start the server
    print("\n🌐 Starting Flask server...")
    print("📍 Your portfolio will be available at: http://localhost:5005")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        os.chdir('backen')
        subprocess.run([sys.executable, 'backend.py'])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
