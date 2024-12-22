# AutoGen-base

![CodeQL](https://github.com/jonrichards/autogen-base/actions/workflows/codeql.yml/badge.svg) ![Dependency Review](https://github.com/jonrichards/autogen-base/actions/workflows/dependency-review.yml/badge.svg)

Base project for [AutoGen](https://github.com/microsoft/autogen) development.

## Introduction

This project uses [devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) for [VSCode](https://code.visualstudio.com/) to create a development environment for [AutoGen](https://github.com/microsoft/autogen).

## Features

- [devcontainer based development environment](https://code.visualstudio.com/docs/devcontainers/containers) for [VSCode](https://code.visualstudio.com/).
- [Python 3.x](https://www.python.org/) [docker](https://www.docker.com/) image base.
- [OpenAI](https://www.openai.com/) API integration.
- [black](https://pypi.org/project/black/) formatting on save.
- [isort](https://pypi.org/project/isort/) import sorting on save.
- [pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) linting.
- [code spell checking](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) with custom [workspace dictionary](.vscode/settings.json).

See [requirements.txt](requirements.txt) for the full list of Python packages and versions used.

## Using

1. Open the project in [VSCode](https://code.visualstudio.com/).
1. Ensure the [devcontainers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) is installed.
1. Copy `OAI_CONFIG_LIST.sample` to `OAI_CONFIG_LIST` and update `OAI_CONFIG_LIST` with the OpenAI model information that you want to use, including API keys.
1. Copy `.env.sample` to `.env` and update the values as needed.
1. Open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) in VSCode and run `Remote-Containers: Reopen in Container`.
1. From the Terminal in VSCode, run:

    ```bash
    python app/app.py
    ```

1. Develop your AutoGen project!
