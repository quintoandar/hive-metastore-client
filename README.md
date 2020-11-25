## Hive Metastore Client
_A client for connecting and running DMLs on hive metastore._

[![Release](https://img.shields.io/github/v/release/quintoandar/hive-metastore-client)]((https://pypi.org/project/hive-metastore-client/))
![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8-brightgreen.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

| Source    | Downloads                                                                                                                       | Page                                                 | Installation Command                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| **PyPi**  | [![PyPi Downloads](https://pepy.tech/badge/hive-metastore-client)](https://pypi.org/project/hive-metastore-client/)                      | [Link](https://pypi.org/project/hive-metastore-client/)        | `pip install hive-metastore-client `                  |

### Build status
| Develop                                                                     | Stable                                                                            | Documentation                                                                                                                                           | Sonar                                                                                                                                                                                    |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Test](https://github.com/quintoandar/hive-metastore-client/workflows/Test/badge.svg) | ![Publish](https://github.com/quintoandar/hive-metastore-client/workflows/Publish/badge.svg) | [![Documentation Status](https://readthedocs.org/projects/hive-metastore-client/badge/?version=latest)](https://hive-metastore-client.readthedocs.io/en/latest/?badge=latest) | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=quintoandar_hive_metastore_client&metric=alert_status)](https://sonarcloud.io/dashboard?id=quintoandar_hive_metastore_client) |

  
### Requirements
The requirements of the project were split in order to better organize and facilitate the installation of both full and individual sets of requirements, according to each one's needs.
```
|-- requirements.dev.txt        < for developing / changing the source code >
|-- requirements.lint.txt       < for linting code >
|-- requirements.test.txt       < for running unit and integration tests >
|-- requirements.txt            < for the project being able to run in a production environment >
|-- docs/requirements.docs.txt  < for recreating the documentation's files >
```

### Code Style and Type checking
Running isolated checks:
- To check style: run `make style-check`
- To check type: run `make type-check`

Running all the checks at once:
- run: `make checks`

To fix style (_with black_):
- run `make apply-style`

## License
[Apache License 2.0](https://github.com/quintoandar/hive-metastore-client/blob/staging/LICENSE)

## Contributing
All contributions are welcome! Feel free to open Pull Requests. Check the development and contributing **guidelines** described [here](CONTRIBUTING.md).

Made with :heart: by the **Data Engineering** team from [QuintoAndar](https://github.com/quintoandar/)