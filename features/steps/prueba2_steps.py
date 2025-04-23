from behave import given, then

@given('user enters "{name}" and "{password}"')
def step_impl(context, name, password):
    print(f"Username for login: {name} *")
    print(f"Password for login: {password} *")
    context.username = name
    #context.password = password

@then('user should be logged in')
def step_impl(context):
    assert context.username != "admin", "Invalid username"
