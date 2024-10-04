from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, ForeignKey, UUID, DateTime

Base = declarative_base()


class Materials(Base):
    __tablename__ = 'materials'

    id = Column(UUID, primary_key=True)
    material_name = Column(String)
    representative_name = Column(String)


class MaterialsSample(Base):
    __tablename__ = 'materials_sample'

    id = Column(UUID, primary_key=True)
    material_name = Column(String)
    representative_name = Column(String)
    Period = Column(String)
    Local_Production = Column(Float)
    Import_Dependence = Column(Float)


