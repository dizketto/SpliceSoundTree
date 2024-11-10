import os
import sys
import sqlite3
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import select
from pathlib import Path
from splice_models import Samples, Packs
from shutil import copy2
from genre_mapping import SUB_GENRE_MAP
from domain_mapping import *
# select samples.filename, packs.genre from samples join packs on packs.uuid = samples.pack_uuid where packs.genre=“pop”
OUTPUTDIR = "/Volumes/Pulsar/Splito"

engine = None
db_session = None


def determine_parent_genre(sample: Samples):
    genre = SUB_GENRE_MAP.get(sample.pack.genre)
    if genre is None:
         for sub_genre in SUB_GENRE_MAP.keys():
            if sub_genre in sample.tag_list:
                 genre = SUB_GENRE_MAP.get(sub_genre)
                 break
                
    return genre or "hybrid"  



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

def determine_instrument_by_tag_map(sample: Samples, map):
    for inst in map:
        if inst in sample.tag_list:
            return inst
    return "uncategorized"

def determine_instrument_by_name_map(sample: Samples, map):
    for inst in map:
        if inst.lower() in sample.filename.lower():
            return inst

def is_tonal(sample: Samples):
    if sample.tag_list.issubset(set(INSTRUMENTS_MAP)):
        return True
    return False


def determine_instrument(sample: Samples, category: SampleCategory):
    instr = determine_instrument_by_name_map(sample, category.name_map)
    if instr:
        return align(instr, category.tag_map)
    
    if not instr:
        instr = determine_instrument_by_tag_map(sample, category.tag_map)
    
    return instr

def add_to_drums_tree(sample: Samples):
    determined_path = [OUTPUTDIR]

    if is_tonal(sample):
        return None
    
    if not sample.tag_list.intersection({"drums", "percussion", "snares", "kicks", "rims", "hats", "crash", "fills"}):
        return None
    
    if "percussion" in sample.tags and not sample.is_drumnbass() and (
        not sample.is_tagged_as("handpan")
    ) and (
        not sample.is_tagged_as("hand pan")
    ):
         determined_path.append("Percussions")

    elif sample.tag_list.intersection(DRUMS_SAFESET) != set():
        determined_path.append("Drums")

    if len(determined_path) < 2:
         return None

    s_type = determine_sample_type(sample.sample_type)
    determined_path.append(s_type)

    if s_type == "Loops":
        genre = determine_genre(sample)
        determined_path.append(genre)
        if is_tops(sample):
             determined_path.append("tops")
    else:
        drum_part = determine_instrument(sample, PercussiveCategory())
        determined_path.append(drum_part)

    directory = "/".join(determined_path)

    # print(f"+ {directory}/{sample.filename}")
    return directory


def add_to_chromatic_tree(sample: Samples):
    determined_path = [OUTPUTDIR]
    determined_path.append("Chromatics")
    s_type = determine_sample_type(sample.sample_type)
    determined_path.append(s_type)
    instrument = determine_instrument(sample, ChromaticCategory())
    determined_path.append(instrument)
    genre = determine_genre(sample)
    determined_path.append(genre)
    directory = "/".join(determined_path)
    print(f"+ {directory}/{sample.filename}")
    return directory
              

# connection = sqlite3.connect("sounds.db")
# cur = connection.cursor()
# res = cur.execute("select * from samples join packs on packs.uuid = samples.pack_uuid limit 1")
# samples_list = cur.fetchall()
# for sample in samples_list:
#     print(sample)

engine=sqlalchemy.create_engine('sqlite:///sounds.db')

def scan_whole_db(session):

    stmt = select(Samples) #.where(Samples.sample_type == "oneshot") #.where(Samples.tags.like("%open%"))
    db_data = session.scalars(stmt).all() #.fetchmany(50)
    # print(db_data.sample_type)
    return db_data

with Session(engine) as session:    
    db_data = scan_whole_db(session)

    for sample in db_data:
        directory = add_to_drums_tree(sample)

        if not directory:
            directory = add_to_chromatic_tree(sample)
        
        if directory:
            """ save the file """
            os.makedirs(directory, exist_ok=True)
            os.system(f"touch '{directory}/{sample.filename}'")
            
            # copy2(sample.local_path, f"{directory}/{sample.filename}")