import requests


def validate_long_word(url, word):
    res = requests.get(url + word)
    obj = res.json()
    return [d["definition"] for d in obj[0]["meanings"]["definitions"]]    # might not work because of typo


def validate_case_insensitivity(url,word):
    response = requests.get(url + word)

    # Check if the request was successful
    assert response.status_code < 400

    data = response.json()

    # Check if the word in the response is the same as the word in the request (case insensitive)
    return data[0]["word"] == word.lower()