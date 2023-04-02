from src.pre_built.counter import count_ocurrences


def test_counter():

    # Teste para a palavra "Python"
    camel_case = count_ocurrences("data/jobs.csv", "Python")
    assert camel_case == 1639
    uppercase = count_ocurrences("data/jobs.csv", "PYTHON")
    assert uppercase == 1639
    lowercase = count_ocurrences("data/jobs.csv", "python")
    assert lowercase == 1639

    # Teste para a palavra "Javascript"
    camel_case = count_ocurrences("data/jobs.csv", "Javascript")
    assert camel_case == 1139
    uppercase = count_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert uppercase == 1139
    lowercase = count_ocurrences("data/jobs.csv", "javascript")
    assert lowercase == 1139

    # Teste para a palavra "Ruby"
    camel_case = count_ocurrences("data/jobs.csv", "Ruby")
    assert camel_case == 297
    uppercase = count_ocurrences("data/jobs.csv", "RUBY")
    assert uppercase == 297
    lowercase = count_ocurrences("data/jobs.csv", "ruby")
    assert lowercase == 297
