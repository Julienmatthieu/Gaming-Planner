from os import error

#commands
commandSign='!'
cancel='cancel'
planning='planning'
clear='clear'
help='help'
here='here'
set_channel='here'
unset_channel='nothere'
reset='reset'

emojis_dict = {
    'thumbs_up':    '\N{THUMBS UP SIGN}',
    'thumbs_down':  '\N{THUMBS DOWN SIGN}',
    'check':        '\N{WHITE HEAVY CHECK MARK}',
    'cross':        '❌',
    'skull':        '💀'
} 
 
msg_dict = {
    'game_name':        '>>> Bonjour! Quel est le nom du jeu ?',
    'cancel':           '>>> La session a été annulée.',
    'nothing_cancel':   '>>> Aucun session à annuler.',
    'slots':            '>>> Combien de joueurs dans cette session ?',
    'time':             '>>> A quelle heure la session débutera ? (hh:mm)',
    'role':             '>>> Qui peut participer ? (Role ou pseudo si une seul personne)',
    'done':             '>>> La session est en cours de rédaction. Merci pour votre temps !',
    'added':            'You have been added to the session'
}

help = {
    'cancel':  'Défini le chan d\'acttion du bot. A configurer a chaque redémarage',
    'planning': 'Créer une session de jeu étape par étape (Non utilisable en MP)',
    # TO DO PARAM
#        \n\t{com.commandSign}{com.planning}-GameName-NombreDeJoueurs-Date-Role pour créer une session en une seule commande (Non utilisable en MP)\
    'clear': 'Supprime tous les messages du bot',
    'cancel': 'Annule la session en cours de création'
}
#        \n\t{com.commandSign}{com.cancel}:  \
#        \n\t  **Ce bot est actuellement en cours de dévelopement. Pour tout feedback ou idée n\' hésitez pas à contacter Stalingrad#9674**')

error = {
    'event-not-found':  '>>> Aucun évènement en cours. Vous pouvez en créer un nouveau avec la commande !planning',
    'not_here':         '>>> Cette commande n\'est utilisable que sur un serveur de jeu.'   
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
    'slots': 3,
    'time': 4,
    'role': 5
    }

