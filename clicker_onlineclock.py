from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

''' hay que tener en cuenta que el contador en la web empieza por 1, no por 0
    usar numeros negativos para ejecucion infinita  '''

driver = webdriver.Chrome(ChromeDriverManager().install()) # abrimos/instalamos la herramienta 
url = driver.get("https://counter.onlineclock.net/")  # abrimos la url en cuestion para testear
time.sleep(1)


def count_up(clicks):
    if clicks < 0:
        up = True
        while up:
            increase = driver.execute_script("javascript:doCounter('up')")
    else:
        while clicks != 0:
            increase = driver.execute_script("javascript:doCounter('up')")
            clicks -= 1
    time.sleep(1)


def count_down(clicks):
    if clicks < 0:
        down = True
        while down:
            decrease = driver.execute_script("javascript:doCounter('down')")
    else:
        while clicks != 0:
            decrease = driver.execute_script("javascript:doCounter('down')")
            clicks -= 1
    time.sleep(1)


def reset_count():
    reset = driver.execute_script("javascript:doConfirmDelete()")
    time.sleep(1)
    accept_alert = driver.switch_to.alert.accept()
    time.sleep(1)

if __name__ == "__main__":  
    count_up(1200)
    count_down(325)
    reset_count()
    driver.close()  # cerramos el navegador
