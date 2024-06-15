# Ternary Operator
promod_marks = 90
amit_marks = 97

# x > y -> do something - print("pramod is winner")
# y > x -> do something else -> print("amit is winner")

print("Promod is winner" if promod_marks > amit_marks else "Amit is winner")

if promod_marks > amit_marks:
    print("Promod is winner")
else:
    print("Amit is winner")