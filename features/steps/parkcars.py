from behave import *
from CarParks.carpark import Carpark

@given(u'an empty car park')
def step_impl(context):
    car_park = Carpark(5)



@when(u'a car with a reg number of "abc" enters the car park')
def step_impl(context):
    assert True


@then(u'a car with a reg number of "abc" should occupy a space in the car park')
def step_impl(context):
    assert True


@given(u'a carpark that holds a car with the reg number "abc"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a carpark that holds a car with the reg number "abc"')


@when(u'a second car with the reg number "abc" tries to enter the carpark')
def step_impl(context):
    assert False


@then(u'only one car with the reg number "abc" should occupy a space in the car park')
def step_impl(context):
    assert False



