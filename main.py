from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()
app.title = "Fonoma Backend Exercise"
app.description = "Solution for the Fonoma Backend exercise"
app.version = "0.0.1"

class Order(BaseModel):
    id: Optional[int] = None
    item: str = Field(max_length=100)
    quantity: int = Field(ge=1)
    price: float = Field(ge=0.01) #le == less or equal
    status: str = Field(max_length=30) #ge == great or equal

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item":  "Lavadora",
                "quantity": 1,
                "price": 299.99,
                "status": "completed"
            }
        }    



@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.post("/solution", tags=["solution"], status_code=201,response_model=str)
async def process_orders(orders: List[Order] = Body(), criterion:str = Body()):                     
    """
        sumary_line
    
        Keyword arguments:
        orders -- A list of order(A Base Model to validate the fields of each item)
        Return: return the computation of all the items that match with the criterion by the quantity of the items in the petition
    """
    revenue = 0
    if criterion == "all":
        for order in orders:
            revenue += order.price * order.quantity
    else:
        for order in orders:
            if criterion == order.status:
                revenue += order.price * order.quantity
        if revenue == 0:
            return "The criterion you search is not in the list"
    return revenue

if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)


