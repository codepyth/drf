from datetime import date

today = (date.today())
print((date.today()))
print(today.year)
print((today.month, today.day))


# def age_restriction(dob):
#     today = date.today()
#     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
#     if not (20 < age < 30):
#         return "You are no eligible for the job"
#     return dob
#
#
# age_restriction(05-09-2021)