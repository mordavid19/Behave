from behave import *

# def payment_info_and_submits(context):
#     context.execute_steps(u"""
#     Given User is on payment screen 
#     When User enters payment details 
#     And User completes payment
#     """)

@given('launch application')
def launch_application(context):
    print('launch application')

@then('Input credentials')
def input_credentials(context):
    print('Input credentials')

@given('user is on credit card payment screen')
def credit_card_pay(context):
    print('User is on credit card payment screen')

@then('user should be able to complete credit card payment')
def credit_card_pay_comp(context):
    print('user should be able to complete credit card pay')

@given('user is on debit card payment screen')
def debit_card_pay(context):
    print('User is on debit card payment screen')

@then('user should be able to complete debit card payment')
def debit_card_pay_comp(context):
    print('user should be able to complete debit card pay')
