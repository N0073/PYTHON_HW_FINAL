class TestData:
    """Тестовые данные для UI и API тестов"""

    # API endpoints
    ENDPOINTS = {
        "menu": "/menu",
        "cart": "/cart",
        "order": "/order",
        "restaurant_info": "/restaurant/{restaurant_id}"
    }

    # UI Locators
    SEARCH_INPUT = "input[data-test id='search-input']"
    SEARCH_BUTTON = "button[data-test id='search-button']"
    RESTAURANT_CARD = "div[data-test id='restaurant-card']"
    MENU_SECTION = "section[data-test id='menu-section']"
    WORKING_HOURS = "div[data-test id='working-hours']"
    LOGIN_BUTTON = "button[data-test id='login-button']"
    CART_ICON = "div[data-test id='cart-icon']"


    # Test Data
    SEARCH_QUERY = "Пицца"
    RESTAURANT_NAME = "Test Restaurant"
    PRODUCT_NAME = "Маргарита"
    INVALID_QUANTITY = 0
    VALID_QUANTITY = 2

    # Credentials
    TEST_EMAIL = "test_user@example.com"
    TEST_PASSWORD = "TestPass123"
