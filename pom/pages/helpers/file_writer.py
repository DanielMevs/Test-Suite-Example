def write_file(email: str, password: str) -> None:
    with open('../new_users/new_user.txt', 'w+') as f:
        f.write(email + '\n')
        f.write(password)