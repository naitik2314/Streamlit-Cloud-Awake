# 🌐 Random Text Selector with Selenium

This Python-based project leverages the **Selenium WebDriver** to visit a website, perform random text selection, and revisit the website at random intervals between **6 to 24 hours**. The script highlights randomly selected visible text on the page and mimics human-like behavior by scrolling and interacting with the page.

---

## 🚀 Features

- 🎯 **Random Text Selection**: Dynamically locates and highlights random visible text elements on the page., to give the impression of active users
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

---

## 📜 Usage

### Configuration
- 🔗 **Set the Website URL**: Update the `URL` variable in the script to the website you want to visit.
- 📂 **Driver Path**: Update the `executable_path` in the script with the path to your browser driver.

### Run the Script
1. Execute the script:
   ```bash
   python3 streamlit-awake.py
   
2. The script will:
- Visit the specified website.
- Wait for the page to load.
- Randomly select a visible text element, scroll to it, highlight it, and simulate interaction.
- Wait for a random interval (6–24 hours) before revisiting the website.

---

## 📂 Project Structure

```plaintext
random-text-selector/
│
├── streamlit-awake.py  # main script
├── README.md                # Project documentation
```
---

## 🖥️ Demo

### 🎨 **Active User Stimulation**:

### 📊 **Console Output**:
```plaintext
Navigating to https://example.com...
Found 50 text elements.
Found 30 visible text elements.
Highlighted text: "Welcome to Example!"
Hovered over the random text element.
Waiting for 8 hours and 15 minutes before the next visit...
```
---

## 📖 How It Works

1. **Random Text Selection**:
   - Locates all text elements on the webpage using the XPath `//*[text()]`.
   - Filters out non-visible elements to ensure interactions are valid.
   - Randomly selects one of the visible text elements for interaction.

2. **Human-like Interaction**:
   - Scrolls the selected text element into view.
   - Highlights the element with a red border (`2px solid red`).
   - Simulates a hover action using Selenium's `ActionChains`.

3. **Revisit Logic**:
   - Revisits the website at a random interval (6–24 hours).
   - Repeats the random text selection and interaction process.

---

## ⚙️ Customization

1. **Change Interval**:
   Modify the interval in seconds for revisiting:
   ```python
   wait_time = random.randint(6 * 3600, 24 * 3600)  # 6 to 24 hours
   ```
2. Target Specific Tags: To restrict the selection to specific HTML tags like <p> or <span>:
   ```python
   text_elements = driver.find_elements(By.XPATH, "//p | //span")

---

## 📧 Contact

Feel free to reach out for suggestions or contributions!  
**Email**: naitik@wayne.edu  
**GitHub**: [naitik2314](https://github.com/naitik2314)

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🌟 Contributions

Contributions are welcome! Fork this repository, create a feature branch, and submit a pull request.

