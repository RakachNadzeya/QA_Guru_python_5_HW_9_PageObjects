import os

from selene import browser, have, command


class StudentRegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).double_click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def select_subject(self, value):
        browser.element('#subjectsInput').click().send_keys(value).press_enter()

    def select_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        
    def upload_picture(self, path):
        file_path = os.path.join(os.getcwd(), 'resources', path)
        browser.element('#uploadPicture').send_keys(file_path)

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, name):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def select_city(self, name):
        browser.element('#city').perform(command.js.scroll_into_view)
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit_form(self):
        browser.element("footer").execute_script('element.remove()')
        browser.element('#submit').execute_script('element.click()')

    def should_have_user_info(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture,
                              current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                current_address,
                state_and_city,
            )
        )
        return self