from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # lê os dados do arquivo especificado pelo parâmetro `path`, mds !
    all_jobs = read(path)
    # variável para armazenar o salário mais alto encontrado até o momento
    highSalary = 0
    """percorre cada emprego e verifica se o salário máximo é um número
    inteiro e maior que o salário mais alto encontrado até agora"""
    for job in all_jobs:
        if job['max_salary'].isdigit() and int(job['max_salary']) > highSalary:
            """ se o salário máximo é válido e maior que o salário
            mais alto encontrado até agora, atualiza highSalary"""
            highSalary = int(job['max_salary'])
    # passa por favor !
    return highSalary
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)

    # Percorre os dados e encontra o menor salário
    salaries = [
        int(row["min_salary"])
        for row in data
        if row.get("min_salary").isdigit()
        ]
    min_salary = min(salaries) if salaries else 0

    return min_salary
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        # Tenta obter os valores de min_salary e max_salary do dicionário 'job'
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])

        """ Verifica se a faixa salarial faz sentido
        (ou seja, min_salary não é maior que max_salary)"""
        if min_salary > max_salary:
            raise ValueError(
                "'min_salary' should not be greater than 'max_salary'."
                )

        # Converte o valor de 'salary' para um inteiro (caso seja uma string)
        the_salary = int(salary)

    except (KeyError, ValueError, TypeError):
        # Caso ocorra algum erro, dispara uma exceção ValueError
        raise ValueError("Invalid job or salary values.")

    """ Caso contrário, retorna True se o salário está
    dentro da faixa salarial do trabalho, e False caso contrário"""
    return min_salary <= the_salary <= max_salary
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            """verifica se a faixa salarial do cargo
             corresponde ao parâmetro salarial"""
            match = matches_salary_range(job, salary)
        except ValueError:
            """se min_salary ou max_salary não
            forem numéricos, ignore o trabalho"""
            pass
        else:
            if match:
                filtered_jobs.append(job)

    return filtered_jobs
    raise NotImplementedError
