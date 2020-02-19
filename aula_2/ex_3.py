# identificar se e-mail esta correto

#email = input("Digite seu e-mail: ")

emails = [
	'petyfezygniyg@msddvqiytmpogire',
	'yjozbkgirsfchbjtlnigqqeohaj',
	'axukkfdcpemkruogaemqlcyfngun',
	'czmymzvhdyfltqe@rktzjljbs',
	'@yoeisikhawyno@b',
	'dfeydhfnlydwrlvpmsomi',
	'xogsqaxph@btippxiz',
	'hxkuqlyxreuwfzwypvw',
	'togaczelhzijnafhyg@czp@f',
	'jxtmqikapfv@uqqckowiz@hyi',
]
# print(email)
for email in emails:
    num = 0
    for letra in email:
        if letra in "@":
            #print("Digitou um numero")
            num = num + 1
    if num == 1:
        print("Este e e-mail valido: ", num)
    else:
        print("Este e e-mail invalido", num)