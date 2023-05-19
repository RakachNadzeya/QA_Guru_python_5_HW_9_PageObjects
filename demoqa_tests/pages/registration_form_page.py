import os

from selene import browser, by, have, be
from demoqa_tests.data.users import User


class StudentRegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.element(f'[value={student.gender}]').double_click()
        browser.element('#userNumber').type(student.phone_number)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(student.birthday.year)
        browser.element('.react-datepicker__month-select').type(student.birthday.strftime('%B'))
        browser.element(f'.react-datepicker__day--0{student.birthday.day}').click()

        for subject in student.subjects:
            browser.element('#subjectsInput').type(subject).press_tab()

        for hobby in student.hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.exact_text(student.hobbies)).click()

        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources/{student.picture}")

        browser.element('#currentAddress').type(student.address)

        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()

        browser.element('#submit').click()

    def should_have_registered(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birthday.strftime("%d")} {student.birthday.strftime("%B")},{student.birthday.year}'
        subject = ', '.join([subject for subject in student.subjects])
        hobbies = ', '.join(student.hobbies)
        state_and_city = f'{student.state} {student.city}'

        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone_number}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {student.hobbies}',
            f'Picture {student.picture}',
            f'Address {student.address}',
            f'State and City {state_and_city}')
        )