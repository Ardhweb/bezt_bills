import_successful = False

# try:
#     from invoicemodule.models import Invoicer
#     import_successful = True
#     print("Import successful.")
# except ImportError as e:
#     import_successful = False
#     print(f"Import failed: {e}")

# if import_successful:
#     print("Running in development mode.")
# else:
#     print("Running in production mode.")

try:
    from bezt_bills.core.models import Address
    t = True  # Indicates the import was successful
    print("Running in development mode.")
except ImportError:
    t = False  # Indicates the import failed

# Use the value of t to determine the mode
if t==True:
    print("Running in development mode.")
else:
    print("Running in production mode.")

