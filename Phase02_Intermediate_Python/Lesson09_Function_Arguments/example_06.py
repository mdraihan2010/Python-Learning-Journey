# **kwargs ব্যবহার করা হয় যখন Function কতগুলো Keyword Arguments পাবে তা আগে থেকে জানা নেই।
# Basic Example


def student_info(**info):
    print(info)


student_info(
    name="Raihan",
    age=23,
    department="CSE"
)