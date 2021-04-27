import requests
import time


# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)
    time.sleep(6) # o timeoutresolve o problema


try:
    resp = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.Timeout:
    resp = requests.get("http://httpbin.org/delay/1", timeout=2)
finally:  
    print(resp.status_code)

