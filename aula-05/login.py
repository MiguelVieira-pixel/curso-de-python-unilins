def login(Puser, Ppassword):
    loggeds_users = {
        'admin': '1234',
        'beji': '123',
        'aluno': 'unilins'
    }

    if Puser in loggeds_users and loggeds_users[Puser] == Ppassword: #verifica o usuário e a senha
        return True
    else:
        return False
