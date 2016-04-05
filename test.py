import safygiphy
import te

total_tests = 0
succesful_tests = []
failed_tests = []
errors = ["####################################################"]
"""
Giphy object tests
"""

# TODO: Test all built in API Endpoints with tags/IDs that will work
# TODO: Test all built in API Endpoints with tags/IDs that won't work
# TODO: Test all __getattr__ API Endpoints with tags/IDs that will work
# TODO: Test all __getattr__ API Endpoints with tags/IDs that won't work
# TODO: Test an API endpoint that doesn't exist and that gives a 404 error

"""
Sticky object tests
"""

# TODO: Test all built in API Endpoints with tags/IDs that will work
# TODO: Test all built in API Endpoints with tags/IDs that won't work
# TODO: Test all __getattr__ API Endpoints with tags/IDs that will work
# TODO: Test all __getattr__ API Endpoints with tags/IDs that won't work
# TODO: Test an API endpoint that doesn't exist and that gives a 404 error

"""
Combined object tests
"""

# TODO: Test all GIF built in API Endpoints with tags/IDs that will work
# TODO: Test all GIF built in API Endpoints with tags/IDs that won't work
# TODO: Test all GIF __getattr__ API Endpoints with tags/IDs that will work
# TODO: Test all GIF __getattr__ API Endpoints with tags/IDs that won't work
# TODO: Test a GIF API endpoint that doesn't exist and that gives a 404 error

# TODO: Test all STICKER built in API Endpoints with tags/IDs that will work
# TODO: Test all STICKER built in API Endpoints with tags/IDs that won't work
# TODO: Test all STICKER __getattr__ API Endpoints with tags/IDs that will work
# TODO: Test all STICKER __getattr__ API Endpoints with tags/IDs that won't work
# TODO: Test a STICKER API endpoint that doesn't exist and that gives a 404 error

print("####################################################")
print("ALL TESTS COMPLETED")
print("{0} TEST RAN".format(total_tests))
if failed_tests:
    print("{0} TEST(S) SUCCESSFUL".format(succesful_tests))
    print("{0} TEST(S) FAILED".format(len(failed_tests)))
    for test in failed_tests:
        print("TEST: {0} FAILED WITH ERROR: {1}".format(test["name"], test["error"]))
else:
    print("ALL TESTS RAN SUCCESFULLY")