from datetime import date

from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_form_page import StudentRegistrationPage


def test_fill_out_the_form():
    student = User(
        first_name='Nadzeya',
        last_name='Rakach',
        email='random.email@gmail.com',
        gender='Female',
        phone_number='1231231231',
        birthday=date(1988, 9, 20),
        subjects=['English'],
        hobby='2',
        hobbies='Reading',
        picture='1570735001190494352.jpg',
        address='Poland, Gdańsk, Wilcza 1',
        state='Haryana',
        city='Karnal'
    )

    registration_page = StudentRegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_have_registered(student)