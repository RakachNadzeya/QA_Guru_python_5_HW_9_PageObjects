import os
from selene.support import by
from selene import be, have
from selene import browser

import tests


def test_fill_out_the_form():
    browser.open("/automation-practice-form")

    # WHEN user fills in the form
    browser.element("#firstName").type("Nadzeya")
    browser.element("#lastName").type("Rakach")
    browser.element("#userEmail").type("test.email@gmail.com")
    browser.all("[name=gender]").element_by(have.value("Female")).double_click()
    browser.element("#userNumber").type("1231231231")

    browser.element("#dateOfBirthInput").click()
    browser.element(
        by.xpath(
            "//select[@class='react-datepicker__month-select']/option[.='September']"
        )
    ).click()
    browser.element(by.xpath("//option[@value='1988']")).click()
    browser.element(
        by.xpath("//div[@class='react-datepicker__day react-datepicker__day--020']")
    ).click()

    browser.element("#subjectsInput").click().send_keys("English").press_enter()

    browser.all(".custom-checkbox").element_by(have.exact_text("Reading")).click()

    browser.element("#uploadPicture").type(
        str(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    os.path.pardir,
                    f"tests/resources/1570735001190494352.jpg",
                )
            )
        )
    )


    browser.element("#currentAddress").type("Poland, Gdańsk, Wilcza 1")

    browser.element("#state").click().element(by.xpath("//*[.='Haryana']")).click()
    browser.element("#city").click().element(by.xpath("//*[.='Karnal']")).click()

    browser.element("#submit").click()

    # THEN correct user data is shown
    browser.element(by.xpath("//div[@class='modal-content']")).should(be.present)
    browser.all("tbody tr").should(
        have.texts(
            "Nadzeya Rakach",
            "test.email@gmail.com",
            "Female",
            "1231231231",
            "20 September,1988",
            "English",
            "Reading",
            "1570735001190494352.jpg",
            "Poland, Gdańsk, Wilcza 1",
            "Haryana Karnal",
        )
    )
