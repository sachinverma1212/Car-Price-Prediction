from pydantic import BaseModel, Field
from enum import Enum
from typing import Literal,List


class FuelType(str,Enum):
    petrol= "Petrol"
    diesel = "Diesel"
    cng = "CNG"
    
    
    
class SellerType(str,Enum):
    dealer = "Dealer"
    individual = "Individual"
    
class Transmission(str,Enum):
    manual = "Manual"
    automatic = "Automatic"
    




class CarFeatures(BaseModel):
    Car_Name: str= Field(..., example = "ritz")
    Year: int = Field(..., example= 2014)
    Present_Price: float = Field(..., example= 5.59)
    Owner: int = Field(...,ge=0,le=3,example=0,description="Number of previous owners (0,1 or 3)")
    Kms_Driven: int = Field(...,example= 27000)
    
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: Transmission
     
    

class PredictionResponse(BaseModel):
    prediction_price:float
    