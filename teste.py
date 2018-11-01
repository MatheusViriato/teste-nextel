# Importing dependencies
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def main():
    # JSON containing keys for Google search
    entry_json = { 
        "google-me": [
            "Nextel",
            "telefonia do futuro",
            "selenium python"
        ]
    }

    # Starting Firefox driver and initializing variables
    driver = webdriver.Firefox()
    driver.get("http://www.google.com.br")
    list_results = []
    dictionary = {}

    # To each json key
    for search_key in entry_json["google-me"]:

        # Search key in Google
        input_element = driver.find_element_by_name("q")
        input_element.send_keys(search_key)
        input_element.submit()

        print('Pesquisando "' + search_key + '" no Google')

        driver.implicitly_wait(10)

        # Getting results from a tag h3
        results = driver.find_elements_by_tag_name('h3')

        print('Os 3 primeiros resultados:')
        # Adding the first 3 results in the list_results
        # and printing in the console
        for result in results[:3]:
            list_results.append(result.text)
            print(result.text)
        
        # Adding searched key with your results in the dictionary
        dictionary[search_key] = list_results

        # Cleaning list for other results in loop
        list_results = []

        # zzzzzz for 2 seconds
        time.sleep(2)

        # Reloading google page
        driver.get("http://www.google.com")

    # Finally, printing JSON/Dictionary
    print(dictionary)

    # saving JSON/Dictionary to a output file
    writeOutput(dictionary)

    driver.quit()

# saving JSON/Dictionary to a output file
def writeOutput(dictionary):
    f = open("output.json","w+")
    f.write(json.dumps(dictionary, ensure_ascii=False))

if __name__ == "__main__":
    main()