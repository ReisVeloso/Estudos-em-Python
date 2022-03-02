import pyautogui
import time
i='sim'
listaEmail=[]
while i == 'sim':
    email = (input('Digite o email do destinatário: '))
    listaEmail.append(email)
    i = str(input('Deseja adicionar outro email? ')).strip().lower()
print(listaEmail)
listaEmail =' '.join(listaEmail)
print(listaEmail)
decisão1= str(input('Vamos enviar Email para esses contatos {} ?'.format(listaEmail))).strip().lower()

if decisão1 == 'sim':
    pyautogui.PAUSE = 2
    pyautogui.press('winleft')
    time.sleep(2)
    pyautogui.write('google')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('https://mail.google.com/mail/u/2/#inbox?compose=newgoogle')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(137, 198)  # Move o mouse p a posição falada e clica
    time.sleep(2)
    pyautogui.write(listaEmail) #digitar a lista de emails
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('Teste automação ')
    pyautogui.press('tab')
    pyautogui.write('Testando o Pyautogui')
    time.sleep(1)
    pyautogui.hotkey('ctrl','enter')
