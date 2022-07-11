import requests

product_id = input("Waht is the product ID you want to delete?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print("Not an innteger")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)