import frappe
import requests
# from frappe.integrations.utils import make_get_request

@frappe.whitelist()
def call_api(doc):
    # print(doc)
    response = requests.get(f"https://swapi.dev/api/people/{doc}")

    # url = f"https://swapi.dev/api/people/{doc}"
    # response = frappe.make_get_request(url)

    r =  response.json()
    return r['name']