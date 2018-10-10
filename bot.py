import telepot

bot = telepot.Bot("670067772:AAECWzTTeHmamjoyCClLKIqXjWyaHv6a5Bk")
msg = bot.getUpdates()
#msg é uma lista, acessa o ultimo item lista que é um dicionario com outros dicionarios dentro dele.
#e msg é a chave para acessar o dicionario que contém a última mensagem e dentro deste dic.temos a chave text que retorna a utltima mensagem.
#print(msg[-1]['message']['text'])

palavras = ["poesia", "poema", "ode", "trova"]



def recebendoMSG(msg):
        poema = '''Gentileza regrada do meu entendimento.
O tempo que eu vou chamar ser hoje sem sentido nenhum.Rendez-me presente do rio,
Os corpos de todas as coisas serem assim, assim, muitas vezes tudo e contigo,
E com muitos casos duvidosos, Mas falta-me os carros monotonos e dos armados,
Mas o faco escuro de Milton onde estao a mim. Nao sei que meu coracao a ti aberto! Como a salva da casa, a sorte deus longinquo respiraremos a beira-mar so com a sensacao de a sociedade livre; mas o que se sente
E a tua mao movida por grandes cores, Com as almas e nos seus amores, Nos ares atras de si e viver. So assim, o noite, e eu nao sinto
Que a perda de mim a senhora, que e a que pode haver dias so de tedio, como se estivesse sonhadas,
A consciencia de ter medo de que nao pudesse ? a inteligencia de que a vida
Passa por cima do muro da quinta, toda a vida.
Tudo passo e contar o que sinto,
Que eu quero sentir tudo de todas as maneiras,
Com o poder de ser assim e que eu nao sinto.
Nada pode ser que seja possivel
ter pena'''
        mensagem = msg['text']
        for p in palavras:
            if p in mensagem:
                bot.sendMessage(msg['from']['id'],poema)

     
bot.message_loop(recebendoMSG)



while True:
     #pass
     texto = input()
     bot.sendMessage(681421692,texto)
  




#https://www.youtube.com/watch?v=2TCkaJdcicQ
