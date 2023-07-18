LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Dictionary of the rotors and the reflectors, according to the documentation
I     = {'A':'E','B':'K','C':'M','D':'F','E':'L','F':'G','G':'D','H':'Q','I':'V','J':'Z','K':'N','L':'T','M':'O','N':'W','O':'Y','P':'H','Q':'X','R':'U','S':'S','T':'P','U':'A','V':'I','W':'B','X':'R','Y':'C','Z':'J'}
II    = {'A':'A','B':'J','C':'D','D':'K','E':'S','F':'I','G':'R','H':'U','I':'X','J':'B','K':'L','L':'H','M':'W','N':'T','O':'M','P':'C','Q':'Q','R':'G','S':'Z','T':'N','U':'P','V':'Y','W':'F','X':'V','Y':'O','Z':'E'}
III   = {'A':'B','B':'D','C':'F','D':'H','E':'J','F':'L','G':'C','H':'P','I':'R','J':'T','K':'X','L':'V','M':'Z','N':'N','O':'Y','P':'E','Q':'I','R':'W','S':'G','T':'A','U':'K','V':'M','W':'U','X':'S','Y':'Q','Z':'O'}
IV    = {'A':'E','B':'S','C':'O','D':'V','E':'P','F':'Z','G':'J','H':'A','I':'Y','J':'Q','K':'U','L':'I','M':'R','N':'H','O':'X','P':'L','Q':'N','R':'F','S':'T','T':'G','U':'K','V':'D','W':'C','X':'M','Y':'W','Z':'B'}
V     = {'A':'V','B':'Z','C':'B','D':'R','E':'G','F':'I','G':'T','H':'Y','I':'U','J':'P','K':'S','L':'D','M':'N','N':'H','O':'L','P':'X','Q':'A','R':'W','S':'M','T':'J','U':'Q','V':'O','W':'F','X':'E','Y':'C','Z':'K'}
VI    = {'A':'J','B':'P','C':'G','D':'V','E':'O','F':'U','G':'M','H':'F','I':'Y','J':'Q','K':'B','L':'E','M':'N','N':'H','O':'Z','P':'R','Q':'D','R':'K','S':'A','T':'S','U':'X','V':'L','W':'I','X':'C','Y':'T','Z':'W'}
VII   = {'A':'N','B':'Z','C':'J','D':'H','E':'G','F':'R','G':'C','H':'X','I':'M','J':'Y','K':'S','L':'W','M':'B','N':'O','O':'U','P':'F','Q':'A','R':'I','S':'V','T':'L','U':'P','V':'E','W':'K','X':'Q','Y':'D','Z':'T'}
VIII  = {'A':'F','B':'K','C':'Q','D':'H','E':'T','F':'L','G':'X','H':'O','I':'C','J':'B','K':'J','L':'S','M':'P','N':'D','O':'Z','P':'R','Q':'A','R':'M','S':'E','T':'W','U':'N','V':'I','W':'U','X':'Y','Y':'G','Z':'V'}
BETA  = {'A':'L','B':'E','C':'Y','D':'J','E':'V','F':'C','G':'N','H':'I','I':'X','J':'W','K':'P','L':'B','M':'Q','N':'M','O':'D','P':'R','Q':'T','R':'A','S':'K','T':'Z','U':'G','V':'F','W':'U','X':'H','Y':'O','Z':'S'}
UKB_B = {'A':'E','B':'N','C':'K','D':'Q','E':'A','F':'U','G':'Y','H':'W','I':'J','J':'I','K':'C','L':'O','M':'P','N':'B','O':'L','P':'M','Q':'D','R':'X','S':'Z','T':'V','U':'F','V':'T','W':'H','X':'R','Y':'G','Z':'S'}
UKB_C = {'A':'R','B':'D','C':'O','D':'B','E':'J','F':'N','G':'T','H':'K','I':'V','J':'E','K':'H','L':'M','M':'L','N':'F','O':'C','P':'W','Q':'Z','R':'A','S':'X','T':'G','U':'Y','V':'I','W':'P','X':'S','Y':'U','Z':'Q'}


CONFIG_FILE = "config"

# plugboard without connections
def base_plugboard():
    return {l:l for l in LETTERS}

def read_configuration():
    with open(CONFIG_FILE, "r") as config_file:
        config = config_file.read().split(" ")
    rotors = config[:4]
    offsets = [int(x) for x in config[4:8]]
    plugboard = base_plugboard()
    for cable in config[8:-1]: # plugboard is modificated
        l1, l2 = cable
        plugboard[l1] = l2
        plugboard[l2] = l1
    reflector = config[-1]
    return (rotors, offsets, plugboard, reflector)


