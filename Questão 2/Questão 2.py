import threading

def FormandosAdm():
    with open('content/Administração.txt', 'r', encoding='utf-8') as fileAdm:
        linhas = fileAdm.readlines()

        for linha in linhas:
            if 'Concluído' in linha:
                print(linha)

def FormandosArq():
    with open('content/Arquitetura.txt', 'r', encoding='utf-8') as fileArq:
        linhas = fileArq.readlines()

        for linha in linhas:
            if 'Concluído' in linha:
                print(linha)

def FormandosComputação():
    with open('content/Ciência da Computação.txt', 'r', encoding='utf-8') as fileComp:
        linhas = fileComp.readlines()
        for linha in linhas:
            if 'Concluído' in linha:
                print(linha)

def FormandosDireito():
  with open('content/Direito.txt', 'r', encoding='utf-8') as fileDir:
      linhas = fileDir.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosEducaçãoFísica():
  with open('content/Educação Física.txt', 'r', encoding='utf-8') as fileEduFis:
      linhas = fileEduFis.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosEngenhariaCivil():
  with open('content/Engenharia Civil.txt', 'r', encoding='utf-8') as fileEngCivil:
      linhas = fileEngCivil.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosEngenhariadaComputação():
  with open('content/Engenharia da Computação.txt', 'r', encoding='utf-8') as fileEngComp:
      linhas = fileEngComp.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosEngenhariaElétrica():
  with open('content/Engenharia Elétrica.txt', 'r', encoding='utf-8') as fileEngEle:
      linhas = fileEngEle.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosEngenhariaMecânica():
  with open('content/Engenharia Mecânica.txt', 'r', encoding='utf-8') as fileEngMec:
      linhas = fileEngMec.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosMedicinaVeterinária():
  with open('content/Medicina Veterinária.txt', 'r', encoding='utf-8') as fileMedVet:
      linhas = fileMedVet.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosMedicina():
  with open('content/Medicina.txt', 'r', encoding='utf-8') as fileMed:
      linhas = fileMed.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosNutrição():
  with open('content/Nutrição.txt', 'r', encoding='utf-8') as fileNutri:
      linhas = fileNutri.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosPsicologia():
  with open('content/Psicologia.txt', 'r', encoding='utf-8') as filePsico:
      linhas = filePsico.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosQuímica():
  with open('content/Química.txt', 'r', encoding='utf-8') as fileQuim:
      linhas = fileQuim.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

def FormandosRelaçõesInternacionais():
  with open('content/Relações Internacionais.txt', 'r', encoding='utf-8') as fileRelInt:
      linhas = fileRelInt.readlines()
      for linha in linhas:
          if 'Concluído' in linha:
              print(linha)

# Criando as threads
thread1 = threading.Thread(target=FormandosAdm)
thread2 = threading.Thread(target=FormandosArq)
thread3 = threading.Thread(target=FormandosComputação)
thread4 = threading.Thread(target=FormandosDireito)
thread5 = threading.Thread(target=FormandosEducaçãoFísica)
thread6 = threading.Thread(target=FormandosEngenhariaCivil)
thread7 = threading.Thread(target=FormandosEngenhariadaComputação)
thread8 = threading.Thread(target=FormandosEngenhariaElétrica)
thread9 = threading.Thread(target=FormandosEngenhariaMecânica)
thread10 = threading.Thread(target=FormandosMedicinaVeterinária)
thread11 = threading.Thread(target=FormandosMedicina)
thread12 = threading.Thread(target=FormandosNutrição)
thread13 = threading.Thread(target=FormandosPsicologia)
thread14 = threading.Thread(target=FormandosQuímica)
thread15 = threading.Thread(target=FormandosRelaçõesInternacionais)



# Iniciando as threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()

# Aguardando a finalização das threads
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread10.join()
thread11.join()
thread12.join()
thread13.join()
thread14.join()
thread15.join()

print("Processamento concluído!")


