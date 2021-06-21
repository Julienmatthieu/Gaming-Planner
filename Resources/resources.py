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
    'game_name':        '>>> Hello ! What is the name of the ?',
    'game_image':       '>>> I had no image for this game. Could you link one to me ? (or use the !next commad to pass)',
    'cancel':           '>>> Game session had been canceled.',
    'nothing_cancel':   '>>> No game session to cancel.',
    'slots':            '>>> How many players ?',
    'time':             '>>> At what time will the session start ?',
    'done':             '>>> The session is being written. Thank you for your time !',
    'added':            '>>> You have been added to the session',
    'next':             '>>> The step have been passed'
}

button = {
    'cancel':   'cancel',
    'ok':       'I\'m in'
}

help = {
    'planning': 'Creat a new game session. You will need to allow DP from non friends on your discord settings. (Not usable in DM)',
    'clear':    'Delete all previous bot\'s posts',
    'cancel':   'Cancel the session that is being created',
    'next':     'Pass a step (usable when specify by bot)'
}

error = {
    'event-not-found':  '>>> No event found. You can create a new one using the !planning command',
    'not_here':         '>>> This command is not usable here. Use the !help command',
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

