# Alternative Dockerfile approach (optional)
FROM mcr.microsoft.com/devcontainers/python:3.10

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/vscode/.bashrc \
    && echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/vscode/.zshrc

# Configure Poetry
RUN /home/vscode/.local/bin/poetry config virtualenvs.create true \
    && /home/vscode/.local/bin/poetry config virtualenvs.in-project false

USER vscode
