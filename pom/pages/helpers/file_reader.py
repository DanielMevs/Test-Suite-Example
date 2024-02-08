def read_file() -> None:
    user_name = pass_word = ''

    with open('../new_users/new_user.txt', 'r+') as f:
        user_name, pass_word = f.read().split('\n')
    
    return user_name, pass_word