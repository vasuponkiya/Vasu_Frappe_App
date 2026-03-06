import frappe
import requests

@frappe.whitelist()
def call_api(doc):
    # print(doc)
    response = requests.get(f"https://swapi.dev/api/people/{doc}")
    r =  response.json()
    # print(r)
    return r['name']