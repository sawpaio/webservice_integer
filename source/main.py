from aiohttp import web
import json
from files.numerosromanos.source.int2roman_lucas import roman_number
from files.valida_cpf.source.validacpf_lucas import CPFvalidator
from files.distancia_entre_zeros.source.count_zeros_lucas import Count_zeros
from files.generate_passwords.source.generate_password_lucas import random_pass
from files.classificador_senhas.source.classificador_senhas_lucas import Classifica
from files.encryption_password.source.encrypto_password import crypto_pass

async def getRoman(request):
    response_obj = roman_number.keyboard2roman(request.match_info['string'])
    return web.Response(text=json.dumps(response_obj))
    
async def getValidaCPF(request):
    response_obj = CPFvalidator.valida_cpf(request.match_info['string'])
    return web.Response(text=json.dumps(response_obj))

async def getDistanciadeZeros(request):
    response_obj = Count_zeros.zeros_count(request.match_info['string'])
    return web.Response(text=json.dumps(response_obj))

async def getGeradordeSenhas(request):
    response_obj = random_pass()
    response_obj2 = Classifica.classifica_senha(response_obj)
    response_obj3 = crypto_pass.hash_md5(response_obj2)

    return web.Response(text=json.dumps({'senha gerada:': response_obj,
                                         'força da senha:': response_obj2,
                                         'hash_MD5 da senha:': response_obj3}))

app = web.Application()
app.router.add_get("/roman/{string}", getRoman)
app.router.add_get("/valida_cpf/{string}", getValidaCPF)
app.router.add_get("/dist_zeros/{string}", getDistanciadeZeros)
app.router.add_get("/gera_senha/", getGeradordeSenhas)
web.run_app(app, host='localhost', port=7777)