import os
import sys
import sqlite3
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import select
from pathlib import Path
from splice_models import Samples, Packs


# select samples.filename, packs.genre from samples join packs on packs.uuid = samples.pack_uuid where packs.genre=“pop”
OUTPUTDIR = "/Volumes/Pulsar/Splito"

class SampleField:
        ID = 0
        local_path = 1
        attr_hash = 2
        dir = 3
        audio_key = 4
        bpm = 5
        chord_type = 6
        duration = 7
        file_hash = 8
        sas_id = 9
        filename = 10
        genre = 11
        pack_uuid = 12
        sample_type = 13
        tags = 14
        popularity = 15
        purchased_at = 16
        last_modified_at = 17
        waveform_url = 18
        provider_name = 19
        pack_id	= 20,
        uuid = 21,
        pack_name = 22,
        description	= 23,
        cover_url = 24,
        genre = 25,
        permalink = 26,
        pack_provider = 27

DRUM_MAP = {
     "snares", 
     "hats", 
     "kicks",
     "crash",  
     "rides", 
     "cymbals", 
     "toms", 
     "claps",
     "rims",
     "fills",
     "japanese",
     "middle eastern",
     "asian",
     "bells",
     "shakers",
     "latin",
     "kalimba"
}

INSTRUMENTS_MAP = {
    "mallets"
}

SUB_GENRE_MAP = {
    "hip hop":"hip hop",
    "kompa": "afrobeat",
    "deep house": "housentechno",
    "drum and bass": "drum and bass",
    "trap": "trap",
    "jersey club": "housentechno",
    "pop":"chillout",
    "hyperpop":"future bass",
    "rnb":"funk_n_soul",
    "lo-fi hip hop": "hip hop",
    "flamenco": "afro latin",
    "tech house": "housentechno",
    "jungle": "drum and bass",
    "leftfield bass": "dubstep",
    "trip hop": "trip hop",
    "house": "housentechno",
    "uk garage": "housentechno",
    "disco": "funk_n_soul",
    "edm": "housentechno",
    "neo soul": "funk_n_soul",
    "afropop & afrobeats": "afrobeat",
    "techno": "housentechno",
    "future soul": "funk_n_soul",
    "soul": "funk_n_soul",
    "future bass": "future bass",
    "cinematic": "chillwave",
    "tropical house": "housentechno",
    "bossa nova": "afro latin",
    "synthwave": "chillwave",
    "minimal techno": "housentechno",
    "funk": "funk_n_soul",
    "latin american": "afro latin",
    "reggaeton": "afro latin",
    "latin trap": "afro latin",
    "psy trance": "housentechno",
    "jazz": "funk_n_soul",
    "uk drill": "trap",
    "boom bap": "hip hop",
    "glitch": "idm",
    "idm": "idm",
    "experimental": "idm",
    "desert blues": "afrobeats",
    "glitch hop": "idm",
    "reggae": "reggaedub",
    "dub": "reggaedub",
    "cumbia": "afro latin",
    "afro latin": "afro latin",
    "caribbean": "afro latin",
    "jump up dnb": "drum and bass",
    "dubstep": "dubstep",
    "trap edm": "trap",
    "tearout dubstep": "dubstep",
    "asian": "asian",
    "chiptune": "idm",
    "big room house": "housentechno",
    "hard techno": "housentechno",
    "melodic techno": "housentechno",
    "drumstep": "dubstep",
    "downtempo": "chillwave",
    "drill": "trap",
    "indie pop": "chillwave",
    "synth-pop": "chillwave",
    "dancehall": "afro latin",
    "african": "afrobeats",
    "son cubano": "afro latin",
    "chillout": "chillwave",
    "gospel": "funk_n_soul",
    "game audio": "idm",
    "future house": "housentechno",
    "progressive house": "housentechno",
    "electro": "housentechno",
    "funky house": "housentechno",
    "electro house": "housentechno",
    "breakbeat": "drum and bass",
    "ambient": "chillwave",
    "trance": "housentechno",
    "middle eastern": "asian",
    "breaks": "drum and bass",
    "dembow": "latin",
    "indie electronic": "indie",
    "deep dubstep": "dubstep",
    "indie rock": "indie",
    "afro house": "afrobeats",
    "phonk": "funk_n_soul",
    "hand pan": "hand pan"
}

engine = None
db_session = None


def determine_parent_genre(sample: Samples):
    genre = SUB_GENRE_MAP.get(sample.pack.genre)
    if genre is None:
         for sub_genre in SUB_GENRE_MAP.keys():
            if sub_genre in sample.tags:
                 genre = SUB_GENRE_MAP.get(sub_genre)
                 break
                
    return genre or "hybrid"  

# def is_not_tagged_as(sample, tag):
#     return tag in sample.tags.split(",")

def is_tops(sample):
    if sample.tag_list.intersection({
         "hats", "cymbals", "rides"
    }):
         return True
    return False

def determine_sample_type(s_type):
     if s_type == "loop":
          return "Loops"
     return "OneShots"

def determine_genre(sample: Samples):
    parent_genre = determine_parent_genre(sample)
    return parent_genre

def determine_drum_part(sample: Samples):
    if sample.tag_list.issuperset({"hats", "open"}) and "snares" not in sample.tag_list:
        return "hats"
    
    for drum in DRUM_MAP:
        if drum in sample.tag_list:
            return drum
    return "uncategorized"

def determine_drums(sample: Samples):
    print(f"processing: {sample.filename}")
    determined_path = [OUTPUTDIR]
    if "percussion" in sample.tags and not sample.is_drumnbass() and sample.is_not_tagged_as("mallets"):
         determined_path.append("Percussions")

    elif "drums" in sample.tags:
        determined_path.append("Drums")

    if len(determined_path) < 2:
         return

    s_type = determine_sample_type(sample.sample_type)
    determined_path.append(s_type)

    if s_type == "Loops":
        genre = determine_genre(sample)
        determined_path.append(genre)
        if is_tops(sample):
             determined_path.append("tops")
    else:
        drum_part = determine_drum_part(sample)
        determined_path.append(drum_part)

    directory = "/".join(determined_path)
    print(f"* {directory}/{sample.filename}")


              
              

# connection = sqlite3.connect("sounds.db")
# cur = connection.cursor()
# res = cur.execute("select * from samples join packs on packs.uuid = samples.pack_uuid limit 1")
# samples_list = cur.fetchall()
# for sample in samples_list:
#     print(sample)

engine=sqlalchemy.create_engine('sqlite:///sounds.db')

def scan_whole_db(session):
    # sample_objs = session.scalars(select(Samples)).all()
    stmt = select(Samples).where(Samples.sample_type == "oneshot").where(Samples.tags.like("%open%"))
    db_data = session.scalars(stmt).all() #.fetchmany(50)
    # print(db_data.sample_type)
    return db_data

with Session(engine) as session:    
    db_data = scan_whole_db(session)

    for sample in db_data:
        determine_drums(sample)