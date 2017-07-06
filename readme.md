# Nucleotides Counter
This application is a simple program that counts number of nucleotides in a **\*.fsa** file. The application is written in [python](https://www.python.org/) and deployed with [docker](https://docker.com/).

Goal of this project is to demonstrate how to build an application/service that will run as a standalone program, as well as a component of a pipeline.


**Create application's container**
Using `docekr-compose` create running container.
```
$ docker-compose up -d
```

**Test application**
Run application's test.

```
$ docker exec nucleotide_1.0 python test/test.py
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

**Run application**
Run program.
```
$ docker exec nucleotide_1.0 ntcounter data/dna.fsa
{"A": 333, "C": 454, "T": 303, "G": 469
```
