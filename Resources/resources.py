from os import error

emojis_dict = {
    'thumbs_up':    '\N{THUMBS UP SIGN}',
    'thumbs_down':  '\N{THUMBS DOWN SIGN}',
    'check':        '\N{WHITE HEAVY CHECK MARK}',
    'cross':        '❌',
    'skull':        '💀'
} 
 
msg_dict = {
    'game_name':    '>>> Bonjour! Quel est le nom du jeu ?',
    'cancel':       '>>> La session a été annulée.',
    'slots':        '>>> Combien de joueurs dans cette session ?',
    'time':         '>>> A quelle heure la session débutera ? (hh:mm)',
    'role':         '>>> Qui peut participer ? (Role ou pseudo si une seul personne)',
    'done':         '>>> La session est en cours de rédaction. Merci pour votre temps !'
}

error = {
    'event-not-found':    'Aucun évènement en cours. Vous pouvez en créer un nouveau avec la commande !planning' 
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