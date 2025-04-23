from behave import given, when , then

@given('we have behave installed')
@given('tengo behave instalado')
def step_impl(context):
    pass



@when('we implement a test')
@when('implementamos una prueba')
def step_impl(context):
    assert True is not False
    
@then('behave will test it for us!')
@then('behave verifica que todo es ok!')
def  stop_impl(context):
    assert context.falled is False