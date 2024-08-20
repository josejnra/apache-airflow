#!/bin/bash

poetry install

poetry update

/bin/bash .devcontainer/vscode_settings.sh
