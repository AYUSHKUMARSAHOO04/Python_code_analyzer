import pylint.lint
import flake8.main.application
import tempfile
import os

def analyze_code(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
        temp_file.write(code.encode('utf-8'))
        temp_file.flush()

        pylint_results = run_pylint(temp_file.name)
        flake8_results = run_flake8(temp_file.name)

    os.unlink(temp_file.name)
    return pylint_results + flake8_results

def run_pylint(file_path):
    pylint_opts = [file_path]
    pylint_output = pylint.lint.Run(pylint_opts, do_exit=False)
    return pylint_output.linter.reporter.data

def run_flake8(file_path):
    flake8_app = flake8.main.application.Application()
    flake8_app.initialize([file_path])
    flake8_app.run_checks()
    flake8_app.report()
    return flake8_app.formatter.results