from metodos import UrbanRoutesPage
import data
from localizadores import UrbanRoutesPageL
# import codigo
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.loc = UrbanRoutesPageL()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        self.routes_page.wait_for_load_home_page()
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_choose_fare(self):
        self.routes_page.click_order_a_taxi_button()
        self.routes_page.wait_for_page_confort() #cree este metodo para esperar a que aparezca el elemento en la pantalla
        self.routes_page.click_fare_comfort()
        tariff= self.driver.find_elements(*self.loc.fare_comfort)
        assert "card" in self.driver.find_element(*self.loc.fare_comfort).get_attribute("class") #tener en class el texto card
        assert tariff[4].is_enabled() # 4 ubicacion de la tarifa confort y is enabled verificar que un elemento este seleccionado



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
