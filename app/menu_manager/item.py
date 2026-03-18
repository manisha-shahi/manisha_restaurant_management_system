
import json

def food_items():
    data = {
    "Snacks": {
        "Veg Spring Roll": { "half_plate": 70, "full_plate": 120 },
        "Paneer Tikka": { "half_plate": 100, "full_plate": 180 },
        "Veg Manchurian": { "half_plate": 90, "full_plate": 150 },
        "Chilli Paneer": { "half_plate": 110, "full_plate": 170 },
        "non vegFrench Fries": { "half_plate": 60, "full_plate": 100 },
        "Hara Bhara Kebab": { "half_plate": 90, "full_plate": 160 },
        "Chicken Tikka": { "half_plate": 120, "full_plate": 220 },
        "Chicken Lollipop": { "half_plate": 130, "full_plate": 240 },
        "Samosa":{ "half_plate": 15, "full_plate": 30 },
        "Pakoda":{ "half_plate": 50, "full_plate": 70 },
        "Kachori":{ "half_plate": 60, "full_plate": 120 },
        "Aloo Tikki":{ "half_plate": 70, "full_plate": 140 },
        "Bread Pakora":{ "half_plate": 30, "full_plate": 40 }
    },

    "Main Course": {
        "Butter Paneer Masala": { "half_plate": 140, "full_plate": 220 },
        "Shahi Paneer": { "half_plate": 130, "full_plate": 210 },
        "Kadai Paneer": { "half_plate": 120, "full_plate": 200 },
        "Dal Makhani": { "half_plate": 110, "full_plate": 180 },
        "Mix Veg": { "half_plate": 100, "full_plate": 160 },
        "Palak Paneer": { "half_plate": 120, "full_plate": 190 },
        "Matar Paneer": { "half_plate": 120, "full_plate": 190 },
        "Chole Masala": { "half_plate": 100, "full_plate": 170 }
    },

    "Roti": {
        "Tandoori Roti": { "half_plate": 10, "full_plate": 20 },
        "Butter Naan": { "half_plate": 20, "full_plate": 40 },
        "Garlic Naan": { "half_plate": 25, "full_plate": 50 },
        "Lachha Paratha": { "half_plate": 25, "full_plate": 45 },
        "Plain Naan": { "half_plate": 15, "full_plate": 35 },
        "Cheese Naan":{ "half_plate": 35, "full_plate": 65 }
    },

    "Rice": {
        "Plain Rice": { "half_plate": 50, "full_plate": 90 },
        "Jeera Rice": { "half_plate": 70, "full_plate": 120 },
        "Veg Pulao": { "half_plate": 90, "full_plate": 150 },
        "Veg Biryani": { "half_plate": 110, "full_plate": 180 },
        "Chicken Biryani": { "half_plate": 130, "full_plate": 220 }
    },

    "Fast Food": {
        "Veg Burger": { "half_plate": 50, "full_plate": 80 },
        "Cheese Burger": { "half_plate": 70, "full_plate": 100 },
        "Veg Pizza": { "half_plate": 120, "full_plate": 200 },
        "Pasta": { "half_plate": 90, "full_plate": 150 },
        "Sandwich": { "half_plate": 60, "full_plate": 120 },
        "non veg Burger":{ "half_plate": 60, "full_plate": 120 },
        "non veg Pizza":{ "half_plate": 60, "full_plate": 120 },
        "veg French Fries":{ "half_plate": 60, "full_plate": 120 }
    },

    "Desserts": {
        "Gulab Jamun": { "half_plate": 40, "full_plate": 80 },
        "Ice Cream": { "half_plate": 50, "full_plate": 90 },
        "Rasgulla": { "half_plate": 40, "full_plate": 80 },
        "Brownie": { "half_plate": 70, "full_plate": 120 }
    },

    "Drinks": {
        "Cold Drink": { "half_plate": 30, "full_plate": 60 },
        "Lassi": { "half_plate": 40, "full_plate": 80 },
        "Masala Chai": { "half_plate": 20, "full_plate": 40 },
        "Coffee": { "half_plate": 30, "full_plate": 60 }
    }
    }

    with open("app/database/item_data.json", "w") as file:
        json.dump(data, file, indent=4)
        return data
        
