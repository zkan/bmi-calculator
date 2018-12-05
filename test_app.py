import pytest

from app import app, calc_bmi


BASE_URL = '/'


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_page_should_render_correctly(client):
    response = client.get(BASE_URL)
    content = response.data.decode('utf-8')

    assert '<title>BMI Calculator</title>' in content
    assert '<h1>BMI Calculator</h1>' in content
    form_html = '<form class="pure-form" method="POST" action="/">\n\t' \
        'Weight in kgs:<br>\n\t<input type="text" name="weight"><br>\n\t' \
        'Height in cms:<br>\n\t<input type="text" name="height"><br>\n\t' \
        '<button type="submit" class="pure-button pure-button-primary" ' \
        'value="Submit">Submit</button>\n\t</form>'
    assert form_html in content


def test_submit_weight_and_height_should_see_bmi_result(client):
    data = {
        'weight': '80',
        'height': '180'
    }
    response = client.post(BASE_URL, data=data)
    content = response.data.decode('utf-8')

    assert 'Your BMI is 24.69.' in content


def test_calc_bmi():
    bmi = calc_bmi(80, 180)

    assert bmi == 24.69
