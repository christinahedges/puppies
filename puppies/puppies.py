from IPython.display import Image, display
from . import PACKAGEDIR
import numpy as np
import pandas as pd

breeds = ['corgi', 'goldenretriever', 'husky', 'poodle', 'dalmatian', 'schnauzer', 'collie', 'bernese']

class Puppy():
    ''' Generic Puppy Class '''

    def __init__(self, breed='any'):
        self.breed = breed
        if breed.lower().replace(' ', '') not in breeds:
            self.breed = np.random.choice(breeds)
        # Generate URL
        self.image_address = '{}/data/{}.jpg'.format(PACKAGEDIR, self.breed.lower().replace(' ', ''))

    def _repr_html_(self):
        display(Image(self.image_address, width=1000))

    def sit(self):
        display(Image(self.image_address, width=1000))

    def stay(self):
        display(Image(self.image_address, width=1000))

    def to_pandas(self):
        '''Convert puppy to pandas dataframe'''
        df = pd.DataFrame(columns=['pupper','pup','doggo'])
        df.pupper = ['PUPPY'] * 100
        df.pup = ['PUPPY'] * 100
        df.doggo = ['PUPPY'] * 100
        return df

    def to_numpy(self):
        ''' Convert puppy to numpy array'''
        return np.asarray([l for l in 'puppypuppypuppypuppypuppy'], dtype=str).reshape((5, 5))

    def __repr__(self):
            return '''
                    ___
                 __/.  `.  .-"""-.
                 \_,` | \-'  /   )`-')
                  "") `"`    \  ((`"`
                 ___Y  ,    .'7 /|
                (_,___/...-` (_/_/ '''

    def __str__(self):
            return '''
                    ___
                 __/.  `.  .-"""-.
                 \_,` | \-'  /   )`-')
                  "") `"`    \  ((`"`
                 ___Y  ,    .'7 /|
                (_,___/...-` (_/_/ '''
