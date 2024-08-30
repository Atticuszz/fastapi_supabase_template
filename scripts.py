import subprocess


def run_cmd(cmd: str) -> None:
    subprocess.run(cmd, shell=True, check=True)


def run_tests() -> None:
    # Install requirements by poetry
    run_cmd("uv sync --all-extras --dev")

    # Run pre-commit tests
    # run_cmd("poetry run pre-commit autoupdate")
    # run_cmd("poetry run pre-commit clean")
    # run_cmd("poetry run pre-commit install")
    run_cmd("uv run pre-commit run --all-files")

    # Generate coverage report --cov=./ --cov-report=xml --cov-report=html -vv
    run_cmd("uv run pytest  --cov=./ --cov-report=xml --cov-report=html -vv")


if __name__ == "__main__":
    run_tests()
