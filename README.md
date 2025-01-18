# 🌐 Random Text Selector with Selenium

This Python-based project leverages the **Selenium WebDriver** to visit a website, perform random text selection, and revisit the website at random intervals between **6 to 24 hours**. The script highlights randomly selected visible text on the page and mimics human-like behavior by scrolling and interacting with the page.

---

## 🚀 Features

- 🎯 **Random Text Selection**: Dynamically locates and highlights random visible text elements on the page.
- ⏲️ **Custom Intervals**: Re-visits the website at random intervals ranging from 6 to 24 hours.
- 🖱️ **Realistic Interactions**: Mimics human interaction by scrolling to text elements and simulating mouse hover actions.
- 🔧 **Robust and Flexible**: Handles hidden elements gracefully and works across any website with visible text.
- ✅ **Error-Handled Execution**: Provides clear error handling and debugging information.

---

## 🛠️ Requirements

- **Python**: Version `3.10.16`  
- **Selenium**: Version `4.27.1`
- **Browser Driver**: Compatible browser driver (e.g., ChromeDriver for Google Chrome)

---

## 📋 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/naitik2314/Streamlit-Cloud-Awake.git
   cd Streamlit-Cloud-Awake

2. **Set up Python Environment**: Create and Activate a virtual environment:
   Either using Conda or Python venv
   ```bash
   # Conda
   conda create --name environmentname python=3.10.16
   conda activate environmentname
   conda install selenium==4.27.1
               OR
   # Python venv
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install selenium==4.27.1

3. Download Broswer Webdriver
   For Google Chrome: [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads)
   Ensure the driver version matches your browser version.
   
