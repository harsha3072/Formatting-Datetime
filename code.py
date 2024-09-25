from datetime import datetime

dt_format = "%b %d %Y %I:%M%p"
dt_object = datetime.strptime(input(), dt_format)

output_format = datetime.strftime(dt_object, "%d/%m/%Y %H:%M:%S")
print(output_format)
