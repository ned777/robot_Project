# Robot — eBay Product Title Scraper (Playwright, Python 3.14, Ubuntu 24.04)

## Overview
This project demonstrates browser automation using **Playwright** with **Python 3.14**.  
It launches Chromium, searches eBay for the keyword **"kvm displayport"**, scrolls to trigger lazy-loaded results, and prints the first valid product title (skipping sponsored listings).

---

## Features
- Automated search with Playwright
- Dynamic content handling (scroll + lazy loading)
- Ad/skippable content filtering
- Error handling for timeouts and missing elements
- Clean, readable, well-documented code

---

## Prerequisites
- Python **3.14+**
- pip (Python package manager)
- Internet connection (Playwright downloads the browser)

---

## Installation

### 1. Clone or extract the folder
git clone https://github.com/<your-username>/Robot.git
cd Robot

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate     # Linux

### 3. Install dependencies
pip install -r requirements.txt
playwright install

---

## Running the Program

### 1. Run the script from inside the Robot directory:
python main.py

### 2. The script will open Chromium, navigate to eBay, and display something like:

Searching for 'kvm displayport' on eBay...
Found product: TESmart 2-Port KVM Switch DisplayPort 1.4 8K60Hz 4K144Hz USB3.0 Audio Mic

---

## Notes
- Verified functional on Ubuntu 24.04 LTS with Python 3.14 and Playwright 1.47.0.
- This project uses clean, modular code suitable for review and version control.





