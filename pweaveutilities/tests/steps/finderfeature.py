
# python standard library
import os

# third-party
from hamcrest import assert_that, is_, equal_to
from behave import given, when, then

# this package
from pweaveutilities.generators import  find

@given("a finder with a root set to a directory with one matching file(s)")
def step_implementation(context):
    context.finder = find("*.one", 'steps/findfiles')
    context.expected = ["steps/findfiles/this.one"]
    return

@when("the finder's outcome is checked")
def step_implementation(context):
    context.outcome = sorted([found for found in context.finder])
    return

@then("the finder's outcome matches the expected")
def step_implementation(context):
    assert_that(context.outcome,
                is_(equal_to(context.expected)))
    return

@given('a finder with a root set to a directory with no matching file(s)')
def no_matches(context):
    context.finder = find("*.none", 'steps/findfiles')
    context.expected = []
    return

@given('a finder with a root set to a directory with several matching file(s)')
def no_matches(context):
    context.finder = find("*.three", 'steps/findfiles')
    context.expected = [os.path.join('steps/findfiles/', filename) for filename in 'ape.three bonobo.three chimp.three'.split()]
    return

@given("a finder with a set of nested folders")
def nested_folders(context):
    context.finder = find('*.rst', 'steps/findfiles')
    context.expected = [ 'steps/findfiles/a_child/child.rst',
                         'steps/findfiles/b_child/child.rst',
                         'steps/findfiles/root.rst']
    return