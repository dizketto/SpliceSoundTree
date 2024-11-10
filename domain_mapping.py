from enum import Enum

class Category(Enum):
    Percussive = 0
    Chromatic = 1

class SampleCategory:
    @property
    def name_map(self):
        raise NotImplementedError
    
    @property
    def tag_map(self):
        raise NotImplementedError
    

class PercussiveCategory(SampleCategory):
    @property
    def type(self):
        return Category.Percussive

    @property
    def name_map(self):
        return DRUM_NAME_MAP
    
    @property
    def tag_map(self):
        return DRUM_TAG_MAP
    
    @property
    def etno_map(self):
        return ETNO_MAP
    

class ChromaticCategory(SampleCategory):
    @property
    def type(self):
        return Category.Chromatic
    
    @property
    def name_map(self):
        return INSTRUMENTS_MAP
    
    @property
    def tag_map(self):
        return INSTRUMENTS_MAP
    
    @property
    def etno_map(self):
        return ETNO_MAP



DRUM_TAG_MAP = [
     "snares",  
     "kicks",
     "claps",
     "hats",
     "rims",
     "crash",  
     "rides", 
     "cymbals", 
     "toms", 
     "fills",
     "japanese",
     "middle eastern",
     "asian",
     "bells",
     "shakers",
     "shaker",
     "latin",
     "latin american",
     "wooden",
     "metallic",
     "tablas",
     "tabla",
     "congas",
     "conga",
     "SID"
]

DRUM_NAME_MAP = [
    name.rstrip("s") for name in DRUM_TAG_MAP
]

DRUMS_SAFESET = {
    "drums", 
    "percussion", 
    "snares", 
    "kicks", 
    "rims", 
    "hats", 
    "crash", 
    "fills",
    "shakers",
    "shaker",
    "tom",
    "toms",
    "cymbals"
}

INSTRUMENTS_MAP = [
    "riser",
    "drop",
    "pluck",
    "mallets",    
    "bass",
    "brass & woodwinds",
    "trumpet",
    "fx",
    "keys",
    "synth",
    "piano",
    "voice",
    "vocals",
    "vocal",
    "guitar",
    "pads",
    "pad",
    "latin american",
    #"hand pan",
    "handpan",
    "steeldrum",
    "steel drum",
    "metallic",
    "SID",
    "strings",
    "violin",
    "viola",
    "music"
]

ETNO_MAP = [
    "african",
    "arabic",
    "japanese",
    "middle eastern",
    "chinese",
    "indian",
]


def align(inst, map):
    for mapped_name in map:
        if inst in mapped_name:
            return mapped_name
        

