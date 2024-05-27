from pydantic import BaseModel

class Param(BaseModel):
    env_hum: float
    env_temp: float
    soil_con: float
    soil_hum: float
    soil_nitro: float
    soil_ph: float
    soil_phos: float
    soil_pot: float
    soil_salin: float
    soil_tds: float
    soil_temp: float