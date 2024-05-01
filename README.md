# Genealogy Tree Application

This repository contains the code for a genealogy tree application developed using Python and Tkinter.

## Author

Lsnoglos

## Setting Up the Development Environment

Follow these steps to set up your development environment and run the application.

1. **Clone the repository and navigate to the project directory**:

    ```bash
    git clone https://github.com/lsnoglos/tree.git
    cd tree
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    python main.py
    ```

## Troubleshooting

### Issues with Tkinter Not Working

If you encounter issues with Tkinter not functioning correctly (e.g., ModuleNotFoundError: No module named 'tkinter'), follow these steps:

1. **Deactivate your virtual environment temporarily**:
   
    ```bash
    deactivate
    ```

2. **Update your package list and install `python3-tk`**:

    ```bash
    sudo apt update
    sudo apt install python3-tk
    ```

3. **Reactivate your virtual environment and try running the application again**:

    ```bash
    source venv/bin/activate
    python main.py
    ```

This will ensure that Tkinter is installed on your system and available for use within your virtual environment. If the problem persists, please check that your Python installation is configured correctly to include Tkinter.
