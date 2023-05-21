<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Tests][tests-url]][tests-shield]
[![Ruff][Ruff-url]][Ruff-shield]




<h3 align="center">lairad - local artificial intelligence research and development</h3>

  <p align="center">
    <br />
    <a href="https://github.com/th-neu/lairad"><strong>Explore the docs »</strong></a>
    <br />
    *<a href="https://github.com/th-neu/lairad/issues">Report Bug</a>
    *<a href="https://github.com/th-neu/lairad/issues">Request Feature</a>
	*<a href="https://github.com/th-neu/lairad/discussions">Discussion</a>
 </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-linux">Installation Linux</a></li>
        <li><a href="#installation-windows">Installation Windows</a></li>                      		<li><a href="#using-docker">Using docker</a></li>
        <li><a href="#environment-file-settings">Environment File settings</a></li>
      </ul>
    </li>
    <li><a href="#docker-container">Docker container</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

lairad is a local artificial intelligence research and development tool. Same input, same output is a goal. Enabling local independent research to better understand the possibilities of local run/deployed large language models. LLM Models that work well are the 13B vicuna series. More research and data collection is needed here. When ever possible docker containers are used.<br>
* MariaDB for User / Project / Prompt storage<br>
* whoogle-search to have better search control<br>
* gogs to store files and have a commit history

## !!! This is an alpha !!! 
Bug and issues are expected. Adding a new Project (Goal), getting basic search results back, storing that information is all that works for now. New commands will be add once everything about search / tasks works smoothly.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][Python.org]][Python-url]
* [![Flask][Flask.com]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

<!-- PREREQUISITES -->
### Prerequisites

Working python installation and pip.

* pyhton pip install

	[https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

<!-- INSTALLATION LINUX -->
### Installation Linux


1. Clone the repo
   ```sh
   git clone https://github.com/th-neu/lairad.git
   ```
2. Install python3 virtual environment (if not installed)
	 ```sh
	sudo apt-get install python3-venv
	```
3. setup the virtual environment
   ```sh
   cd lairad && python3 -m venv lairad
   ```
4. activate the new virtual environment
   ```sh
   source ~/venv/lairad/bin/activate
   ```
5. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
5. Copy env.example to .env
   ```sh
   cp env.example .env
   ```
7. edit the .env file
   ```sh
   <your favorite editor here> .env
   ```
8. run app.py
   ```sh
   python3 app.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION WINDOWS -->
### Installation Windows


1. Clone the repo
   ```cmd
   git clone https://github.com/th-neu/lairad.git
   ```
2. setup the virtual environment
   ```cmd
   cd lairad && python -m venv lairad
   ```
3. activate the new virtual environment
   ```cmd
   lairad\Scripts\activate.bat
   ```
4. Install pip packages
   ```cmd
   pip install -r requirements.txt
   ```
5. Copy env.example to .env
   ```cmd
   copy env.example .env
   ```
6. edit the .env file
   ```cmd
   <your favorite editor here> .env
   ```
7. run app.py
   ```cmd
   python app.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USING DOCKER -->
### Using docker

Use the installation steps with a virtual environment. Remove # app.py line 224,225 and add # at line 223. Using --rm to remove the container for testing.
1. Build the image
   ```bash
	docker build -t your-name/image-name .
   ```
2. Run the container
   ```bash
	docker run --rm -p 5000:5000 your-name/image-name
	```

For armv7 use the Dockerfile.armv7. Remove # app.py line 224,225 and add # at line 223. Using --rm to remove the container for testing.

1. Pull the docker image
   ```bash
   docker pull ghcr.io/th-neu/docker-py-mariadbc-armhf:latest
	```
2. Build the image
   ```bash
	docker build -t your-name/image-name -f Dockerfile.armv7 .
	```
3. Run the container
   ```bash
	docker run --rm -p 5000:5000 your-name/image-name
	```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ENVIRONMENT FILE-->
### Environment File Settings
Settings for the database (sqlite3 or mariadb at the moment).
</br>Settings for API Endpoint for llama-cpp-python.


```env
## Secret App key
secret_key=<Secret_Key>

## Database connection
# sqlite3 configuration
DB_TYPE=sqlite
DATABASE=example.db
# mariadb configuration
# DB_TYPE=mariadb
# DB_USER=root
# DB_PASSWORD=
# DB_HOST=
# DB_PORT=3306
# DB_NAME=lairad

## Endpoint for llama-cpp-python Python API
# LLAMA_CCP_API_URL=http://localhost:8000/v1/completions
LLAMA_CCP_API_URL=http://localhost:8000/v1/completions
## LLAMA_CCP_API_Schema
LLAMA_TEMPERATURE=0.8
LLAMA_STOP=[}}}, ###]
LLAMA_MAX_TOKEN=300
LLAMA_ECHO=true
```

The Secret Key is not to be shared."It should be a long random string of bytes, although unicode is accepted too." One can use python (windows example):
```cmd
python -c "import os; print(os.urandom(16))"
```
or a Password manager to generate a long random string.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- OTHER CONTAINER-->
### Docker container

This is my choice of container. You can build your own images or install the software directly onto a host system. Docker is recommenced.

[whoogle-search docker installation](https://github.com/benbusby/whoogle-search#manual-docker)<br>
[MariaDB knowledge base](https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/)<br>
[gogs docker installation](https://github.com/gogs/gogs#tutorials)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Navigate your web browser to localhost:5000 (replace with IP for docker / none localhost installation) and use admin/admin to login.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Deploy tests (flask web front end, db back end, python basic logic)
- [ ] Rewrite Code with proper python structure.
- [ ] Working task management (call LLM with goals and act on it [search, write file]).
- [ ] Localization Support
    - [ ] English
    - [ ] German

See the [open issues](https://github.com/th-neu/lairad/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

lairad@runbox.com

Project Link: [https://github.com/th-neu/lairad](https://github.com/th-neu/lairad)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
* [ghostwriter](https://ghostwriter.kde.org/de/)
* [whoogle-search](https://github.com/benbusby/whoogle-search)
* [gogs](https://github.com/gogs/gogs)
* [pylint](https://pylint.org/)
* [Auto-gpt](https://github.com/Significant-Gravitas/Auto-GPT)
* [Best Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/th-neu/lairad.svg?style=plastic
[contributors-url]: https://github.com/th-neu/lairad/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/th-neu/lairad.svg?style=plastic
[forks-url]: https://github.com/th-neu/lairad/network/members
[tests-shield]: https://github.com/th-neu/lairad/actions/workflows/python-tests.yml/badge.svg?branch=main
[tests-url]: https://github.com/th-neu/lairad/actions/workflows/python-tests.yml
[stars-shield]: https://img.shields.io/github/actions/th-neu/lairad.svg?style=plastic
[stars-url]: https://github.com/th-neu/lairad/stargazers
[issues-shield]: https://img.shields.io/github/issues/th-neu/lairad.svg?style=plastic
[issues-url]: https://github.com/th-neu/lairad/issues
[license-shield]: https://img.shields.io/github/license/th-neu/lairad.svg?style=plastic
[license-url]: https://github.com/th-neu/lairad/blob/master/LICENSE.md
[product-screenshot]: images/screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=plastic&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Flask.com]: https://img.shields.io/badge/Flask-563D7C?style=plastic&logo=bootstrap&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Python.org]: https://img.shields.io/badge/Python-563D7C?style=plastic&logo=bootstrap&logoColor=white
[Python-url]: https://www.python.org/
[Ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json?style=plastic
[Ruff-url]: https://github.com/charliermarsh/ruff
