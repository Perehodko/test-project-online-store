from pages.product_page import ProductPage
from pages.main_page import MainPage

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_to_basket()
    page1 = MainPage(browser, link) 
    page1.solve_quiz_and_get_code()
    page.should_be_message_about_add_item_to_basket()
    page.should_be_correct_price()



