from selenium.webdriver.common.by import By
from selenium import webdriver


first_name_locator = (By.ID, "registrationFirstNameInp-label")
last_name_locator = (By.ID, "registrationLastNameInp-label")
email_locator = (By.ID, "registrationLastNameInp")
password_locator = (By.ID, "registrationPasswordInp")
company_locator = (By.ID, "registrationCompanyInp")
company_country_locator = (By.ID, "react-select-2-input")
phone_locator = (By.ID, "registrationPhoneInp")
agreement_check_box_locator = (By.ID, "agreementChkbox")
signup_button_locator = (By.ID, "registrationSignUpBtn")
is_checked_locator = (By.CSS_SELECTOR,"#root > div > main > div > form > div:nth-child(2) > label > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorDefault.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorDefault.Mui-checked.tss-1u1zsb9-checked.mui-bif1rt")
not_filled_company_name_text = (By.CLASS_NAME, "MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium mui-1rkjp0p")
invalid_company_name_text = (By.LINK_TEXT, "Please enter a valid company name")