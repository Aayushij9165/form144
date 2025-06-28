from pydantic import BaseModel
from typing import Optional
from datetime import date

class Page1Model(BaseModel):
    policyholder_name: Optional[str]
    policy_number: Optional[str]
    policy_start_date: Optional[date]
    policy_end_date: Optional[date]

class BuyerModel(BaseModel):
    buyer_name: Optional[str]
    buyer_address: Optional[str]
    buyer_city: Optional[str]
    buyer_country: Optional[str]
    buyer_phone: Optional[str]
    buyer_fax: Optional[str]
    buyer_email: Optional[str]
    buyer_website: Optional[str]
    buyer_contact: Optional[str]
    buyer_mobile: Optional[str]
    buyer_reg: Optional[str]
    buyer_vat: Optional[str]

class AltBuyerModel(BaseModel):
    alt_address: Optional[str]
    alt_city: Optional[str]
    alt_country: Optional[str]
    alt_phone: Optional[str]
    alt_fax: Optional[str]
    alt_email: Optional[str]
    alt_website: Optional[str]
    alt_contact: Optional[str]
    alt_mobile: Optional[str]
    alt_reg: Optional[str]
    alt_vat: Optional[str]

class ParentCompanyModel(BaseModel):
    parent_name: Optional[str]
    parent_address: Optional[str]
    parent_city: Optional[str]
    parent_country: Optional[str]
    parent_phone: Optional[str]
    parent_fax: Optional[str]
    parent_email: Optional[str]
    parent_website: Optional[str]
    parent_contact: Optional[str]
    parent_mobile: Optional[str]
    parent_reg: Optional[str]
    parent_vat: Optional[str]

class BankModel(BaseModel):
    bank_name: Optional[str]
    bank_address: Optional[str]
    bank_city: Optional[str]
    bank_country: Optional[str]
    bank_phone: Optional[str]
    bank_fax: Optional[str]
    bank_email: Optional[str]
    bank_website: Optional[str]
    bank_ac: Optional[str]
    bank_swift: Optional[str]

class GoodsModel(BaseModel):
    goods_desc: Optional[str]
    export_country: Optional[str]
    destination_country: Optional[str]

class OrderModel(BaseModel):
    order_no: Optional[str]
    order_amount: Optional[str]
    terms_payment: Optional[str]
    ship_sched1: Optional[str]
    ship_sched2: Optional[str]
    ship_sched3: Optional[str]
    anticipated_country: Optional[str]
    product_value: Optional[str]
    product_desc: Optional[str]

class TableRowModel(BaseModel):
    row1_col1: Optional[str]
    row1_col2: Optional[str]
    row1_col3: Optional[str]
    row1_col4: Optional[str]
    row1_col5: Optional[str]
    row1_col6: Optional[str]
    row1_col7: Optional[str]
    row2_col1: Optional[str]
    row2_col2: Optional[str]
    row2_col3: Optional[str]
    row2_col4: Optional[str]
    row2_col5: Optional[str]
    row2_col6: Optional[str]
    row2_col7: Optional[str]
    row3_col1: Optional[str]
    row3_col2: Optional[str]
    row3_col3: Optional[str]
    row3_col4: Optional[str]
    row3_col5: Optional[str]
    row3_col6: Optional[str]
    row3_col7: Optional[str]
    row4_col1: Optional[str]
    row4_col2: Optional[str]
    row4_col3: Optional[str]
    row4_col4: Optional[str]
    row4_col5: Optional[str]
    row4_col6: Optional[str]
    row4_col7: Optional[str]

class Section16_17Model(BaseModel):
    sec16a_i: Optional[str]
    sec16a_ii: Optional[str]
    sec16a_iii: Optional[str]
    sec16a_iv: Optional[str]
    sec16b: Optional[str]
    sec16b_para: Optional[str]
    sec17: Optional[str]
    sec17_para: Optional[str]

class ChequeModel(BaseModel):
    cheque_no: Optional[str]
    cheque_date: Optional[date]
    cheque_amount: Optional[str]
    branch: Optional[str]
    cheque_city: Optional[str]
    cheque_submit_date: Optional[date]

class Page4Model(BaseModel):
    years1: Optional[str]
    years2: Optional[str]
    years3: Optional[str]
    nature_concern: Optional[str]
    buyer_class1: Optional[str]
    buyer_class2: Optional[str]
    buyer_class3: Optional[str]
    fin1: Optional[str]
    fin2: Optional[str]
    legal1: Optional[str]
    legal2: Optional[str]
    legal3: Optional[str]

class Form144Model(BaseModel):
    page1: Page1Model
    buyer: BuyerModel
    alt_buyer: AltBuyerModel
    parent: ParentCompanyModel
    bank: BankModel
    goods: GoodsModel
    order: OrderModel
    table: TableRowModel
    sec16_17: Section16_17Model
    cheque: ChequeModel
    page4: Page4Model
