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
    assert camel_case == 122
    uppercase = count_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert uppercase == 122
    lowercase = count_ocurrences("data/jobs.csv", "javascript")
    assert lowercase == 122
