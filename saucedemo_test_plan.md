# Saucedemo.com Test Plan
Testing UI login functionality for saucedemo.com 

## Test cases
### 1. Page info Validation
- goal: validate the connection is secure and title is right
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Check url protocol
    2. check page title
- expected result:
    - url protocol to be "https"
    - page title to be "Sauce Demo"
### 2. Username Field Validation
- goal: Validate username text box cannot be empty
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Leave username text box field empty without inserting any input
    2. Click on login button
- expected result: error box appears with informative message (username field cannot be empty) without any redirection to another page
### 3. Password Field Validation
- goal: Validate password text box cannot be empty
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Insert "my username" in the username text box field
    2. Leave password text box empty without inserting any input
    3. Click on login button
- expected result: error box appears with informative message (password field cannot be empty) without any redirection to another page
### 4. Login Success
- goal: Validate login with valid input
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Insert "standard_user" in the username text box field
    2. Insert "secret_sauce" in the password text box field
    3. Click on login button
- expected result: redirected to "www.saucedemo.com/inventory.html"
### 5. Login Failure
- goal: Validate unsuccessful login trial with invalid input
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Insert "standard_user" in the username text box field
    2. Insert "secret_sauce" in the password text box field
    3. Click on login button
- expected result: error box appears with informative message (invalid username or password) without any redirection to another page
### 6. Login Locked User
- goal: Validate unsuccessful login trial with locked user
- enviroment: Google Chrome browser
- prerequisites:
    - go to www.saucedemo.com
- steps:
    1. Insert "locked_out_user" in the username text box field
    2. Insert "secret_sauce" in the password text box field
    3. Click on login button
- expected result: error box appears with informative message (user is locked) without any redirection to another page