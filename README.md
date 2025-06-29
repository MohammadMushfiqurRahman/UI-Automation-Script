﻿# UI Automation Script for Web Applications

<div align="center">
  <h2>🤖 Comprehensive Python-based UI Automation Framework</h2>
  <p>Selenium WebDriver • Robust Error Handling • Detailed Reporting • Configurable Test Scenarios</p>
</div>

---

## 🚀 FEATURES

### Core Capabilities
- **🔐 Login Automation** - Automated login workflows with configurable selectors
- **🎯 Core UI Actions** - Click, input, navigation, and form filling operations  
- **✅ Smart Assertions** - Element text, page title, and presence validations
- **🛡️ Error Handling** - Comprehensive exception handling with screenshot capture
- **📊 Test Reporting** - HTML reports with pass/fail statistics and visual evidence
- **⚡ Flexible Configuration** - JSON-based test configuration for easy customization

---

## 🛠️ TECH STACK

| Technology | Purpose |
|------------|---------|
| **Python 3.7+** | Core scripting language |
| **Selenium WebDriver** | Browser automation engine |
| **Chrome/ChromeDriver** | Browser driver |
| **HTML DOM** | Element manipulation |
| **CSS Selectors** | Element targeting |

---

## 📋 PREREQUISITES

- ✅ Python 3.7 or higher
- ✅ Google Chrome browser  
- ✅ ChromeDriver (automatically managed or manually installed)

---

## 🔧 INSTALLATION

1. **Clone the repository:**
```bash
git clone https://github.com/MohammadMushfiqurRahman/ui-automation-script.git
cd ui-automation-script
```

2. **Install required packages:**
```bash
pip install selenium
```

3. **Download ChromeDriver:**
   - **Option A**: Use WebDriver Manager (Recommended)
   ```bash
   pip install webdriver-manager
   ```
   
   - **Option B**: Manual Installation
     - Download from [ChromeDriver Downloads](https://chromedriver.chromium.org/)
     - Add to your system PATH

## 🚀 Quick Start

### Basic Usage

```python
from ui_automation import WebUIAutomation

# Initialize automation
automation = WebUIAutomation(headless=True, timeout=15)

# Define test configuration
test_config = {
    "login": {
        "url": "https://example.com/login",
        "username": "your-email@example.com",
        "password": "your-password",
        "username_selector": "input[name='email']",
        "password_selector": "input[name='password']",
        "submit_selector": "button[type='submit']"
    },
    "navigation_tests": [
        {
            "url": "https://example.com/dashboard",
            "expected_title": "Dashboard",
            "expected_element": ".dashboard-content"
        }
    ]
}

# Run tests
try:
    automation.run_test_suite(test_config)
finally:
    automation.cleanup()
```

### Running the Example

```bash
python ui_automation_script.py
```

## 📝 Configuration Guide

### Test Configuration Structure

```python
test_config = {
    # Login Configuration (Optional)
    "login": {
        "url": "login_page_url",
        "username": "your_username",
        "password": "your_password",
        "username_selector": "input[name='username']",  # CSS selector
        "password_selector": "input[name='password']",   # CSS selector
        "submit_selector": "button[type='submit']"       # CSS selector
    },
    
    # Navigation Tests
    "navigation_tests": [
        {
            "url": "page_to_test",
            "expected_title": "Expected Page Title",
            "expected_element": ".expected-css-selector"
        }
    ],
    
    # Form Tests
    "form_tests": [
        {
            "form_data": {
                "field_name": {
                    "selector": "input[name='field']",
                    "value": "test_value"
                }
            },
            "submit_selector": "button[type='submit']"
        }
    ],
    
    # Click Tests
    "click_tests": [
        {
            "selector": ".button-to-click",
            "name": "descriptive_name"
        }
    ]
}
```

## 🎨 Features Overview

### 🔐 Login Automation
- Configurable field selectors
- Automatic login verification
- Support for various authentication forms
- Post-login redirect validation

### 🎯 UI Actions
```python
# Safe element finding with timeout
element = automation.safe_find_element(By.CSS_SELECTOR, ".my-element", "element name")

# Safe clicking with fallback
automation.safe_click(element, "button name")

# Form filling with validation
automation.fill_form(form_data, submit_selector)

# Navigation with verification
automation.navigate_and_verify(url, expected_element, expected_title)
```

### ✅ Assertions
```python
# Text content assertion
automation.assert_element_text(element, "expected text", "element name")

# Page title assertion
automation.assert_page_title("Expected Title")
```

### 📊 Reporting Features
- **HTML Reports**: Visual test results with statistics
- **Screenshot Capture**: Automatic screenshots on failures
- **Detailed Logging**: Timestamped logs with status indicators
- **Test Metrics**: Pass/fail counts and execution time

## 📁 Project Structure

```
ui-automation-script/
├── ui_automation_script.py    # Main automation script
├── README.md                  # This file
├── requirements.txt           # Python dependencies
└── test_reports/             # Generated test reports
    ├── test_log_YYYYMMDD_HHMMSS.log
    ├── test_report_YYYYMMDD_HHMMSS.html
    └── screenshots/
```

## 🔍 Example Test Report

The script generates comprehensive HTML reports including:

- **Test Summary**: Total, passed, and failed test counts
- **Detailed Results**: Individual test outcomes with timestamps
- **Screenshots**: Visual evidence for failed tests
- **Execution Logs**: Detailed logging information

![Test Report Example](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=Test+Report+Dashboard)

## 🛡️ Error Handling

The framework includes robust error handling for common scenarios:

- **Element Not Found**: Timeout handling with screenshots
- **Click Intercepted**: JavaScript fallback execution
- **Network Issues**: Retry mechanisms and graceful degradation
- **Page Load Problems**: Wait strategies and verification

## ⚙️ Advanced Configuration

### Custom Timeouts
```python
automation = WebUIAutomation(headless=False, timeout=20)
```

### Headless vs. GUI Mode
```python
# Headless mode (faster, no GUI)
automation = WebUIAutomation(headless=True)

# GUI mode (visible browser, debugging)
automation = WebUIAutomation(headless=False)
```

### Custom Chrome Options
```python
# Modify the setup_driver method to add custom options
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-notifications")
```

## 📋 Best Practices

1. **Use Descriptive Selectors**: Prefer `data-testid` or stable CSS classes
2. **Implement Waits**: Always use explicit waits instead of `time.sleep()`
3. **Handle Dynamic Content**: Account for loading states and dynamic elements
4. **Screenshot on Failures**: Capture visual evidence for debugging
5. **Modular Test Design**: Break complex workflows into smaller, reusable methods

## 🐛 Troubleshooting

### Common Issues

**ChromeDriver Version Mismatch:**
```bash
# Update ChromeDriver to match your Chrome version
pip install --upgrade webdriver-manager
```

**Element Not Found:**
- Verify CSS selectors in browser dev tools
- Check for dynamic content loading
- Increase timeout values

**Login Failures:**
- Validate credentials and selectors
- Check for CAPTCHA or additional security measures
- Verify post-login redirect behavior

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Selenium WebDriver](https://selenium-python.readthedocs.io/) for browser automation
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) for element inspection
- Python community for excellent testing frameworks

## 📞 Support

