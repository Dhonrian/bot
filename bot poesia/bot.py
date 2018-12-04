#from __future__ import print_function

import argparse
import os
from six.moves import cPickle




from six import text_type





parser = argparse.ArgumentParser(
                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--save_dir', type=str, default='save',
                    help='model directory to store checkpointed models')
parser.add_argument('-n', type=int, default=500,
                    help='number of characters to sample')
parser.add_argument('--prime', type=text_type, default=u'',
                    help='prime text')
parser.add_argument('--sample', type=int, default=1,
                    help='0 to use max at each timestep, 1 to sample at '
                         'each timestep, 2 to sample on spaces')

args = parser.parse_args()

import telepot
import tensorflow as tf
from model import Model



bot = telepot.Bot("670067772:AAECWzTTeHmamjoyCClLKIqXjWyaHv6a5Bk")
msg = bot.getUpdates()
#msg é uma lista, acessa o ultimo item lista que é um dicionario com outros dicionarios dentro dele.
#e msg é a chave para acessar o dicionario que contém a última mensagem e dentro deste dic.temos a chave text que retorna a utltima mensagem.
#print(msg[-1]['message']['text'])

palavras = ["poesia", "poema", "ode", "trova"]

start = '''Olá eu sou o Bot de Poesia, fui treinado com poemas de Machado de Assis e Fernando Pessoa.
Para receber um poema, escreva uma frase que contenha as palavras:
Ode, Trova, Poema ou Poesia'''

def sample(args):
    tf.reset_default_graph() 
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    #Use most frequent char if no prime is given
    if args.prime == '':
        args.prime = chars[0]
    model = Model(saved_args, training=False)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            data = model.sample(sess, chars, vocab, args.n, args.prime,
                               args.sample).encode('utf-8')
            poema = data.decode('utf-8')
            return poema


def recebendoMSG(msg):
    mensagem = msg['text'].lower()
    id_chat = msg['from']['id']
    palavra = 0    

    if mensagem == "/start":
            bot.sendMessage(id_chat, start)

    for p in palavras:
        if p in mensagem:
            text = sample(args)
            bot.sendMessage(id_chat, text)
            palavra = 1

    if palavra == 0 and mensagem != "/start" :
        bot.sendMessage(id_chat, "Comando nao reconhecido")
    
bot.message_loop(recebendoMSG)







