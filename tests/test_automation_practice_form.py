from selene import have

from demoqa_tests.pages.student_registration_page import StudentRegistrationPage


def test_fill_out_the_form():
    registration_page = StudentRegistrationPage()

    # open the form
    registration_page.open()

    # fill the form
    registration_page.fill_first_name('Nadzeya')
    registration_page.fill_last_name('Rakach')
    registration_page.fill_email('random.email@gmail.com')
    registration_page.select_gender('Female')
    registration_page.fill_phone_number('1231231231')
    registration_page.fill_date_of_birth('1988', 'September', '20')
    registration_page.select_subject('English')
    registration_page.select_hobby('Reading')
    registration_page.upload_picture('1570735001190494352.jpg')
    registration_page.fill_current_address('Poland, Gdańsk, Wilcza 1')
    registration_page.select_state('Haryana')
    registration_page.select_city('Karnal')

    # submit the form
    registration_page.submit_form()

    # form should have registered user
    registration_page.should_have_user_info(
        'Nadzeya Rakach',
        'random.email@gmail.com',
        'Female',
        '1231231231',
        '20 September,1988',
        'English',
        'Reading',
        '1570735001190494352.jpg',
        'Poland, Gdańsk, Wilcza 1',
        'Haryana Karnal'
    )