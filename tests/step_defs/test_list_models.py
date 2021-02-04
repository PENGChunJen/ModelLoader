# coding=utf-8
"""List All Models feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/list.feature', 'List available models')
def test_list_available_models():
    """List available models."""


@given('the user use the modelloader cli tool')
def the_user_use_the_modelloader_cli_tool():
    """the user use the modelloader cli tool."""
    raise NotImplementedError


@when('the user type model --list command')
def the_user_type_model_list_command():
    """the user type model --list command."""
    raise NotImplementedError


@then('the cli tool print all available models on terminal')
def the_cli_tool_print_all_available_models_on_terminal():
    """the cli tool print all available models on terminal."""
    raise NotImplementedError

