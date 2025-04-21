.PHONY: all venv install clean fclean re exe

PYTHON = python3
VENV = venv
VENV_BIN = $(VENV)/bin
PIP = $(VENV_BIN)/pip
PYTHON_VENV = $(VENV_BIN)/python
PROGRAM_NAME = computor
SRCS = srcs/

all: exe
	@echo "Program $(PROGRAM_NAME) is ready to use!"

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

exe: install
	chmod +x $(SRCS)/main.py
	@echo '#!/bin/bash' > $(PROGRAM_NAME)
	@echo '' >> $(PROGRAM_NAME)
	@echo '# Get the directory where this script is located' >> $(PROGRAM_NAME)
	@echo 'SCRIPT_DIR="$$( cd "$$( dirname "$${BASH_SOURCE[0]}" )" && pwd )"' >> $(PROGRAM_NAME)
	@echo '' >> $(PROGRAM_NAME)
	@echo '# Check if venv exists, if not, create it' >> $(PROGRAM_NAME)
	@echo 'if [ ! -d "$$SCRIPT_DIR/venv" ]; then' >> $(PROGRAM_NAME)
	@echo '    echo "Setting up virtual environment..."' >> $(PROGRAM_NAME)
	@echo '    cd "$$SCRIPT_DIR" && make install' >> $(PROGRAM_NAME)
	@echo 'fi' >> $(PROGRAM_NAME)
	@echo '' >> $(PROGRAM_NAME)
	@echo '# Run the program using the Python from the virtual environment' >> $(PROGRAM_NAME)
	@echo '"$$SCRIPT_DIR/venv/bin/python" "$$SCRIPT_DIR/$(SRCS)main.py" "$$@"' >> $(PROGRAM_NAME)
	chmod +x $(PROGRAM_NAME)
	@echo "Executable created at ./$(PROGRAM_NAME)"

clean:
	rm -rf __pycache__
	rm -rf */__pycache__

fclean: clean
	rm -rf $(VENV)
	rm -f $(PROGRAM_NAME)

re: fclean all

help:
	@echo "Available targets:"
	@echo "  all        : Create the executable program (default)"
	@echo "  venv       : Create virtual environment only"
	@echo "  install    : Create virtual environment and install dependencies"
	@echo "  exe        : Make main.py executable and create wrapper script"
	@echo "  clean      : Remove Python cache files"
	@echo "  fclean     : Remove all generated files including virtual environment"
	@echo "  re         : Clean everything and rebuild"
	@echo "  help       : Display this help message" 