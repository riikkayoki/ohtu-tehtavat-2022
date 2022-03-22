*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Keywords ***
Create User And Input New Command
    Create User  riikkayoki  kissa123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  risto  reipas123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  riikkayoki  kissa123
    Output Should Contain  Username riikkayoki already exists

Register With Too Short Username And Valid Password
    Input Credentials  r  kissa123
    Output Should Contain  Username is too short, minimum length is 5

Register With Valid Username And Too Short Password
    Input Credentials  riksu  kissa1
    Output Should Contain  Password is too short, minimum length is 8

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  risto  reipas
    Output Should Contain  Password must contain at least one number
