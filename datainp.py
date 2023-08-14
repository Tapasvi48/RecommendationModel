from pydantic import BaseModel

class USER(BaseModel):
    user_id:object




# sub cat brand user_id item_id
class PRODUCT(BaseModel):
    sub_cat:object
    brand:object
    user_id:object
    item_id:object





