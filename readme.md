# Nucleotides Counter
This application is a simple program that counts number of nucleotides in a **\*.fsa** file. The application is written in [python](https://www.python.org/) and deployed with [docker](https://docker.com/).

Goal of this project is to demonstrate how to build an application/service that will run as a standalone program, as well as a component of a pipeline.


**Installation**
```
user@machine:~$ cd ~
user@machine:~$ mkdir -p pipeline && cd pipeline
user@machine:~/pipeline$ git clone https://github.com/ldynia/nucleotide-counter
user@machine:~/pipeline$ cd nucleotide-counter/
```

**Create application's container**
Using `docekr-compose` create running container.
```
user@machine:~/pipeline/nucleotide-counter$ docker-compose up -d
```

**Test application**
Run application's test.

```
user@machine:~/pipeline/nucleotide-counter$ docker exec nucleotide_1.0 python test/test.py
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

**Run application**
Run program.
```
user@machine:~/pipeline/nucleotide-counter$ docker exec nucleotide_1.0 ntcounter data/dna.fsa
{"A": 333, "C": 454, "T": 303, "G": 469
```
