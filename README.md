<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]





<h3 align="center">lairad - local artificial intelligence research and development</h3>

  <p align="center">
    <br />
    <a href="https://github.com/th-neu/lairad"><strong>Explore the docs »</strong></a>
    <br />
    *<a href="https://github.com/th-neu/lairad/issues">Report Bug</a>
    *<a href="https://github.com/th-neu/lairad/issues">Request Feature</a>
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
        <li><a href="#installation linux">Installation Linux</a></li>
        <li><a href="#installation windows">Installation Windows</a></li>                      		<li><a href="#using docker">Using docker</a></li>
        <li><a href="#environment">Environment File</a></li>
      </ul>
    </li>
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

lairad is a local artificial intelligence research and development tool. Same input, same output is a goal. Enabling local independent research to better understand the possibilities of local run/deployed large language models. LLM Models that work well are the 13B vicuna series. More research and data collection is needed here.
<br>
### The Project is in alpha status! 
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
   pip -r requirements.txt
   ```
5. Copy env.example to .env
   ```js
   cp env.example .env
   ```
7. edit the .env file
   ```js
   <your favorite editor here> .env
   ```
8. run app.py
   ```cmd
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
   pip -r requirements.txt
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

Use the installation steps with a virtual environment. Remove # app.py line 224,225 and add # at line 223.
1. Build image with .env file
   ```cmd
   python app.py
   ```

Or use docker compose with the provided Dockerfile.

For armv7 use the Dockerfile.armv7. Remove # app.py line 224,225 and add # at line 223.

1. Pull the docker image
   ```sh
   docker pull ghcr.io/th-neu/docker-py-mariadbc-armhf:latest
	```
2. Build the image
   ```sh
	docker build your-name/image-name . -F Dockerfile.armhf
	```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ENVIRONMENT FILE-->
### Environment File Settings
At least one database (sqlite3 or mariadb at the moment).
Endpoint for llama-cpp-python
The Endpoint for koboldcpp API does not work at the moment

```sh
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

## Endpoint for koboldcpp API
KOBOLDCPP_API_URL=http://localhost:5001/api/v1/generate
## KOBOLDCPP_API_SCHEMA
KOBOLDCPP_FRMTRMSPCH=1
KOBOLDCPP_SINGLELINE=1
KOBOLDCPP_TEMPERATURE=0.2
KOBOLDCPP_TOP_P=0.6
KOBOLDCPP_MAX_LENGTH=500
KOBOLDCPP_TOP_K=40
KOBOLDCPP_REP_PEN=1.1
KOBOLDCPP_TOP_A=0
KOBOLDCPP_STOP_SEQUENCE="}}}"
```
<!-- OTHER CONTAINER-->
### Other docker container

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Translations
    - [ ] German

See the [open issues](https://github.com/th-neu/LIARAD/issues) for a full list of proposed features (and known issues).

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

Project Link: [https://github.com/th-neu/LIARAD](https://github.com/th-neu/LIARAD)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best Readme Template](https://github.com/othneildrew/Best-README-Template)
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
* [koboldcpp](https://github.com/LostRuins/koboldcpp)
* [ghostwriter](https://ghostwriter.kde.org/de/)
* [Auto-gpt](https://github.com/Significant-Gravitas/Auto-GPT)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/th-neu/LIARAD.svg?style=for-the-badge
[contributors-url]: https://github.com/th-neu/LIARAD/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/th-neu/LIARAD.svg?style=for-the-badge
[forks-url]: https://github.com/th-neu/LIARAD/network/members
[stars-shield]: https://img.shields.io/github/stars/th-neu/LIARAD.svg?style=for-the-badge
[stars-url]: https://github.com/th-neu/LIARAD/stargazers
[issues-shield]: https://img.shields.io/github/issues/th-neu/LIARAD.svg?style=for-the-badge
[issues-url]: https://github.com/th-neu/LIARAD/issues
[license-shield]: https://img.shields.io/github/license/th-neu/LIARAD.svg?style=for-the-badge
[license-url]: https://github.com/th-neu/LIARAD/blob/master/LICENSE.md
[product-screenshot]: images/screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Flask.com]: https://img.shields.io/badge/Flask-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Python.org]: https://img.shields.io/badge/Python-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Python-url]: https://www.python.org/
