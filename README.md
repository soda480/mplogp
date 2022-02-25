# mplogp
[![build](https://github.com/soda480/mplogp/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/mplogp/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/soda480/mplogp/branch/main/graph/badge.svg?token=GA62T7LDGK)](https://codecov.io/gh/soda480/mplogp)
[![Code Grade](https://api.codiga.io/project/22249/status/svg)](https://app.codiga.io/public/project/22249/mplogp/dashboard)
[![complexity](https://img.shields.io/badge/complexity-Simple:%204-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

A Python script to parse a logfile generated from multi-processing based tools. The script will parse the logfile and create logs for each process under a specified timestamped folder. Supports log files generated from a log Formatter whose first two fields are: `%(asctime)s %(processName)s ...`.


## `mplogp`
```
usage: mplogp [-h] --log LOG --folder FOLDER [--regex REGEX]

A Python script to parse a logfile generated from multi-processing based tools

optional arguments:
  -h, --help       show this help message and exit
  --log LOG        The location of the logfile to parse
  --folder FOLDER  The folder where to write the parsed logs
  --regex REGEX    Regular expression to alias process log filename - must contain a matched group
```

### Examples
Parse the `example3.log` file and write the parsed logs under the `logs` folder, add alias to each process log with its matched processor id:
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
-v $PWD:/code \
prepbadge:latest \
/bin/bash
```

Build the project:
```bash
pyb -X
```
