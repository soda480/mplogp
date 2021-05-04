# mplogp
[![coverage](https://img.shields.io/badge/coverage-100.0%25-green)](https://pybuilder.io/)
[![complexity](https://img.shields.io/badge/complexity-Simple:%202-green)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-green)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

A log parser for parsing logs generated from multi-processing based tools.


## `mplogp`
```
usage: mplogp [-h] --log LOG

A log parser for parsing logs generated from multi-processing based tools

optional arguments:
  -h, --help  show this help message and exit
  --log LOG   Location of the logfile to parse
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