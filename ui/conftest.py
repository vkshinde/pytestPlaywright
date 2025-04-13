import allure
import pytest


@pytest.hookimpl
def pytest_bdd_before_scenario(request, feature, scenario):
    print(f"Starting scenario: {scenario.name}")

@pytest.hookimpl
def pytest_bdd_after_scenario(request, feature, scenario):
    print("Allure dir After scenario")

@pytest.hookimpl
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step failed: {step.name}")
    print(f"Error: {exception}")
