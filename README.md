<div align="center">

# Bun's Python Project Boilerplate Template
</br>

  [![Python application](https://github.com/NinjaBunny9000/python-project-template/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/NinjaBunny9000/python-project-template/actions/workflows/python-app.yml) [![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?)](/docs/ "Go to project documentation") 

</div>

## Project Information
> *Briefly describe the purpose and functionality of your project, script, or tool*  

This is a boilerplate TEMPLATE for Python projects. It's a starting point that (hopefully) helps cut down on the repetitive project setup tasks and help keep project file structures consistent.

Included are...\n - A boilerplate `main.py` script with logging, cli arguments, and a few other things to help you get started
 - `.env` and `.config` files to help keep secrets secret and simplify configuring your script to run by other users
 - An `environment.yml` file for configuring and setting up environments for your tool
 - Initial test framework and Travis CI integration already setup and ready to rock and roll
 - VSCode `.vscode/` dir with configs for your project to utilize `unittest` and speed up
 - A FastAPI-based REST API with organized project structure, configuration management, and health check endpoint

## Details
- **Project Owner:** *name*
- **Project's Web Page:** [https://www.web.site](https://www.web.site)

## Contributors
* [@author](Author)

---
## Getting Started
> *Describe how to quickly get started running your project.*

Clone this repository to your local machine, create a VENV and install the project's requirements.

### 1. Setup the environment
#### Conda / Mamba
- Create the conda VENV for the project and install the required packages
```bash
conda env create -f environment.yml -n <new-environment-name>
```
- Activate the new VENV
```bash
conda activate <new-environment-name>
```
#### PIP
```sh
pip install -r requirements.txt
```

### 2. Configure the project
- Rename `.config.TEMPLATE` to `.config`. Edit values to work with your local machine.
- Rename `.env.TEMPLATE` to `.env` and update it with any required secrets

### 3. Run the FastAPI Development Server
The project includes a FastAPI-based REST API. To run it:

```bash
cd src
uvicorn api:app --reload
```

- Access the API at `http://localhost:8000`
- View interactive API documentation at `http://localhost:8000/docs`
- Check API health at `http://localhost:8000/api/health`

### 4. Run the CLI Script
Alternatively, you can run the CLI entry point:

```bash
python src/main.py <arguments>
```

## Development Environment
> *List any requirements or additional setup as needed to develop/contribute to this project.*

### Configuring the Environment
> *List any development-specific environment settings or steps here.*

### Running Tests

In VSCode, use the Testing pane.

> From the Command Palette (F1 or ctrl/cmd+shift+p): `View: Show Testing`

![Testing Pane](https://imgur.com/0pLqEAj.png)  

> From the command line: `python -m unittest tests`

### Contributing
> *Detail how to contribute to this project*

---

## ⚠️ IMPORTANT CONSIDERATIONS ⚠️
> *Add more notes here if needed, or feel free remove from the README*
- Store secrets, credentials, or confidential information in `.env`.
  - Use them in the script with `os.environ`.  (e.g. `os.environ['GITHUB_TOKEN']`)
- Store any configuration variables (information that changes from machine to machine) in `.config`
  - Reference them in the script with `cfg`. (e.g. `cfg.RESOURCE_PATH`)

**This project adheres to the following standards:**
> *Use this area for some quick contribution points or guidelines for devs*
- Use `snake_case` for variable names
- Use `camelCase` for function names
  - The first word (lowercase) should be a verb that describes the action it takes. (e.g. `parseData()`)
- Define constants near the top of the file, below imports/setup, with `UPPER_CASE_LIKE_THIS`
- *Import order, etc*
