"""
Refreshes the memory regarding recently learned information.
"""

# Which of the following commands will print the first 5 rows (not including the header) of the
# DataFrame df?

print(df.head(5))

# You’re doing some analytics on the ages of the typical customer for a company. They give you the
# following DataFrame. If you want to ignore all of the PII (personal identifying information) and
# only select the ages from the DataFrame, which of the follow lines of code would you use?

customers = pd.DataFrame(
    [
        ["Jesse Sternberg", "193 6th Avenue", 31],
        ["Amy Lauder", "546 Marblehead Way", 43],
        ["Gerri Sanderson", "65 New York Street", 35],
        ["Austin Barnes", "2888 North Ogden Avenue", 28],
    ],
    columns=["name", "address", "age"],
)

customers.age

# If you wanted to select the row including all of the data for the month of May, which of the
# following lines of code would you use?

clinic_df = pd.DataFrame(
    [
        ["January", 100, 100, 23, 100],
        ["February", 51, 45, 145, 45],
        ["March", 81, 96, 65, 96],
        ["April", 80, 80, 54, 180],
        ["May", 51, 54, 54, 154],
        ["June", 112, 109, 79, 129],
    ],
    columns=["month", "clinic_east", "clinic_north", "clinic_south", "clinic_west"],
)

clinic_df[clinic_df.month == "May"]

# Which of the following commands will correctly import the csv content_inventory.csv into the
# DataFrame content?

content = pd.read_csv("content_inventory.csv")

# Consider the following code that is intended to create a new DataFrame showing the grades of
# students in a class. Will this code create a valid DataFrame? If not, why?

grades = pd.DataFrame(
    {
        "name": ["Chloe", "Grace", "Jeremy", "Isla"],
        "unit_1_grade": [95, 82, 83, 75],
        "unit_2_grade": [91, 74, 89, 84],
        "Grade for the Year": [93, 78, 86],
    }
)

# The code will not run because Grade for the Year has 3 elements instead of the required 4.
