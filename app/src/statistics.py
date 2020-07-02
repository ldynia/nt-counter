class Statistic():

    def __init__(self, file):
        self.file = file

    def __del__(self):
        self.file.close()

    def count_nucleotides(self):
        results = {}
        self.file.seek(0)
        for line in self.file:
            line = line.strip()
            if not line.startswith('>'):
                for letter in line.strip('\n'):
                    if letter not in results:
                        results[letter] = 0
                    results[letter] += 1
        return results
