# Title: Dictionary.py
# Date: 2022-10-06 20:49:04.000-05:00 (CST)
# @author: samantix

# ----------------------------------------------------------
class Dictionary(object):
    '''class for making, assessing, and modifying dictionary objects'''
    # * Initializer ------------------------------------------------

    def __init__(self, Dict={}):
        self.Dict = Dict

    # * Getters ----------------------------------------------------

    def getDict(self):
        return self.Dict

    # * Tellers ----------------------------------------------------

    def __repr__(self):
        return 'Dictionary({})'.format(str(self.getDict())[1:-1])

    def __str__(self):
        '''
        returns a str representation of argument (prioritized before __repr__() method)
        '''
        return str(self.getDict())

    def isSuperSetOf_v1(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: bool eval of d2 as subset of d1
        Tech: all(), for in, items(), get(), values()
        @author: samantix
        '''
        d1 = self.getDict()
        d2 = d2.getDict()
        new_d = {}
        for k, v in d1.items():
            new_d[k] = v - d2.get(k, 0)
        return all(set(d2) <= set(d1) and i >= 0 for i in new_d.values())

    def isSuperSetOf_v2(self, d2):
        '''
        Convert dicts to sets of their keys & verify the word is a subset of the hand

        I: 2 dictionaries with int/float values
        O: bool eval of d2 as subset of d1
        F: True (or False)
        Tech: all(), for in, items(), get(), values()
        @author: samantix
        Version: 2
        '''
        d1 = self.getDict()
        d2 = d2.getDict()
        if set(d2) <= set(d1):
            # remove all char of the word from the hand
            new_d = {k: d1[k] - d2.get(k, 0) for k, v in d1.items()}
            # verify that the hand has no negative char values after word removal
            return all(i >= 0 for i in new_d.values())
        else:
            return False

    def isSuperSetOf(self, d2):
        '''
        Convert dicts to sets of their keys & verify the word is a subset of the hand

        I: 2 dictionaries with int/float values
        O: bool eval of d2 as subset of d1
        Tech: all(), for in, items(), get(), values()
        @author: samantix
        Version: 3
        '''
        d1 = self.getDict()
        d2 = d2.getDict()
        # remove all char in word from hand
        new_d = {k: d1[k] - d2.get(k, 0) for k, v in d1.items()}
        # convert dicts to sets of their keys;
        # verify word is subset of hand; and
        # verify hand w/o neg char val after word removal
        return all(set(d2) <= set(d1) and i >= 0 for i in new_d.values())

    # * Doers ------------------------------------------------------

    def make_dict(self, case="l"):
        '''
        I: empty dictionary; case (u=upper, l=lower, a=all)
        O: dict  
        F: {ascii letter : int}
        '''
        # ----------------------------------------------------------
        # *  Sub-methods
        # Variables for improved readability
        ascii_letter_range = 65
        upper_case_letters = range(26)
        lower_case_letter = range(32, 58)

        def upper_case():
            return {chr(ascii_letter_range + ucc_index): ucc_index for ucc_index in upper_case_letters}

        def lower_case():
            return {chr(ascii_letter_range + lcc_index): lcc_index for lcc_index in lower_case_letter}

        def all_case():
            return ({**upper_case(), **lower_case()})

        def paired_case():
            return {chr(ascii_letter_range + ucc_index): [chr(ascii_letter_range + lcc_index) for lcc_index in lower_case_letter][ucc_index] for ucc_index in upper_case_letters}
        # ----------------------------------------------------------
        # * Option functions

        def invalid():
            print('Invalid command.\n')

        def get_case(case):

            option = {
                "l": ("Format: 'a':31,...'z':57 (default)", lower_case),
                "u": ("Format: 'A':0,...'Z':25", upper_case),
                "a": ("Format: 'A':0,...'z':57", all_case),
                "p": ("Format: 'A':'a',...'Z':'z'", paired_case)
            }

            return option.get(case, [None, invalid])[1]()
        # ----------------------------------------------------------

        return get_case(case)
        # ----------------------------------------------------------

    def merge(self, d2={}):
        '''
        I: any 2 dicts
        O: 1 merged dict
        F: {k:v}
        '''
        return {**self.getDict(), **d2.getDict()}

    def subtractVals_v1(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: dict of d1 less d2
        Tech: for in, items(), get()
        @author: samantix
        credit: https://stackoverflow.com/questions/17671875/how-to-subtract-values-from-dictionaries
        '''
        d1 = self.getDict()
        d2 = d2.getDict()
        new_d = {}
        for k, v in d1.items():
            new_d[k] = v - d2.get(k, 0)
        return new_d

    def subtractVals(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: dict of d1 less d2
        Tech: list comprehension, get(), for in, items()
        @author: samantix
        Version: 2
        '''
        d1 = self.getDict()
        d2 = d2.getDict()
        return {k: d1[k] - d2.get(k, 0) for k, v in d1.items()}

    def swap_KeyVal(self):
        '''
        I: dict x1
        O: dict x1
        F: {k:v}
        # * Ex: {k:v} -> {v:k} 
        '''
        d = self.getDict()
        return {v: k for k, v in iter(d.items())}

    def group(self):
        '''
        groups (itemizes) elements of a sequence

        I: sequence (iterable): list,dict,str, etc.
        O: dict
        F: {item:item_count}
        '''
        d = {}
        for e in self.getDict():
            d[e] = d.get(e, 0) + 1
        return d

    def ungroup(self):
        '''
        I: dict of str:int pairs
        O: list of concatenated strings of key-value products
        F: {'a':2,'b':1,'z':3} -> a a b z z z
        @author: samantix
        DOC: 10/01/2022 19:00 CST
        '''
        d = self.getDict()
        # Initialize list that will hold the key-value products
        keyList = []
        # unpack dict chars as if they were quantified by their respective values
        for k, v in d.items():
            keyList += str(k)*int(v)

        # join them horizontally, separated by a single space
        return ' '.join(keyList)


d = Dictionary()
print(d.make_dict('p'))
