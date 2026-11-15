# Name: <Shofwatul Hasanah Sarma>
# NIM: <2511533015>
# Question 7

name = "shofwatul hasanah sarma"        
nim = "2511533015"         
username = "shofwatul015"     
intake = "26" + nim[0:2]    

line = "=" * 30

print(line)
print(f"{'STUDENT CARD':^30}")
print(line)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print(line)