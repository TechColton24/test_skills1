# Making a simple login system
# If username and password is right - access granted
# If password or username or both are wrong - password denied.


test_username = 'testusername'
test_password = 'testpassword'
  

login_username = str(input('Enter Username: '))
if (login_username == test_username):
    login_password = str(input('Enter Password: '))
    if (login_password == test_password):
         print('Access Granted!')
    else:
      print('Try Again!')
      breakpoint
else:
  print('Try Again!')
  breakpoint
