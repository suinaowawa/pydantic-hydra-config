#  Pydantic + Hydra for config and CLI management

This Repo will show you how to easily create a CLI and config for your project with nice validation and a lot more!

## Install

1. Pull Repo

    ```console
    git clone https://github.com/suinaowawa/pydantic-hydra-config.git

    cd pydantic-hydra-config
    ```


2. Install Requirements

    Ensure Python **3.10** is used

    - Linux/mac
    ```console
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    - Windows cmd.exe

    ```console
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install -r requirements.txt
    ```

    - Windows PowerShell
    ```console
    python -m venv .venv
    .venv/Scripts/Activate.ps1
    pip install -r requirements.txt
    ```

    - Anaconda
    ```console
    conda create -n project python=3.10
    conda activate project
    pip install -r requirements.txt
    ```


3. Test Run

    ```console
    python hydra_example.py
    ```
    Check if script runs with default arguments.


## Run

To see and run [pydantic](https://docs.pydantic.dev/latest/) examples: check out `pydantic_example.ipynb` notebook!

To see and run [hydra](https://hydra.cc/) examples: check out `hydra_example.py` with `hydra_guide.md`!

**Happy Coding!!**

## References:

- Pydantic Documentations: https://docs.pydantic.dev/latest/
- Hydra Documentations: https://hydra.cc/
- Nice Blog on Pydantic+Hydra (Pydra): https://suneeta-mall.github.io/2022/03/15/hydra-pydantic-config-management-for-training-application.html