# Nucleotides Counter
The goal of this project is to show you how to build an application that will run as a backend service in new CGE framework.

This application counts number of nucleoties in a [FASTA](http://www.cbs.dtu.dk/services/NetGene2/fasta.php) file. Solution is written in [python](https://www.python.org/) and deployed with [docker](https://docker.com/).


## Installation
```bash
$ git clone https://github.com/ldynia/nt-counter
$ cd nt-counter/
```

## Create application's container
Using `docekr`.

```bash
$ docker run --rm ldynia/ntc:1.0 python test/test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ docker run --rm ldynia/ntc:1.0 ntc -i test/data/dna.fsa | python -m json.tool
{
    "a": {
        "A": 333,
        "C": 454,
        "G": 469,
        "T": 303
    }
}
```

Using `docekr-compose` create running container.

```bash
$ docker-compose build
$ docker-compose up -d
$ docker exec ntcounter python /app/test/test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

$ docker run --rm ldynia/ntc:1.0 ntc -i test/data/dna.fsa | python -m json.tool
{
    "a": {
        "A": 333,
        "C": 454,
        "G": 469,
        "T": 303
    }
}
```
