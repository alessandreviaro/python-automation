import pyautogui
from time import sleep
pyautogui.PAUSE = 1

# Entrar no navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')    

# Entrar no site desejado
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)    
pyautogui.press('enter')

# fazer login da empresa(email)
sleep(3)
pyautogui.click(x=621, y=391)
pyautogui.write('edgaralessandre@gmail.com')

# fazer login da empresa(senha)
pyautogui.press('tab')
pyautogui.write('37353284')

# entrando no sistema
pyautogui.click(x=822, y=547)
sleep(2)  

# cadastar 1 produto
import pandas
data = pandas.read_csv("produtos.csv")

for linha in data.index:
    pyautogui.press('tab')
    codigo = data.loc[linha, 'codigo']
    pyautogui.write(codigo)

    # marca
    pyautogui.press('tab')
    marca = data.loc[linha, 'marca']
    pyautogui.write(marca)

    # tipo
    pyautogui.press('tab')
    tipo = data.loc[linha, 'tipo']
    pyautogui.write(tipo)
    
    # categoria
    pyautogui.press('tab')
    cate = data.loc[linha, 'categoria']
    pyautogui.write(str(cate))

    # preco unitaruio
    pyautogui.press('tab')
    preuni = data.loc[linha, 'preco_unitario']
    pyautogui.write(str(preuni))
    
    # custo
    pyautogui.press('tab')
    custo = data.loc[linha, 'custo']
    pyautogui.write(str(custo) )

    # obs
    pyautogui.press('tab')
    obs = data.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    # enviar
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.scroll(5000)




