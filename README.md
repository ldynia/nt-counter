# Nucleotides Counter
The goal of this project is to show you how to build an application that will run as a backend service in new CGE framework.This application counts number of nucleotides in a [FASTA](http://www.cbs.dtu.dk/services/NetGene2/fasta.php).

## Requirements
* [docker](https://docker.com/) installed.


## Installation
```bash
$ git clone https://github.com/ldynia/nt-counter
$ cd nt-counter/
$ docker build -t ldynia/ntc:1.0 -f docker/Dockerfile .
```

## Create application's container
Using `docekr`.

```bash
$ docker run --rm ldynia/ntc:1.0 python test/test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ docker run --rm ldynia/ntc:1.0 ntc -i test/data/dna_one.fsa test/data/dna_two.fsa
{
    "dna_one.fsa": {
        "G": 469,
        "A": 333,
        "T": 303,
        "C": 454
    },
    "dna_two.fsa": {
        "G": 135,
        "A": 65,
        "T": 64,
        "C": 96
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

$ docker run --rm ldynia/ntc:1.0 ntc -i test/data/dna_one.fsa test/data/dna_two.fsa
{
    "dna_one.fsa": {
        "G": 469,
        "A": 333,
        "T": 303,
        "C": 454
    },
    "dna_two.fsa": {
        "G": 135,
        "A": 65,
        "T": 64,
        "C": 96
    }
}
```
