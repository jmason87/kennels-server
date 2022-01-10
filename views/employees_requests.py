EMPLOYEES = [
    {
      "id": 2,
      "name": "Jordan Nelson",
      "email": "jordan@nelson.com",
    },
    {
      "name": "Meg Ducharme",
      "email": "meg@ducharme.com",
      "id": 4,
    },
    {
      "name": "Emily Lemmon",
      "email": "emily@lemmon.com",
      "id": 6,
    },
    {
      "name": "Leah Gwin",
      "email": "leah@gwin.com",
      "id": 8,
    },
    {
      "name": "Caitlin Stein",
      "email": "caitlin@stein.com",
      "id": 9,
    },
    {
      "name": "Greg Korte",
      "email": "greg@korte.com",
      "id": 10,
    },
    {
      "name": "Charisse Lambert",
      "email": "charisse@lambert.com",
      "id": 11,
    },
    {
      "name": "Madi Peper",
      "email": "madi@peper.com",
      "id": 12,
    },
    {
      "name": "Jenna Solis",
      "email": "jenna@solis.com",
      "id": 14,
    },
    {
      "name": "Eric \"Macho Man\" Taylor",
      "email": "macho@man.com",
      "id": 22
    },
    {
      "name": "Joe Mason",
      "email": "joe@mason.com",
      "id": 23
    },
    {
      "name": "Jim Bob",
      "email": "jim@bob.com",
      "id": 24
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
