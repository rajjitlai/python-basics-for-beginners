# Mail Merge Program

with open("Users.txt", "r") as Users:
    with open("Info.txt", "r") as Body:
        info = Body.read()

        for user in Users:
            msg = "Greetings " + user + " " + info # Greetings Tomba Hello!!

            with open(user.strip() + ".txt", "w") as Mail:
                Mail.write(msg)
