import easygui
import math


def numberOfTeachersNeeded():
    nameOfSchool = easygui.enterbox("Enter the name of the School",
                                    "School Name")
    maxClassSize = easygui.integerbox(
        "What is the maximum number of children "
        "allowed per class:\nMust be a number "
        "between 10 and 30",
        "Maximum class size",
    )
    totalNumChildren = easygui.integerbox(
        "What is the total number of children "
        f"at {nameOfSchool}:Must be a number "
        f"between 10 and 1400",
        "Total roll " "of school",
        upperbound=1400,
        lowerbound=10,
    )

    numOfTeachers = math.ceil(totalNumChildren / maxClassSize)
    availableNumTeachers = easygui.integerbox(
        f"How many teachers are at "
        f"{nameOfSchool}\nMust be a number "
        f"between 1 and 120",
        "Actual number of teachers",
        upperbound=120,
    )
    if availableNumTeachers == numOfTeachers:
        easygui.msgbox(
            "You have the right amount of teachers for students",
            "Right Amount"
        )
    elif availableNumTeachers > numOfTeachers:
        x = availableNumTeachers - numOfTeachers
        easygui.msgbox(
            f"You have too many teachers\nYou could do without {x} "
            f"teachers",
            "Too many",
        )
    elif availableNumTeachers < numOfTeachers:
        x = numOfTeachers - availableNumTeachers
        easygui.msgbox(
            f"You don't have enough teachers\nYou need {x} more " f"teachers",
            "Not enough",
        )


while True:
    yOrN = easygui.ynbox("Do you want to Calculate the number of Teachers "
                         "needed for your school?", "Welcome")
    if yOrN == 1:
        numberOfTeachersNeeded()
    else:
        quit()
