import re

raw_pets =[
    {"pet_code": "P301", "species": "dog", "price": 7500000, "status": "available"},
    {"pet_code": "p101", "species": "cat", "price": 3000000, "status": "available"},
    {"pet_code": "P202", "species": "bird", "price": 1200000, "status": "sold"},
    {"pet_code": "P102", "species": "cat", "price": 3500000, "status": "reserved"},
    {"pet_code": "P302", "species": "dog", "price": 9000000, "status": "available"}
]
def clean_and_validate_pets(raw_pets):
    cleaned_pets = []
    pattern = re.compile(r"^P\d+$")
    for pet in raw_pets:
        p = pet.copy()
        p["pet_code"] = p["pet_code"].strip().upper()

        if pattern.match(p["pet_code"]):
            cleaned_pets.append(p)
    return cleaned_pets

# Phần 1.2

def search_pets(pets, max_price, status=None):
    result = []
    for pet in pets:
        cond_price = pet["price"] <= max_price

        if status is not None:
            cond_status = pet.get("status") == status
        else:
            cond_status = True

        if cond_price and cond_status:
            result.append(pet)

    return result

# Phần 1.3

def sort_pets_by_price_desc(pets):
    n = len(pets)
    sorted_pets = pets.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_pets[j]["price"] < sorted_pets[j+1]["price"]:
                sorted_pets[j], sorted_pets[j+1] = sorted_pets[j+1], sorted_pets[j]
    return sorted_pets