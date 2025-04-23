from behave import given
@given('I reach office at "{time}" shift')
@given('llego a la oficina en el turno "{time}"')
def step_impl(context, time):
    assert time != "tarde", "Invalid period of time"
    print("Shift is: {}".format(time))
#Esto es una prueba