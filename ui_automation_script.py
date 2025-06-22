#!/usr/bin/env python3
"""
UI Automation Script configured for popular QA testing websites
Ready-to-use configurations for practicing automation
"""

# Configuration for "The Internet" (Herokuapp) - Most Popular QA Testing Site
the_internet_config = {
    "login": {
        "url": "https://the-internet.herokuapp.com/login",
        "username": "tomsmith",  # Default username for the site
        "password": "SuperSecretPassword!",  # Default password
        "username_selector": "#username",
        "password_selector": "#password",
        "submit_selector": "button[type='submit']"
    },
    "navigation_tests": [
        {
            "url": "https://the-internet.herokuapp.com/secure",
            "expected_title": "The Internet",
            "expected_element": ".flash.success"
        },
        {
            "url": "https://the-internet.herokuapp.com/checkboxes",
            "expected_title": "The Internet",
            "expected_element": "input[type='checkbox']"
        }
    ],
    "form_tests": [
        {
            "form_data": {
                "checkbox1": {
                    "selector": "input[type='checkbox']:first-child",
                    "value": "click"  # Special value to indicate clicking
                },
                "checkbox2": {
                    "selector": "input[type='checkbox']:last-child", 
                    "value": "click"
                }
            }
        }
    ],
    "click_tests": [
        {
            "selector": "a[href='/dropdown']",
            "name": "dropdown link"
        },
        {
            "selector": "a[href='/upload']",
            "name": "file upload link"
        }
    ]
}

# Configuration for Sauce Demo - E-commerce testing
sauce_demo_config = {
    "login": {
        "url": "https://saucedemo.com/",
        "username": "standard_user",  # Valid test username
        "password": "secret_sauce",   # Valid test password
        "username_selector": "#user-name",
        "password_selector": "#password",
        "submit_selector": "#login-button"
    },
    "navigation_tests": [
        {
            "url": "https://saucedemo.com/inventory.html",
            "expected_title": "Swag Labs",
            "expected_element": ".inventory_list"
        }
    ],
    "click_tests": [
        {
            "selector": "#add-to-cart-sauce-labs-backpack",
            "name": "add backpack to cart"
        },
        {
            "selector": ".shopping_cart_link",
            "name": "shopping cart"
        },
        {
            "selector": "#checkout",
            "name": "checkout button"
        }
    ],
    "form_tests": [
        {
            "form_data": {
                "first_name": {
                    "selector": "#first-name",
                    "value": "John"
                },
                "last_name": {
                    "selector": "#last-name",
                    "value": "Doe"
                },
                "postal_code": {
                    "selector": "#postal-code",
                    "value": "12345"
                }
            },
            "submit_selector": "#continue"
        }
    ]
}

# Configuration for DemoQA - Comprehensive testing elements
demo_qa_config = {
    "navigation_tests": [
        {
            "url": "https://demoqa.com/text-box",
            "expected_title": "ToolsQA",
            "expected_element": "#textbox-wrapper"
        },
        {
            "url": "https://demoqa.com/buttons",
            "expected_title": "ToolsQA", 
            "expected_element": ".btn-group-vertical"
        }
    ],
    "form_tests": [
        {
            "form_data": {
                "full_name": {
                    "selector": "#userName",
                    "value": "John Doe"
                },
                "email": {
                    "selector": "#userEmail",
                    "value": "john.doe@example.com"
                },
                "current_address": {
                    "selector": "#currentAddress",
                    "value": "123 Main Street, City, Country"
                },
                "permanent_address": {
                    "selector": "#permanentAddress",
                    "value": "456 Oak Avenue, City, Country"
                }
            },
            "submit_selector": "#submit"
        }
    ],
    "click_tests": [
        {
            "selector": "#doubleClickBtn",
            "name": "double click button"
        },
        {
            "selector": "#rightClickBtn", 
            "name": "right click button"
        }
    ]
}

# Configuration for Automation Practice - E-commerce simulation
automation_practice_config = {
    "navigation_tests": [
        {
            "url": "http://automationpractice.com/index.php",
            "expected_title": "My Store",
            "expected_element": "#homepage-slider"
        }
    ],
    "click_tests": [
        {
            "selector": ".login",
            "name": "sign in link"
        },
        {
            "selector": ".shopping_cart",
            "name": "shopping cart"
        }
    ],
    "form_tests": [
        {
            "form_data": {
                "search": {
                    "selector": "#search_query_top",
                    "value": "dress"
                }
            },
            "submit_selector": "#searchbox button[type='submit']"
        }
    ]
}

# Master test runner for all QA sites
def run_qa_testing_suite():
    """Run automation tests on popular QA testing websites"""
    
    from ui_automation_script import WebUIAutomation
    
    test_sites = {
        "The Internet (Herokuapp)": the_internet_config,
        "Sauce Demo": sauce_demo_config,
        "DemoQA": demo_qa_config,
        "Automation Practice": automation_practice_config
    }
    
    for site_name, config in test_sites.items():
        print(f"\n{'='*50}")
        print(f"🧪 Testing: {site_name}")
        print(f"{'='*50}")
        
        automation = WebUIAutomation(headless=False, timeout=10)  # Visible browser for learning
        
        try:
            automation.run_test_suite(config)
        except Exception as e:
            automation.reporter.log_test_result(
                f"{site_name} - Full Suite", 
                "FAIL", 
                f"Error running test suite: {str(e)}"
            )
        finally:
            automation.cleanup()
            print(f"✅ Completed testing: {site_name}")

# Quick start functions for individual sites
def test_the_internet():
    """Test The Internet (Herokuapp) - Best for beginners"""
    automation = WebUIAutomation(headless=False, timeout=10)
    try:
        automation.run_test_suite(the_internet_config)
    finally:
        automation.cleanup()

def test_sauce_demo():
    """Test Sauce Demo - E-commerce workflow"""
    automation = WebUIAutomation(headless=False, timeout=10)
    try:
        automation.run_test_suite(sauce_demo_config)
    finally:
        automation.cleanup()

def test_demo_qa():
    """Test DemoQA - Form and element interactions"""
    automation = WebUIAutomation(headless=False, timeout=10)
    try:
        automation.run_test_suite(demo_qa_config)
    finally:
        automation.cleanup()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        site = sys.argv[1].lower()
        
        if site == "internet":
            print("🧪 Testing The Internet (Herokuapp)")
            test_the_internet()
        elif site == "sauce":
            print("🧪 Testing Sauce Demo")
            test_sauce_demo()
        elif site == "demoqa":
            print("🧪 Testing DemoQA")
            test_demo_qa()
        elif site == "all":
            print("🧪 Testing All QA Websites")
            run_qa_testing_suite()
        else:
            print("❌ Unknown site. Use: internet, sauce, demoqa, or all")
    else:
        print("🧪 Running default test - The Internet (Herokuapp)")
        test_the_internet()

# Usage Examples:
"""
Run specific site tests:
    python qa_testing_config.py internet
    python qa_testing_config.py sauce  
    python qa_testing_config.py demoqa
    python qa_testing_config.py all

Or import and use in your own scripts:
    from qa_testing_config import test_the_internet
    test_the_internet()
"""