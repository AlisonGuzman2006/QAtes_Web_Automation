
def assert_is_text_contained_elements(elements, text):
    assert any(text in element.text for element in elements), "No element contains the text " + str(text)


def assert_element_is_deleted(elements, text):
    assert not any(text in element.text for element in elements), f"Task '{text}' was not deleted."