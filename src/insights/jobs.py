from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file
    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    job_types = {row['job_type'] for row in data if row['job_type']}
    return list(job_types)
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter
    Returns
    -------
    list
        List of jobs with provided job_type
    """
    """ Cria uma nova lista filtrando os empregos
    cujo job_type é igual ao job_type fornecido"""
    filtered_jobs = [
        job for job in jobs
        if job.get("job_type") == job_type
        ]
    return filtered_jobs
    raise NotImplementedError
