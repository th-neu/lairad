<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]





<h3 align="center"> local artificial intelligence research and development (lairad)</h3>

  <p align="center">
    <br />
    <a href="https://github.com/th-neu/LIARAD"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  ·
    <a href="https://github.com/th-neu/LIARAD/issues">Report Bug</a>
    ·
    <a href="https://github.com/th-neu/LIARAD/issues">Request Feature</a>
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
        <li><a href="#installation windows">Installation Windows</a></li>                		<li><a href="#enviroment">Enviroment</a></li>
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

lairad is a local artificial intelligence research and development tool. Same input, same output is a goal. Enabling local indepent resaerch to better understand the possibilities of local run/deployed large language models to enable the user.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]
* [![Flask][Flask.com]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Working python installation and pip.

* pyhton pip install

	[https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)


### Installation Linux


1. Clone the repo
   ```sh
   git clone https://github.com/th-neu/LIARAD.git
   ```
2. Install python3 virtual environment (if not installed)
	 ```sh
	sudo apt-get install python3-venv
	```
4. setup the virtual environment
   ```sh
   cd lairad && python3 -m venv lairad
   ```
5. activate the new virtual environment
   ```sh
   source ~/venv/lairad/bin/activate
   ```
6. Install pip packages
   ```sh
   pip -r requirements.txt
   ```
7. Copy env.example to .env
   ```js
   cp env.example .env
   ```
8. edit the .env file
   ```js
   <your favorite editor here> .env
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation Windows


1. Clone the repo
   ```cmd
   git clone https://github.com/th-neu/LIARAD.git
   ```
2. Install python3 virtual environment (if not installed)
	 ```cmd
	sudo apt-get install python3-venv
	```
4. setup the virtual environment
   ```cmd
   cd lairad && python3 -m venv lairad
   ```
5. activate the new virtual environment
   ```cmd
   source ~/venv/lairad/bin/activate
   ```
6. Install pip packages
   ```cmd
   pip -r requirements.txt
   ```
7. Copy env.example to .env
   ```cmd
   cp env.example .env
   ```
8. edit the .env file
   ```cmd
   <your favorite editor here> .env
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Enviroment File Settings
atleast one database (sqlite3 or mariadb at the moment)
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
# DB_PASSWORD=egal=88!
# DB_HOST=192.168.1.6
# DB_PORT=3306
# DB_NAME=LAIRAD

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

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

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
