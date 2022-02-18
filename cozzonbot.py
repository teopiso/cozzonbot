#!/usr/bin/env python3.8


import logging
import random
import instaloader
import os, re
import instamod, web
import phdra_radar

from datetime import datetime
from telegram import Update, chatmember, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import telegram

dir_path = os.path.dirname(os.path.realpath(__file__))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Mi dica', quote = False)

def help_command(update: Update, context: CallbackContext) -> None:
    """Chiedi un aiuto al cozzone"""
    update.message.reply_text('Chieda a patollo, l\'ha fatto lui il bot python', quote = False)

class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():                   
            if item in key:                       
                return super().__getitem__(key)   
        raise KeyError(item)
    
def incagnometro(update: Update, context: CallbackContext) -> None:
    """il cozzone ti dice quanto sei incagnato"""
    x=random.randrange(0, 121)
    y=str(x)
    user = update.message.from_user
    switch = Switch({
    range(0, 1): 'Lei signor '+str(user['username']) +' non è per nulla incagnato.\nRilevo un livello di '+y+'/100.\nStia tranquillo, tra poco le passerà',
    range(1, 31): 'Una leggera incagnatura signor '+str(user['username']) +', rilevo '+y+'/100.\nTutto nella norma!',
    range(31, 61): 'L\'incagnatura sta salendo '+str(user['username']) +'\nI sensori di parcheggio della phedra misurano '+y+'/100.',
    range(61, 91): 'Ma lei '+str(user['username']) +' si incagna subito figa!\nL\'incagnatura sta a '+y+'/100.',
    range(91,100):'Tutti nel bunker!!!!!\nIncagnatura di '+str(user['username']) +' a '+y+'/100.\nSi salvi chi può.',
    range(100,121):str(user['username']) +' INCAGNATURA MASSIMA. ABBANDONARE LA NAVE RIPETO ABBADONARE LA NAVE',
    })
    update.message.reply_text(switch[x], quote = False)

def cit(update: Update, context: CallbackContext) -> None:
    '''il cozzone ti manda una sua cit causale'''
    cit = os.path.join(dir_path, "chat/cit.txt")
    frcit = open(cit, encoding="utf8")
    x = random.randrange(0,14476)
    for i, line in enumerate(frcit):
        if i == x:
            update.message.reply_text(line, quote = False)
            break
    frcit.close()

def tag(update: Update, context: CallbackContext) -> None:
    '''il cozzone cita la frase inserita dopo il comando in una frase, se non c'è lui chiede e basta'''
    tag = os.path.join(dir_path, "chat/tag.txt")
    frtag = open(tag, encoding="utf8")
    x = random.randrange(0,660)
    text = update.message.text.split()
    if len(text) <= 1 :
        update.message.bot.send_photo(update.message.chat.id,open('img/chiedo.jpeg','rb'))
    else:
        for i, line in enumerate(frtag):
            if i == x:
                res = line.replace("@" , text[1])
                update.message.reply_text(res, quote = False)
                break
    frtag.close()

def pupilla(update: Update, context: CallbackContext) -> None:
    target=instamod.download_post()
    res='id'
    
    while res == 'id':
        res=random.choice(os.listdir(dir_path+"/ig/"+target+"/"))
    dires=dir_path+"/ig/"+target+"/"+res
    print(str(datetime.today())+' pupilla richiesta da: '+str(update.message.from_user))
    text = update.message.text.split()
    if len(text) <= 1 :
        update.message.bot.send_photo(update.message.chat.id,open(dires,'rb'),caption='un parere?')
    else:
        tag = os.path.join(dir_path, "ig/risposte.txt")
        frreply = open(tag, encoding="utf8")
        x = random.randrange(0,8)
        for i, line in enumerate(frreply):
            if i == x:
                res = line.replace("@" , text[1])
                update.message.bot.send_photo(update.message.chat.id,open(dires,'rb'),caption=res)
        frreply.close()

def getitinerario(update: Update, context: CallbackContext) -> None:
    text = update.message.text.split(" - ")
    text[0]=text[0].replace("/percorso","")
    print(str(datetime.today())+' percorso richiesto da: '+str(update.message.from_user)+'\ntext: '+str(update.message.text))
    if len(text)>=2:
        update.message.reply_text('Aspe che calcolo il costo e il percorso del viaggio...', quote = False)
        res=web.get(str(text[0]),str(text[1]))
        #update.message.reply_text(res, quote = False)
        update.message.bot.send_photo(update.message.chat.id,open(dir_path+'/screenshot.png','rb'),caption=res)
    else:
        user = update.message.from_user
        update.message.reply_text('non faccia lo spiritoso signor '+str(user['username']), quote = False)

def sigode(update: Update, context: CallbackContext) -> None:
    '''si gode, è scritto così per fare dei test, dovrebbe funzionare anche normalmente'''
    update.message.bot.send_message( update.effective_chat.id ,'E si godeeee')

def malato(update: Update, context: CallbackContext) -> None:
    '''e me ne vanto'''
    update.message.bot.send_message( update.effective_chat.id ,'E me ne vanto')

def insulta(update: Update, context: CallbackContext) -> None:
    '''indignato'''
    l=['E insulta','Non c\'è più rispetto','Solo quello sai dire','E insulta','Ha parlato il pagliaccio']
    update.message.bot.send_message( update.effective_chat.id ,random.choice(l))

def godo(update: Update, context: CallbackContext) -> None:
    '''gode'''
    l=['Godo!','Godo merda', 'Quanto godo', 'GODO', 'Godemos', 'Si gode?!', 'è qui che si gode?', 'Posso godere?','Il godimento è ai massimi storici','Che sborrata', 'Bravo coglione']
    update.message.bot.send_message( update.effective_chat.id ,random.choice(l))

def lol(update: Update, context: CallbackContext) -> None:
    '''sisiridi'''
    l=['Sisi ridi coglione','Cazzo ridi','Hanno aperto il circo che ridi?','Fa ridere come te', 'Ridi pagliaccio','Pensa pure di essere simpatico']
    update.message.bot.send_message( update.effective_chat.id ,random.choice(l))

def A_graziecapitano(update: Update, context: CallbackContext) -> None:
    update.message.bot.send_audio(update.message.chat.id, audio=open(dir_path+'/audio/grazieperilcapitano.ogg', 'rb'))

def A_sium(update: Update, context: CallbackContext) -> None:
    update.message.bot.send_audio(update.message.chat.id, audio=open(dir_path+'/audio/sium.ogg', 'rb'))

def A_eredita(update: Update, context: CallbackContext) -> None:
    update.message.bot.send_audio(update.message.chat.id, audio=open(dir_path+'/audio/eredita.ogg', 'rb'))

def A_sveglia(update: Update, context: CallbackContext) -> None:
    update.message.bot.send_audio(update.message.chat.id, audio=open(dir_path+'/audio/sveglia.ogg', 'rb'))

def gaglia(update: Update, context: CallbackContext) -> None:
    res='video'
    if random.randrange(0,10) > 3:
        while res == 'video':
            res=random.choice(os.listdir(dir_path+"/ig/gagliardini/"))
        dires=dir_path+"/ig/gagliardini/"+res
        update.message.bot.send_photo(update.message.chat.id,open(dires,'rb'))
    else:
        vid = os.path.join(dir_path, "ig/gagliardini/video.txt")
        frvid = open(vid, encoding="utf8")
        x = random.randrange(0,20)
        for i, line in enumerate(frvid):
            if i == x:
                update.message.reply_text(line, quote = False)
                break
        frvid.close()

def lory(update: Update, context: CallbackContext) -> None:
    update.message.bot.send_photo(update.message.chat.id,open(dir_path+'/img/lory.jpg','rb'))

def quotaphedra(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('https://paypal.me/pools/c/8wyEn1cfpx', quote = False)
    
def get_meme(update: Update, context: CallbackContext) -> None:
    res=random.choice(os.listdir(dir_path+"/img/meme/"))
    dires=dir_path+"/img/meme/"+res
    update.message.bot.send_photo(update.message.chat.id,open(dires,'rb'))

def start_notify(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    if not current_jobs:
        update.message.reply_text('Il phedrone-sommergibile inizia a scandagliare il fondale in cerca di nuovi relitti', quote = False)
        chat_id = update.message.chat_id
        new_job = context.job_queue.run_repeating(comment_update, interval=300, first=1, context=chat_id, name=str(chat_id))
    else:
        update.message.reply_text('Il phedrone-sommergibile è già in viaggio', quote = False)



def stop_notify(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    if not current_jobs:
        update.message.reply_text('Il phedrone-sommergibile è già parcheggiato', quote = False)
        return
    update.message.reply_text('Il phedrone-sommergibile riemerge dagli abissi e torna al molo', quote = False)
    job = context.job_queue.get_jobs_by_name(str(chat_id))
    job[0].schedule_removal()

def comment_update(context):
    job= context.job
    data = phdra_radar.radar()
    if len (data) > 0 :
        for barcone in data:
            link = "http://autoscout24.it"+barcone["href"]
            string = "TITOLO: "+barcone["title"]+"\nPREZZO: "+barcone["price"]+"\nKM: "+barcone["km"]+"\nANNO: "+barcone["year"]+"\nLUOGO: "+barcone["place"]
            context.bot.send_message(job.context, text="!NUOVO BARCONE TOVATO!\n\n"+string+"\n\n <a href='"+link+"'>COMPRAMI SUBITO</a>", parse_mode=telegram.ParseMode.HTML)

def si_scherza(update: Update, context: CallbackContext):
    dires = dir_path+"/img/meme/sischerza.jpg"
    update.message.bot.send_photo(update.message.chat.id,open(dires,'rb'))


def main():
    """cozzonbot start"""
    updater = Updater("1673561309:AAG7kKGyZuXnHptmoGv1Jxt4gKmzqbGCAtE", use_context=True)

    dispatcher = updater.dispatcher

    #comandi 
    dispatcher.add_handler(CommandHandler("wakeup", start))
    dispatcher.add_handler(CommandHandler("aiutino", help_command))
    dispatcher.add_handler(CommandHandler("incagnometro", incagnometro))
    dispatcher.add_handler(CommandHandler("cit", cit))
    dispatcher.add_handler(CommandHandler("chiedo", tag))
    dispatcher.add_handler(CommandHandler("pupilla", pupilla))
    dispatcher.add_handler(CommandHandler("percorso", getitinerario))
    dispatcher.add_handler(CommandHandler("donazioni", quotaphedra))
    dispatcher.add_handler(CommandHandler("sveglia", A_sveglia))
    dispatcher.add_handler(CommandHandler("meme", get_meme))
    dispatcher.add_handler(CommandHandler("start", start_notify, pass_job_queue=True))
    dispatcher.add_handler(CommandHandler("stop", stop_notify, pass_job_queue=True))

    #comandi triggerati da testo
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'Wa*rzo*na*ta',re.IGNORECASE)), sigode))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'cit',re.IGNORECASE)), cit))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(malat(.*))\b',re.IGNORECASE)), malato))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(coglion(.*)|bastard(.*)|puttan(.*)|troi(.*)|pagliac(.*)|circo|stronz(.*))\b',re.IGNORECASE)), insulta))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(non.*?sto.*?ben(.*)|perso(.*)|vint(.*)|vinc(.*)|non ci.*?s|sto mal(.*)|ammal(.*))\b',re.IGNORECASE)), godo))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(ringraziam.*?capitano|grazi.*?carletto|ringraziam.*?carletto)\b',re.IGNORECASE)), A_graziecapitano))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r's([i]+)([u]+)m',re.IGNORECASE)), A_sium))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(lo.*?l|kek|xd|aha.*?|hah.*?)\b',re.IGNORECASE)), lol))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'gagli',re.IGNORECASE)), gaglia))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(lori|lory|panchetta|divan(.*))\b',re.IGNORECASE)), lory))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'quota',re.IGNORECASE)), quotaphedra))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(eredità|eredita)\b',re.IGNORECASE)), A_eredita))
    dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\b(?<!@)(si scherza|scherzando|in goliardia)\b',re.IGNORECASE)), si_scherza))
    

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
