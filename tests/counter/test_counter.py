from src.pre_built.counter import count_ocurrences


def test_counter():
    """Testa se a contagem de palavras é feita
    corretamente para a palavra 'Python' em letras minúsculas"""
    count = count_ocurrences("data/jobs.csv", "python")
    assert count == 1639

    """Testa se a contagem de palavras é feita corretamente
     para a palavra 'Python' em letras maiúsculas"""
    count = count_ocurrences("data/jobs.csv", "PYTHON")
    assert count == 1639

    """Testa se a contagem de palavras é feita corretamente
    para a palavra 'Javascript' em letras minúsculas"""
    count = count_ocurrences("data/jobs.csv", "javascript")
    assert count == 1190

    """Testa se a contagem de palavras é feita corretamente
    para a palavra 'Javascript' em letras maiúsculas"""
    count = count_ocurrences("data/jobs.csv", "JAVASCRIPT")
    assert count == 1190
