from fastapi import FastAPI, Response
from pydantic import BaseModel
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
from PIL import Image
import os, threading

app = FastAPI()
lock = threading.Lock()
COUNTER_FILE = "counter.txt"

def get_next_counter():
    with lock:
        if not os.path.exists(COUNTER_FILE):
            with open(COUNTER_FILE, "w") as f:
                f.write("1")
            return 1
        with open(COUNTER_FILE, "r+") as f:
            count = int(f.read())
            f.seek(0)
            f.write(str(count + 1))
            f.truncate()
            return count

# ------------------------
# ✅ PAGE BACKGROUNDS
# ------------------------
backgrounds = {
    "page1": "01 Form144 finalized_page-0001.jpg",
    "page2": "01 Form144 finalized_page-0002.jpg",
    "page3": "01 Form144 finalized_page-0003.jpg",
    "page4": "01 Form144 finalized_page-0004.jpg",
}

# ------------------------
# ✅ PAGE COORDINATES
# ------------------------
coords = {
    "page1": {
        "policyholder_name": (550, 1060),
        "policy_number": (400, 1270),
        "policy_start_date": (450, 1350),
    },
    "page2": {
        "max_liability": (600, 140),
        "shipment_date": (600, 245),
        "buyer_name": (470, 350),
        "buyer_address": (470, 380),
        "buyer_city": (270, 430),
        "buyer_country": (790, 430),
        "buyer_phone": (390, 460),
        "buyer_fax": (810, 460),
        "buyer_email": (300, 480),
        "buyer_website": (800, 480),
        "buyer_contact": (380, 510),
        "buyer_mobile": (840, 510),
        "buyer_reg": (440, 530),
        "buyer_vat": (805, 530),
        "alt_address": (470, 585),
        "alt_city": (270, 640),
        "alt_country": (790, 640),
        "alt_phone": (390, 665),
        "alt_fax": (810, 665),
        "alt_email": (300, 690),
        "alt_website": (800, 690),
        "alt_contact": (380, 715),
        "alt_mobile": (840, 715),
        "alt_reg": (440, 740),
        "alt_vat": (805, 740),
        "parent_name": (800, 820),
        "parent_address": (400, 845),
        "parent_city": (270, 900),
        "parent_country": (790, 900),
        "parent_phone": (390, 920),
        "parent_fax": (810, 920),
        "parent_email": (300, 950),
        "parent_website": (800, 950),
        "parent_contact": (380, 975),
        "parent_mobile": (840, 975),
        "parent_reg": (440, 999),
        "parent_vat": (805, 999),
        "bank_name": (510, 1105),
        "bank_address": (500, 1155),
        "bank_city": (270, 1210),
        "bank_country": (790, 1210),
        "bank_phone": (380, 1235),
        "bank_fax": (810, 1235),
        "bank_email": (300, 1259),
        "bank_ac": (380, 1285),
        "bank_swift": (860, 1285),
        "goods_desc": (430, 1340),
        "export_country": (770, 1390),
        "destination_country": (560, 1440),
    },
    "page3": {
        "order_no": (470, 190),
        "order_amount": (400, 217),
        "terms_payment": (800, 220),
        "ship_sched1": (310, 300),
        "ship_sched2": (710, 300),
        "ship_sched3": (1010, 300),
        "anticipated_country": (960, 370),
        "product_value": (410, 460),
        "product_desc": (800, 460),
        "sec16a_i": (970, 863),
        "sec16a_ii": (830, 885),
        "sec16a_iii": (850, 908),
        "sec16a_iv": (1035, 940),
        "sec16b": (1035, 800),
        "sec16b_para": (1035, 993),
        "sec17": (1035, 1065),
        "sec17_para": (1038, 1220),
        "cheque_no": (410, 1300),
        "cheque_date": (560, 1300),
        "cheque_amount": (840, 1300),
        "branch": (410, 1330),
        "cheque_city": (270, 1390),
        "cheque_submit_date": (270, 1420),
    },
    "page4": {
        "years1": (800, 350),
        "years2": (800, 370),
        "years3": (808, 400),
        "nature_concern": (850, 490),
        "buyer_class1": (960, 530),
        "buyer_class2": (960, 560),
        "buyer_class3": (960, 640),
        "fin1": (960, 660),
        "fin2": (960, 680),
        "legal1": (850, 735),
        "legal2": (850, 755),
        "legal3": (850, 785),
    }
}

table_xs = [210, 300, 430, 580, 720, 850, 980]
table_start_y = 676
row_gap = 28

for i in range(1, 5):  # rows 1 to 4
    for j in range(1, 8):  # cols 1 to 7
        x = table_xs[j - 1]
        y = table_start_y + (i - 1) * row_gap
        coords["page3"][f"row{i}_col{j}"] = (x, y)

# ------------------------
# ✅ FULL FORM MODEL
# ------------------------
class Form144Data(BaseModel):
    # page 1 + 2 + 3 + 4 fields
    policyholder_name: str; policy_number: str; policy_start_date: str; policy_end_date: str
    max_liability: str; shipment_date: str
    buyer_name: str; buyer_address: str; buyer_city: str; buyer_country: str; buyer_phone: str
    buyer_fax: str; buyer_email: str; buyer_website: str; buyer_contact: str; buyer_mobile: str
    buyer_reg: str; buyer_vat: str
    alt_address: str; alt_city: str; alt_country: str; alt_phone: str; alt_fax: str
    alt_email: str; alt_website: str; alt_contact: str; alt_mobile: str; alt_reg: str; alt_vat: str
    parent_name: str; parent_address: str; parent_city: str; parent_country: str; parent_phone: str
    parent_fax: str; parent_email: str; parent_website: str; parent_contact: str; parent_mobile: str
    parent_reg: str; parent_vat: str
    bank_name: str; bank_address: str; bank_city: str; bank_country: str; bank_phone: str
    bank_fax: str; bank_email: str; bank_website: str; bank_ac: str; bank_swift: str
    goods_desc: str; export_country: str; destination_country: str
    order_no: str; order_amount: str; terms_payment: str; ship_sched1: str; ship_sched2: str
    ship_sched3: str; anticipated_country: str; product_value: str; product_desc: str
    sec16a_i: str; sec16a_ii: str; sec16a_iii: str; sec16a_iv: str; sec16b: str
    sec16b_para: str; sec17: str; sec17_para: str
    cheque_no: str; cheque_date: str; cheque_amount: str; branch: str; cheque_city: str
    cheque_submit_date: str
    years1: str; years2: str; years3: str; nature_concern: str
    buyer_class1: str; buyer_class2: str; buyer_class3: str
    fin1: str; fin2: str
    legal1: str; legal2: str; legal3: str
    # ✅ table fields
    row1_col1: str; row1_col2: str; row1_col3: str; row1_col4: str; row1_col5: str; row1_col6: str; row1_col7: str
    row2_col1: str; row2_col2: str; row2_col3: str; row2_col4: str; row2_col5: str; row2_col6: str; row2_col7: str
    row3_col1: str; row3_col2: str; row3_col3: str; row3_col4: str; row3_col5: str; row3_col6: str; row3_col7: str
    row4_col1: str; row4_col2: str; row4_col3: str; row4_col4: str; row4_col5: str; row4_col6: str; row4_col7: str

# ------------------------
# ✅ PDF GENERATOR
# ------------------------
@app.post("/generate-form144/")
async def generate_pdf(data: Form144Data):
    buffer = BytesIO()
    c = None

    for page in ["page1", "page2", "page3", "page4"]:
        bg = Image.open(backgrounds[page]).convert("RGB")
        width, height = bg.size
        image_reader = ImageReader(bg)

        if c is None:
            c = canvas.Canvas(buffer, pagesize=(width, height))
        else:
            c.setPageSize((width, height))

        c.drawImage(image_reader, 0, 0, width=width, height=height)
        c.setFont("Helvetica", 14)

        for field, (x, y) in coords[page].items():
            value = getattr(data, field, "")
            if value:
                c.drawString(x, height - y - 16, value)

        c.showPage()

    c.save()
    buffer.seek(0)
    pdf_number = get_next_counter()
    filename = f"Form144_Filled_{pdf_number}.pdf"

    return Response(content=buffer.read(), media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename={filename}"
    })
