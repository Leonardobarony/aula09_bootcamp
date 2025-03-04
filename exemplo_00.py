#from loguru import logger
from sys import stderr
#from functools import wraps
from timer_docarator import time_measure_decorator
import time

# def soma(x,y):
#     try:
#         soma = x + y
#         logger.info(f"voce digitou valores corretos, parabens {soma}")
#         return soma
#     except:
#         logger.critical("voce tem digitar valor incorreto")
@time_measure_decorator
def soma(x,y):
    time.sleep(2)
    soma = x + y
    return soma


soma(2,3)

soma(2,7)

soma(15.5,25.8)
