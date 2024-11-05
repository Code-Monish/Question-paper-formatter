import sqlite3

# We make a connection with a database (Makes one if doesn't already exists.)
conn = sqlite3.connect("Hello.db")

# This is a 'Cursor/pointer' to where are connection is made
cursor = conn.cursor()

data = {
  "Course Data": [
    {
      "course_code": "23RAI003",
      "course_details": [
        {
          "course_name": "C Programming",
          "course_outcomes": [
            {
              "course_objective": "CO1",
              "description": "Apply algorithmic thinking to understand, define and solve problems."
            },
            {
              "course_objective": "CO2",
              "description": "Interpret the typical programming constructs such as data (primitive and compound), control, modularity, and recursion in a program."
            },
            {
              "course_objective": "CO3",
              "description": "Analyze a given program by tracing, identifying coding errors, and debugging them."
            },
            {
              "course_objective": "CO4",
              "description": "Develop computer programs that implement suitable algorithms for problem scenarios and applications."
            }
          ]
        }
      ]
    }]}

# print(data)
for i in data.values():
    for j in i:
        for course_det in j.values():
            print(course_det)