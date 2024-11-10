from typing import List, Optional

from sqlalchemy import ForeignKey, Index, Integer, TIMESTAMP, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
import datetime

class Base(MappedAsDataclass, DeclarativeBase):
    pass


class DbVersion(Base):
    __tablename__ = 'db_version'

    version_id: Mapped[int] = mapped_column(Integer)
    is_applied: Mapped[int] = mapped_column(Integer)
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    tstamp: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text("datetime('now')"))


class EtagCaches(Base):
    __tablename__ = 'etag_caches'

    id: Mapped[Optional[str]] = mapped_column(Text, primary_key=True)
    etag: Mapped[Optional[str]] = mapped_column(Text)


class Packs(Base):
    __tablename__ = 'packs'
    __table_args__ = (
        Index('uuid_on_packs', 'uuid'),
    )

    uuid: Mapped[str] = mapped_column(Text, unique=True)
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)
    cover_url: Mapped[Optional[str]] = mapped_column(Text)
    genre: Mapped[Optional[str]] = mapped_column(Text)
    permalink: Mapped[Optional[str]] = mapped_column(Text)
    provider_name: Mapped[Optional[str]] = mapped_column(Text)

    samples: Mapped[List['Samples']] = relationship('Samples', back_populates='pack')


class Samples(Base):
    __tablename__ = 'samples'
    __table_args__ = (
        Index('attr_hash_on_samples', 'attr_hash'),
        Index('file_hashes_on_samples', 'file_hash'),
        Index('local_path_on_samples', 'local_path'),
        Index('sas_id_on_samples', 'sas_id')
    ) 

    file_hash: Mapped[str] = mapped_column(Text, unique=True)
    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    local_path: Mapped[Optional[str]] = mapped_column(Text)
    attr_hash: Mapped[Optional[str]] = mapped_column(Text)
    dir: Mapped[Optional[str]] = mapped_column(Text)
    audio_key: Mapped[Optional[str]] = mapped_column(Text)
    bpm: Mapped[Optional[int]] = mapped_column(Integer)
    chord_type: Mapped[Optional[int]] = mapped_column(Integer)
    duration: Mapped[Optional[int]] = mapped_column(Integer)
    sas_id: Mapped[Optional[str]] = mapped_column(Text)
    filename: Mapped[Optional[str]] = mapped_column(Text)
    genre: Mapped[Optional[int]] = mapped_column(Integer)
    pack_uuid: Mapped[Optional[str]] = mapped_column(ForeignKey('packs.uuid'))
    sample_type: Mapped[Optional[int]] = mapped_column(Integer)
    tags: Mapped[Optional[str]] = mapped_column(Text)
    popularity: Mapped[Optional[int]] = mapped_column(Integer)
    purchased_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    waveform_url: Mapped[Optional[str]] = mapped_column(Text)
    provider_name: Mapped[Optional[str]] = mapped_column(Text)

    pack: Mapped['Packs'] = relationship('Packs', back_populates='samples')

    def is_tagged_as(self, tag):
        return tag.strip() in [tag.replace(" ","") for tag in self.tag_list]
    
    def is_drumnbass(self):
     return "drum and bass" in self.tag_list

    @property
    def tag_list(self):
        return set(self.tags.split(","))
    