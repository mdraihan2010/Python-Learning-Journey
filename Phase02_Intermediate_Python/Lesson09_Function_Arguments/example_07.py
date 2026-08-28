# *args এবং **kwargs একসাথে


def student_info(*subjects, **details):

    print("Subjects:", subjects)

    print("Details:", details)


student_info(
    "Python",
    "DBMS",
    "Data Structure",
    name="Raihan",
    age=23
)