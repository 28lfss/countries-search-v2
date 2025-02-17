from ..database_config import db
from sqlalchemy.orm import Mapped, mapped_column

class Country(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    cca2: Mapped[str] = mapped_column(db.String(3), unique=True, nullable=False)
    country_name: Mapped[str] = mapped_column(db.String(128), unique=True, nullable=False)
    flag_url: Mapped[str] = mapped_column(db.String(128), nullable=False)
    region: Mapped[str] = mapped_column(db.String(32), nullable=False)
    subregion: Mapped[str] = mapped_column(db.String(128), nullable=True)
    population: Mapped[int] = mapped_column(db.SmallInteger, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cca2' : self.cca2,
            'country_name' : self.country_name,
            'flag_url' : self.flag_url,
            'region' : self.region,
            'subregion' : self.subregion,
            'population' : self.population
        }