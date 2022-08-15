# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('music_collection')

collection = SHEET.worksheet('collection')
data = collection.get_all_values()




table = Table(title="WoM Record Collection")

for heading in data[0]:
    table.add_column(f"{heading}")

for row in data[1::1]:
    table.add_row(*row, style="bold black on white")

console = Console()
console.print(table)