#Jacy Yang's If Else Statements Test Scores

#introduces user to the program
def intro():
    print "This program compares two applicants to"
    print "determine which one seems like the stronger"
    print "applicant. For each candidate, I will need"
    print "either SAT or SAT scores plus a weighted GPA."
    print
#calculates gpa scores
def GPA():
    overall_gpa = float(raw_input("overall GPA? "))
    max_gpa = float(raw_input("max GPA? "))
    transcript_multiplier = float(raw_input("Transcript Multiplier? "))
    gpa_score = round((overall_gpa / max_gpa) * 100 * transcript_multiplier)
    print "GPA score = %s" %gpa_score
    return gpa_score
#calculates SAT scores
def SAT():
    math = int(raw_input("SAT_MATH? "))
    reading = int(raw_input("SAT critical reading? "))
    writing = int(raw_input("SAT writing? "))
    exam_score = float(((2 * math) + reading + writing) / 32)
    print "exam score = %s" % exam_score
    return exam_score
#calculates ACT scores
def ACT():
    english = int(raw_input("ACT English? "))
    math = int(raw_input("ACT Math? "))
    reading = int(raw_input("ACT Reading? "))
    science = int(raw_input("ACT Science? "))
    exam_score = round((english + (2 * math) + reading + science)/1.8, 1)
    print "exam score = %s" % exam_score
    return exam_score
#asks user for calculation function
def scores():
    test = int(raw_input("do you have 1) SAT scores 2) ACT scores? "))
    total_score = 0
    if test == 1:
        exam_score = SAT()
        gpa_score = GPA()
        total_score = round(exam_score + gpa_score, 1)
    elif test == 2:
        exam_score = ACT()
        gpa_score = GPA()
        total_score = round(exam_score + gpa_score, 1)
    else:
        print "Please try again!"
        scores()
    return total_score
    print

def first():
    print "Information for applicant #%s" %1
    toal_score = scores()
    return total_score

def second():
    "Information for applicant #%s" %2
    total_score = scores()
    return total_score

#compares two canidates
#def comparison():
#    first = first()
#    second = second()
#    print "The First applicant overall score = %s" %first
#    print "The Second applicant overall score = %s" %second
#    if first > second:
#        print "The first applicant seems to be better."
#    elif second > first:
#        print "The second applicant seems to be better"
#    else:
#        print "The two applicants seem to be equal."
################################################################################

intro()
first = first()
second = second()
print "The First applicant overall score = %s" %first
print "The Second applicant overall score = %s" %second
if first > second:
    print "The first applicant seems to be better."
elif second > first:
    print "The second applicant seems to be better"
else:
    print "The two applicants seem to be equal."
