from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from services.helper import transform_unordered_semester_data
from services.selenium_service import SeleniumService
import json
import config

def login(wait, username, password):
    # Login Screen
    wait.until(EC.element_to_be_clickable((By.ID, config.USERNAME_FIELD))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.ID, config.PASSWORD_FIELD))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, config.LOGIN_BUTTON))).click()
    # Homepage
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.PRUEFUNG_RESULTS_LINK))).click()
    # Grade overview page
    wait.until(EC.visibility_of_element_located((By.ID, config.SEMESTER_OPTION_SELECTOR)))
    return

def select_semester(driver, wait, semester: int):
    original_window = driver.current_window_handle
    semester_grades = []

    # Target semester dropdown
    select_element = driver.find_element(By.ID, config.SEMESTER_OPTION_SELECTOR)
    select = Select(select_element)

    # Store all choice values of the semester dropdown
    semester_array = []
    for option in select.options:
        semester_array.append(option.text)
    semester_array.reverse()

    # Select the chosen semester
    select.select_by_visible_text(semester_array[semester])

    # Stores all the links for the grades of one semester
    popup_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='tbdata']/a[contains(@id, 'Popup_details')]")))

    # Stores all grades and details of all modules of the semester
    for popup_link in popup_links:
        semester_grades = get_module(driver, wait, popup_link, semester_grades, original_window)

    return semester_grades

def get_module(driver, wait, popup_link, semester_grades, original_window):
    # Opens the next page for the modules
    driver.execute_script("arguments[0].click();", popup_link)  # Click via JavaScript to bypass potential issues
    print(f"Clicked: {popup_link.get_attribute('id')}")  # Debugging output (comment it out)
    wait.until(EC.number_of_windows_to_be(2))

    new_window = (set(driver.window_handles) - {original_window}).pop()
    driver.switch_to.window(new_window)

    # stores the table and rows
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.tb")))
    rows = table.find_elements(By.TAG_NAME, "tr")

    # filters for rows with the necessary information (in that case of class tbdata)
    tbdata_rows = [row for row in rows if row.find_elements(By.CLASS_NAME, "tbdata")]

    unordered_module_information = []
    # Extract and print the text inside each <td class="tbdata">
    for index, row in enumerate(tbdata_rows):
        # Find all <td> elements within the row
        td_elements = row.find_elements(By.CLASS_NAME, "tbdata")
        
        # Extract text from each <td> and strip unnecessary spaces
        row_text = [td.text.strip() for td in td_elements]
        
        unordered_module_information.append(row_text)
    
    # Stores the name of the module which lies outside of the table
    try:
        h1_element = driver.find_element(By.TAG_NAME, "h1")
        module_name = h1_element.text.strip() if h1_element else None
    except NoSuchElementException:
        module_name = None

    transform_unordered_semester_data(unordered_module_information, semester_grades, module_name)

    # Closes the module page and switches back to the overview tab
    driver.close()
    driver.switch_to.window(original_window)
    return semester_grades


def dualis_main(username, password, semester):
    selenium_service = SeleniumService()

    # Open the dualis login page
    selenium_service.driver.get(config.DUALIS_LINK)
    login(selenium_service.wait, username, password)

    semester_grades = select_semester(selenium_service.driver, selenium_service.wait, semester-1)

    # Convert to JSON format
    json_output = json.dumps(semester_grades, indent=4, ensure_ascii=False)

    # Print JSON
    print(json_output)

    # Close the browser
    selenium_service.close()
    return semester_grades
