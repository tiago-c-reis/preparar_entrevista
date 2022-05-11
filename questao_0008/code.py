# Prepare a sua entrevista -- Python
# https://youtube.com/c/AutomationDataScience

# Desafio:
#     Crie uma função que retorne a palavra com mais caracteres a partir de
#     uma frase utilizada como argumento.

#     Vídeo-Desafio: https://youtube.com/shorts/5AiVkpakq1s

import re


def test(frase):
    palavras = [re.sub(r'[\W]', '', p) for p in re.split(r'\s', frase)]

    return max(palavras, key=len)


# -- Testes
rsp = test('08:00 am: Aprenda Python!')
print(rsp)

rsp = test('O que achou difícil?')
print(rsp)

