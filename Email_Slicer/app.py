email = input("enter a email").strip()
if '@' in email:
  username = email[:email.index('@')]
  domain = email[email.index('@')+1:]
  
  print(f"your user name {username} \ndomain name is  {domain}")
  
else:
  print("invalid email please enter a valid email address....")
  