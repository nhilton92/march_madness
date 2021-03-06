from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model_definitions import Base
from model_definitions.team import Team


class Seed(Base):
    __tablename__ = 'seeds'
    TeamID = Column(Integer, ForeignKey(Team.TeamID), primary_key=True, nullable=False)
    Season = Column(Integer, primary_key=True)
    Seed = Column(Integer)

    team = relationship('Team', foreign_keys=[TeamID])
