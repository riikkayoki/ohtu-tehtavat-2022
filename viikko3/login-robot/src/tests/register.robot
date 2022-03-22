*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Keywords ***
Create User And Input New Command
    Input New Command
    Create User  riikkayoki  kissa12345

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  risto  reipas123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  riikkayoki  kissa12345
    Input New Command
    Input Credentials  riikkayoki  kissa123456
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  r  kissa12345
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  riikkayoki  k
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  riikkayoki  kissakoira
    Output Should Contain  Password must contain at least one number
