# Nucleotides Counter
Goal of this project is to demonstrate how to build an application/service that will run as a standalone program/microservice. Additionally, program/microservice can be incorporate to a data pipeline.

The docekr image contains an application that counts number of codons in a **\*.fsa** file. The application is written in [python](https://www.python.org/) and deployed with [docker](https://docker.com/).


## Installation
```bash
user@machine:~$ cd ~
user@machine:~$ mkdir -p pipeline && cd pipeline
user@machine:~/pipeline$ git clone https://github.com/ldynia/nucleotide-counter
user@machine:~/pipeline$ cd nucleotide-counter/
```

## Create application's container
Using `docekr-compose` create running container.

```bash
user@machine:~/pipeline/nucleotide-counter$ docker-compose up -d
```

## Test application
Run application's test.

```bash
user@machine:~/pipeline/nucleotide-counter$ docker exec nucleotide python test/test.py
----------------------------------------------------------------------
Ran 1 test in 0.001s
OK
```

## Run application
Run program.

```bash
user@machine:~/pipeline/nucleotide-counter$ docker exec nucleotide ntcount data/dna.fsa
{"A": 333, "C": 454, "T": 303, "G": 469, "random": true}
```
