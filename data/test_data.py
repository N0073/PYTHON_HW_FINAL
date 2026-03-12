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
    SEARCH_INPUT = "input[data-testid='search-input']"
    SEARCH_BUTTON = "button[data-testid='search-button']"
    RESTAURANT_CARD = "div[data-testid='restaurant-card']"
    MENU_SECTION = "section[data-testid='menu-section']"
    WORKING_HOURS = "div[data-testid='working-hours']"
    LOGIN_BUTTON = "button[data-testid='login-button']"
    CART_ICON = "div[data-testid='cart-icon']"

    # Test Data
    SEARCH_QUERY = "Пицца"
    RESTAURANT_NAME = "Test Restaurant"
    PRODUCT_NAME = "Маргарита"
    INVALID_QUANTITY = 0
    VALID_QUANTITY = 2

    # Credentials
    TEST_EMAIL = "test_user@example.com"
    TEST_PASSWORD = "TestPass123"
