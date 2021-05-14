# mplogp
[![build](https://github.com/soda480/mplogp/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/mplogp/actions/workflows/main.yml)
[![coverage](https://img.shields.io/badge/coverage-100.0%25-green)](https://pybuilder.io/)
[![complexity](https://img.shields.io/badge/complexity-Simple:%204-green)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-green)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

A log parser for parsing logfile generated from multi-processing based tools. Supports log files generated with Formatter whose first two fields are: `%(asctime)s %(processName)s ...`.


## `mplogp`
```
usage: mplogp [-h] --log LOG --folder FOLDER [--regex REGEX]

A log parser for parsing logs generated from multi-processing based tools

optional arguments:
  -h, --help       show this help message and exit
  --log LOG        The location of the logfile to parse
  --folder FOLDER  The folder where to write the parsed logs
  --regex REGEX    Regular expression to alias process log filename - must contain a matched group
```

### Examples
Parse the `example3.log` file and write output to the `logs` folder and alias process their respective processor id:
```
mplogp --log example3.log --folder logs --regex ".*processor id (.*)$"
```
The log file contained logs from 10 processes and produced the following logs:
```
logs
└── 2021-05-13_18-48-46
    ├── MainProcess.log
    ├── Process-1-69b41899.log
    ├── Process-10-c40f3916.log
    ├── Process-2-a6ffc5b5.log
    ├── Process-3-14175157.log
    ├── Process-4-90e875c2.log
    ├── Process-5-ef35f44f.log
    ├── Process-6-c7268544.log
    ├── Process-7-7557d6d6.log
    ├── Process-8-e248e861.log
    └── Process-9-0bb23bab.log
```

## Development

Build the Docker image:
```bash
docker image build \
-t prepbadge:latest .
```

Run the Docker container:
```bash
docker container run \
--rm \
-it \
-v $PWD:/mplogp \
prepbadge:latest /bin/sh
```

Build the project:
```bash
pyb -X
```