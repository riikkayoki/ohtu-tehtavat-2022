*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  riikkayoki
    Set Password  kissa123456
    Set Password confirmation  kissa123456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  r
    Set Password  kissa1234
    Set Password confirmation  kissa1234
    Submit Credentials
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  riikkayoki123
    Set Password  ki
    Set Password confirmation  ki
    Submit Credentials
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  riikkayoki1234
    Set Password  kissa123456
    Set Password confirmation  koira123456
    Submit Credentials
    Registration Should Fail With Message  Passwords must match

Login After Successful Registration
    Go To Login Page
    Set Username  riikkayoki
    Set Password  kissa123456
    Submit Login Credentials
    Login Should Succeed
    Go To Login Page

Login After Failed Registration
    Go To Login Page
    Set Username  riikkayoki1234
    Set Password  kissa4568
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}