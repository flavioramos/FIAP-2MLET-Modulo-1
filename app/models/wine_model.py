from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declared_attr

from app.extensions import db


class YearlyDataMixin():
    """Mixin to dynamically add columns for years 1970 to 2023."""

    @declared_attr
    def __table_args__(cls):
        return {'sqlite_autoincrement': True}

    for year in range(1970, 2024):
        locals()[f'y_{year}'] = db.Column(Integer)


class Comercio(db.Model, YearlyDataMixin):
    __tablename__ = 'comercio'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    produto = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "produto": self.produto,
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ExpEspumantes(db.Model, YearlyDataMixin):
    __tablename__ = 'exp_espumantes'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ExpSuco(db.Model, YearlyDataMixin):
    __tablename__ = 'exp_suco'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ExpUva(db.Model, YearlyDataMixin):
    __tablename__ = 'exp_uva'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ExpVinho(db.Model, YearlyDataMixin):
    __tablename__ = 'exp_vinho'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ImpEspumantes(db.Model, YearlyDataMixin):
    __tablename__ = 'imp_espumantes'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ImpFrescas(db.Model, YearlyDataMixin):
    __tablename__ = 'imp_frescas'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ImpPassas(db.Model, YearlyDataMixin):
    __tablename__ = 'imp_passas'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ImpSuco(db.Model, YearlyDataMixin):
    __tablename__ = 'imp_suco'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ImpVinhos(db.Model, YearlyDataMixin):
    __tablename__ = 'imp_vinhos'
    id = db.Column(Integer, primary_key=True)
    pais = db.Column(String)

    def to_dict(self):
        data = {
            "pais": self.pais
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ProcessaAmericanas(db.Model, YearlyDataMixin):
    __tablename__ = 'processa_americanas'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    cultivar = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "cultivar": self.cultivar
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ProcessaMesa(db.Model, YearlyDataMixin):
    __tablename__ = 'processa_mesa'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    cultivar = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "cultivar": self.cultivar
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ProcessaSemclass(db.Model, YearlyDataMixin):
    __tablename__ = 'processa_semclass'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    cultivar = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "cultivar": self.cultivar
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class ProcessaViniferas(db.Model, YearlyDataMixin):
    __tablename__ = 'processa_viniferas'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    cultivar = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "cultivar": self.cultivar
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data


class Producao(db.Model, YearlyDataMixin):
    __tablename__ = 'producao'
    id = db.Column(Integer, primary_key=True)
    control = db.Column(String)
    produto = db.Column(String)

    def to_dict(self):
        data = {
            "control": self.control,
            "produto": self.produto
        }
        for year in range(1970, 2024):
            data[f'{year}'] = getattr(self, f'y_{year}')

        return data
