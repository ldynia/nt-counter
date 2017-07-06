"""
author: Lukasz Dynowski
email: ludd@bioinforamtics.dtu.dk
license: MIT
"""


class Statistic():
    """
    Example: fsa-analyzer data/dna.fsa | python -m json.tool
    """

    def __init__(self, data_file):
        self.data_file = data_file

    def __del__(self):
        self.data_file.close()

    def count_nucleotides(self):
        results = {}
        self.data_file.seek(0)
        for line in self.data_file:
            line = line.strip('\n')
            if not line.startswith('>'):
                for letter in line.strip('\n'):
                    if letter not in results:
                        results[letter] = 0
                    results[letter] += 1
        return results
