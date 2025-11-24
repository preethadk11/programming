emails=["alice@example.com","bob@test.org","carol@sample.net"]
username=[email.split("@")[0] for email in emails]
print(username)