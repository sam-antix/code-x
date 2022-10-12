# Title: Dictionary.py
# Date: 2022-10-06 20:49:04.000-05:00 (CST)
# Encoding: UTF-8
# @author: samantix

# ----------------------------------------------------------
class Dictionary(object):
    '''class for making, assessing, and modifying dictionary objects'''
    # * Initializer ------------------------------------------------
    # initializes initial class object attributes

    def __init__(self, d={}):
        '''method called upon object instantiation (creation)'''
        self.d = d

    # * Getters ----------------------------------------------------

    def get_d(self):
        return self.d

    # * Tellers ----------------------------------------------------

    def __repr__(self):
        return 'Dictionary({})'.format(str(self.d)[1:-1])

    def __str__(self):
        '''
        returns a str representation of argument (prioritized before __repr__() method)
        '''
        return str(self.get_d())

    def __add__(self, d2):
        return self.merge(d2)

    def isSuperSetOf_v1(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: bool eval of d2 as subset of d1
        Tech: all(), for in, items(), get(), values()
        @author: samantix
        '''
        d1 = self.get_d()
        d2 = d2.get_d()
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
        d1 = self.get_d()
        d2 = d2.get_d()
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
        d1 = self.get_d()
        d2 = d2.get_d()
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
        O: d  
        F: {ascii letter : int}
        '''
        # ----------------------------------------------------------
        # *  Sub-functions
        # Variables for improved readability
        ascii_letter_range = 65
        upper_case_letters = range(26)
        lower_case_letters = range(32, 58)

        def upper_case():
            return {chr(ascii_letter_range + ucc_index): ucc_index for ucc_index in upper_case_letters}

        def lower_case():
            return {chr(ascii_letter_range + lcc_index): lcc_index for lcc_index in lower_case_letters}

        def all_case_indexed():
            return ({**upper_case(), **lower_case()})

        def all_case_paired():
            return {chr(ascii_letter_range + ucc_index): [chr(ascii_letter_range + lcc_index) for lcc_index in lower_case_letters][ucc_index] for ucc_index in upper_case_letters}
        # ----------------------------------------------------------
        # ----------------------------------------------------------
        # * Option functions

        def invalid():
            print('Invalid input.\n')

        def get_case(case):

            option = {
                "l": ("Format: 'a':31,...'z':57 (default)", lower_case),
                "u": ("Format: 'A':0,...'Z':25", upper_case),
                "ai": ("Format: 'A':0,...'z':57", all_case_indexed),
                "ap": ("Format: 'A':'a',...'Z':'z'", all_case_paired)
            }

            return option.get(case, [None, invalid])[1]()
        # ----------------------------------------------------------

        return get_case(case)
#!----------------------------------------------------------

    # + ------------------WORKING-------------------- +
    def get_key_str(self, case='l'):
        # return {chr(ascii_letter_range + ucc_index): [chr(ascii_letter_range + lcc_index) for lcc_index in lower_case_letters][ucc_index] for ucc_index in upper_case_letters}.keys()
        # return self.make_dict().keys()
        return ''.join([k for k, v in self.make_dict(case).items()])
# +----------------------------------------------------------

    def merge(self, d2={}):
        '''
        I: any 2 dicts
        O: 1 merged d
        F: {k:v}
        '''
        return {**self, **d2}
#!----------------------------------------------------------

    # + ------------------WORKING-------------------- +
    def shift_keys(self, shift=0):
        ud_str = Dictionary().get_key_str('u')
        ld_str = Dictionary().get_key_str('l')

        ud_dict = {char: ud_str[(ud_str.index(char) + shift) % 26]
                   for char in ud_str}
        ld_dict = {char: ld_str[(ld_str.index(char) + shift) % 26]
                   for char in ld_str}

        return {**ud_dict, **ld_dict}


#!----------------------------------------------------------
        # def modHand(self, word):
        #     hc = self.hand.copy()
        #     # {k:v for (k,v) in iterable}
        #     wd = {k: hc[k] for k in hc if hc[k]}
        #     for e in word:
        #         hc[e] -= 1
        #     self.hand = {k: hc[k] for k in hc if hc[k]}
        #     return True
#!----------------------------------------------------------
        # {char:      uc_str[(uc_str.index(char) + shift) % 26]       for char in uc_str}
        # {char:      lc_str[(lc_str.index(char) + shift) % 26]       for char in lc_str}

        # k1 = char
        # k2 = char
        # v1 = uc_str[(uc_str.index(char) + shift) % 26]
        # v2 = lc_str[(lc_str.index(char) + shift) % 26]
        # iterable1 = uc_str
        # iterable2 = lc_str

        # {k:v for v in iterable}
# +----------------------------------------------------------

    def subtractVals_v1(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: d of d1 less d2
        Tech: for in, items(), get()
        @author: samantix
        credit: https://stackoverflow.com/questions/17671875/how-to-subtract-values-from-dictionaries
        '''
        d1 = self.get_d()
        d2 = d2.get_d()
        new_d = {}
        for k, v in d1.items():
            new_d[k] = v - d2.get(k, 0)
        return new_d

    def subtractVals(self, d2):
        '''
        I: 2 dictionaries with int/float values
        O: d of d1 less d2
        Tech: list comprehension, get(), for in, items()
        @author: samantix
        Version: 2
        '''
        d1 = self.get_d()
        d2 = d2.get_d()
        return {k: d1[k] - d2.get(k, 0) for k, v in d1.items()}

    def swap_KeyVal(self):
        '''
        I: d x1
        O: d x1
        F: {k:v}
        # * Ex: {k:v} -> {v:k} 
        '''
        d = self.get_d()
        return {v: k for k, v in iter(d.items())}

    def group(self):
        '''
        groups (itemizes) elements of a sequence

        I: sequence (iterable): list,d,str, etc.
        O: d
        F: {item:item_count}
        '''
        d = {}
        for e in self.get_d():
            d[e] = d.get(e, 0) + 1
        return d

    def ungroup(self):
        '''
        I: d of str:int pairs
        O: list of concatenated strings of key-value products
        F: {'a':2,'b':1,'z':3} -> a a b z z z
        @author: samantix
        DOC: 10/01/2022 19:00 CST
        '''
        d = self.get_d()
        # Initialize list that will hold the key-value products
        keyList = []
        # unpack d chars as if they were quantified by their respective values
        for k, v in d.items():
            keyList += str(k)*int(v)

        # join them horizontally, separated by a single space
        return ' '.join(keyList)


# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @


#ud = Dictionary().make_dict('u')
#ld = Dictionary().make_dict('l')
# d.get_key_str()


# print(d.keys())
# print({char ud[i+3]: ld[i+3] for i in range(len(ud))})


# print(Dictionary().shift_keys(3))
# print(Dictionary.mro())
# print(Make.mro())
#d = Dictionary({'a': 1})
# print(d)
# print(Dictionary().shift_keys(3))


# print(d1.merge(d2))


d1 = Dictionary().make_dict()
d2 = Dictionary().make_dict('u')
#print(Dictionary.merge(d1, d2))
#xd = Dictionary(x)
#zd = Dictionary(z)
#print(Dictionary.merge(xd, zd))

x = {'a': 32, 'b': 33, 'c': 34, 'd': 35, 'e': 36, 'f': 37, 'g': 38, 'h': 39, 'i': 40, 'j': 41, 'k': 42, 'l': 43, 'm': 44,
     'n': 45, 'o': 46, 'p': 47, 'q': 48, 'r': 49, 's': 50, 't': 51, 'u': 52, 'v': 53, 'w': 54, 'x': 55, 'y': 56, 'z': 57}

y = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
     'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

print(Dictionary.merge(x, y))
