class Statistic():

    def __init__(self, file):
        self.file = open(file)
        self.filename = file.split('/')[-1]

    def __del__(self):
        self.file.close()

    def count_nucleotides(self):
        results = {self.filename: {}}
        for line in self.file:
            line = line.strip()
            if not line.startswith('>'):
                for letter in line.strip('\n'):
                    if letter not in results[self.filename]:
                        results[self.filename][letter] = 0
                    results[self.filename][letter] += 1
        return results
