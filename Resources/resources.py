from os import error

#commands
databaseSeparator='¤'
commandSign='!'
cancel='cancel'
planning='planning'
clear='clear'
help='help'
here='here'
set_channel='here'
unset_channel='nothere'
reset='reset'
next='next'

emojis_dict = {
    'thumbs_up':    '\N{THUMBS UP SIGN}',
    'thumbs_down':  '\N{THUMBS DOWN SIGN}',
    'check':        '\N{WHITE HEAVY CHECK MARK}',
    'cross':        '',
    'skull':        '💀'
} 
 
msg_dict = {
    'game_name':        '>>> Bonjour! Quel est le nom du jeu ?',
    'game_image':        '>>> I had no image for this game. Could you link one to me ? (or use the !pass commad to pass)',
    'cancel':           '>>> La session a été annulée.',
    'nothing_cancel':   '>>> Aucun session à annuler.',
    'slots':            '>>> Combien de joueurs dans cette session ?',
    'time':             '>>> A quelle heure la session débutera ? (hh:mm)',
    'role':             '>>> Qui peut participer ? (Role ou pseudo si une seul personne)',
    'done':             '>>> La session est en cours de rédaction. Merci pour votre temps !',
    'added':            '>>> You have been added to the session',
    'next':             '>>> The step have been passed'
}

button = {
    'cancel':   'cancel',
    'ok':       'I\'m in'
}

help = {
    'cancel':  'Défini le chan d\'acttion du bot. A configurer a chaque redémarage',
    'planning': 'Créer une session de jeu étape par étape (Non utilisable en MP)',
    'clear': 'Supprime tous les messages du bot',
    'cancel': 'Annule la session en cours de création',
    'next': 'Pass a step (usable when specify by bot)'
}

error = {
    'event-not-found':  '>>> Aucun évènement en cours. Vous pouvez en créer un nouveau avec la commande !planning',
    'not_here':         '>>> Cette commande n\'est utilisable que sur un serveur de jeu.',
    'not_next':         '>>> You can not pass any step.' 
}

msg_type = {
    'dm': 'private',
    'channel': 'text'
}

steps = {
    'done': -1,
    'none': 0,
    'init': 1,
    'game_name': 2,
    'game_image': 21,
    'slots': 3,
    'time': 4,
#    'role': 5
    }

