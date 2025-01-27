from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

paper_author = Table(
    "paper_author",
    Base.metadata,
    Column("paper_id", ForeignKey("paper.id"), primary_key=True),
    Column("author_id", ForeignKey("author.id"), primary_key=True),
)


paper_keyword = Table(
    "paper_keyword",
    Base.metadata,
    Column("paper_id", ForeignKey("paper.id"), primary_key=True),
    Column("keyword_id", ForeignKey("keyword.id"), primary_key=True),
)


paper_paper = Table(
    "paper_paper",
    Base.metadata,
    Column("paper_id_1", ForeignKey("paper.id"), primary_key=True),
    Column("paper_id_2", ForeignKey("paper.id"), primary_key=True),
)


class Author(Base):
    __tablename__ = "author"
    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=True)
    papers = relationship("Paper", secondary=paper_author, back_populates="authors")


class Venue(Base):
    __tablename__ = "venue"
    id = Column(String(100), primary_key=True)
    name = Column(String(200), nullable=True)
    papers = relationship("Paper", back_populates="venue")


class Lang(Base):
    __tablename__ = "lang"
    id = Column(String(100), primary_key=True)
    papers = relationship("Paper", back_populates="lang")


class Keyword(Base):
    __tablename__ = "keyword"
    id = Column(String(1_000), primary_key=True)
    papers = relationship("Paper", secondary=paper_keyword, back_populates="keywords")


class Paper(Base):
    __tablename__ = "paper"
    id = Column(String(100), primary_key=True)
    title = Column(String(500), nullable=True)
    year = Column(Integer, nullable=True)
    authors = relationship("Author", secondary=paper_author, back_populates="papers")
    venue_id = Column(String(100), ForeignKey("venue.id"))
    venue = relationship("Venue", back_populates="papers")
    n_citations = Column(Integer, nullable=True)
    keywords = relationship("Keyword", secondary=paper_keyword, back_populates="papers")
    abstract = Column(String(100_000), nullable=True)
    # to do: think about dropping it, it takes too much space
    url = Column(String(1_000_000), nullable=True)
    lang_id = Column(String(100), ForeignKey("lang.id"))
    lang = relationship("Lang", back_populates="papers")
    # references = relationship("Paper", secondary=paper_paper, back_populates='references')


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
