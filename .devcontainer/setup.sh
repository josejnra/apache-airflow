#!/bin/bash

poetry install
poetry update
poetry self add poetry-plugin-shell
poetry self add poetry-plugin-export

/bin/bash .devcontainer/vscode_settings.sh
