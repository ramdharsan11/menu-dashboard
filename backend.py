from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data
menu_items = [
    {"id": 1, "name": "Pizza", "price": 12.99, "sales": 100},
    {"id": 2, "name": "Burger", "price": 8.99, "sales": 85},
    {"id": 3, "name": "Pasta", "price": 10.99, "sales": 45},
    {"id": 4, "name": "Salad", "price": 6.99, "sales": 30},
    {"id": 5, "name": "Soda", "price": 2.99, "sales": 120},
]

@app.get("/api/bestsellers")
def get_bestsellers():
    sorted_items = sorted(menu_items, key=lambda x: x["sales"], reverse=True)
    return sorted_items[:3]

@app.get("/api/low-margin")
def get_low_margin():
    # Items with price < $8 are "low margin"
    return [item for item in menu_items if item["price"] < 8]

@app.get("/api/low-performing")
def get_low_performing():
    sorted_items = sorted(menu_items, key=lambda x: x["sales"])
    return sorted_items[:2]

@app.get("/api/kpi")
def get_kpi():
    total_sales = sum(item["sales"] for item in menu_items)
    total_revenue = sum(item["price"] * item["sales"] for item in menu_items)
    return {
        "total_items": len(menu_items),
        "total_orders": total_sales,
        "total_revenue": round(total_revenue, 2)
    }

@app.get("/api/search")
def search(q: str = ""):
    return [item for item in menu_items if q.lower() in item["name"].lower()]