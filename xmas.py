# Python 3.9.15
# Pandas 1.5.1

import random
import pandas as pd

participants = ['spencer',
                'kathryn',
                'elo',
                'preston',
                'corynn',
                'maddie',
                'adria',
                'connor',
                'abby',
                'simon',
                'kati',
                'mitchell',]

partners = {'spencer': 'kathryn',
            'kathryn': 'spencer',
            'preston': 'corynn',
            'corynn': 'preston',
            'maddie': 'adria',
            'adria': 'maddie',
            'connor': 'abby',
            'abby': 'connor',
            'simon': 'kati',
            'kati': 'simon',
            'mitchell': None,
            'elo': None
            }

recipients = participants.copy()


def do_christmas_magic(participants = participants, partners = partners, recipients = recipients):
    
    # random.seed(69420)  # lmao this random seed already produces a valid result

    self_matches = True
    spouse_matches = True
    duo_matches = True
    trio_matches = True

    while self_matches or spouse_matches or duo_matches or trio_matches:
    
        random.shuffle(recipients)

        # Cannot buy for yourself
        self_matches = any([participants[i] == recipients[i] for i in range(len(participants))])

        # Cannot buy for your spouse
        spouse_matches = any([partners[participants[i]] == recipients[i] for i in range(len(participants))])

        # Cannot have duos
        duos = pd.DataFrame({'buyer': participants, 'receiver': recipients})
        duo_matches = any([duos['buyer'][i] == duos['receiver'][duos.index[duos['buyer'] == duos['receiver'][i]].tolist()[0]] for i in range(len(participants))])

        # Cannot have trios
        trios = duos
        trio_matches = any(
            [trios['buyer'][i] == trios['receiver'][trios.index[\
                trios['buyer'] == trios['receiver'][trios.index[\
                    trios['buyer'] == trios['receiver'][i]]].tolist()[0]]].tolist()[0]\
                        for i in range(len(participants))]
        )

        if self_matches or spouse_matches or duo_matches or trio_matches:
            print('Invalid Result')
        else:
            print('Valid Result')

    return trios

if __name__ == '__main__':
    result = do_christmas_magic()
    print(result)
    