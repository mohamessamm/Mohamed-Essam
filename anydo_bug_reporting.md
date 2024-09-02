# Any.do Bugs
Bug report for Any.do IOS mobile application  

## Bugs
### 1. Email Address IS Not Validated
- reproducible steps:
    - open app
    - Click on email icon
    - Enter invalid email address "mohamed@blabla.oo"
    - Enter name "mohamed"
    - Enter password "123456"
- expected result: validating email address before registering and show an error message
- actual result: registering successfuly with invalid email address
- affected devices: iphone 13
- network: wifi
- severity: medium
- priority: medium
- impact: spamming database
### 2. Force Signing Out After Entering Incorrect Password
- reproducible steps (inconsistent): 
    - open app
    - sign in to your account
    - Click on three dot at the top right of the page
    - Click on Setting
    - Click on Profile under ACCOUNT
    - Click on pencil icon beside your email address to change the email
    - Change the email address
    - Click I'm sure on the confirmation box that will appear
    - Type incorrect password
    - Close the app
    - open the app again
- expected result: nothing happens and the app continue as it is
- actual result: after typing incorrect password your email address field will be empty and once you restart the app, you will be signed out and have to sign in again
- affected devices: iphone 13
- network: wifi
- severity: medium
- priority: medium
- impact: user exprience
### 3. Registeration Is Blocked After Entering Incorrect Password
- reproducible steps (inconsistent): 
    - open app
    - sign in to your account
    - click on three dot at the top right of the page
    - click on Setting
    - click on Profile under ACCOUNT
    - click on pencil icon beside your email address to change the email
    - change the email address
    - click I'm sure on the confirmation box that will appear
    - type incorrect password
    - sign out
    - register new account using email
- expected result: registering new account successfully
- actual result: after typing incorrect password your email address field will be empty and registeration will be blocked, you need to restart the app to resolve the issue
- affected devices: iphone 13
- network: wifi
- severity: low
- priority: low
- impact: users won't be able to register, they need to restart the app again
### 4. Changing Name Without Validation
- reproducible steps:
    - open app
    - sign in to your account
    - click on three dot at the top right of the page
    - click on Setting
    - click on Profile under ACCOUNT
    - click on pencil icon beside your name to change the name
    - type any characters "-"
- expected result: name invalid error message
- actual result: name changed successfuly
- affected devices: iphone 13
- network: wifi
- severity: low
- priority: low
### 5. Removing Task Without Confirming Or Undo Option
- reproducible steps:
    - open app
    - sign in to your account
    - write a task
    - click on the delete button beside the task to delete it
- expected result: either confirming deleting the task or undo option appear
- actual result: task item deleted without any confirmation or option to undo
- affected devices: iphone 13
- network: wifi
- severity: low
- priority: low
- impact: user experience, clicking on the delete icon by mistake
### 6. Error Messages Is Not Informative
- reproducible steps: try to enter any invalid input and wait for the error message
- expected result: informative error message
- actual result: always have one error "something went wrong" witout specifying the error
- affected devices: iphone 13
- network: wifi
- severity: medium
- priority: medium
- impact: user experience