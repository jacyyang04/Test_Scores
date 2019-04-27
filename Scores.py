#Jacy Yang's If Else Statements Test Scores

#introduces user to the program
def intro():
    print "This program compares two applicants to"
    print "determine which one seems like the stronger"
    print "applicant. For each candidate, I will need"
    print "either SAT or SAT scores plus a weighted GPA."
    print
#calculates gpa scores and returns GPA score
def GPA():
    overall_gpa = float(raw_input("    overall GPA? "))
    max_gpa = float(raw_input("    max GPA? "))
    transcript_multiplier = float(raw_input("    Transcript Multiplier? "))
    gpa_score = float((overall_gpa / max_gpa) * 100 * transcript_multiplier)
    print "    GPA score = %s" % round(gpa_score, 1)
    return gpa_score
#calculates SAT scores and returns exam score
def SAT():
    math = float(raw_input("    SAT math? "))
    reading = float(raw_input("    SAT critical reading? "))
    writing = float(raw_input("    SAT writing? "))
    exam_score = float(((2 * math) + reading + writing) / 32)
    print "    exam score = %s" % round(exam_score, 1)
    return exam_score
#calculates ACT scores and returns exam score
def ACT():
    english = float(raw_input("    ACT English? "))
    math = float(raw_input("    ACT Math? "))
    reading = float(raw_input("    ACT Reading? "))
    science = float(raw_input("    ACT Science? "))
    exam_score = float((english + (2 * math) + reading + science)/1.8)
    print "    exam score = %s" % round(exam_score, 1)
    return exam_score
#prompts exam types and returns exam score, returns GPA scores,
def scores():
    test = int(raw_input("    do you have 1) SAT scores 2) ACT scores? "))
    total_score = 0
    if test == 1:
        exam_score = SAT()
    elif test == 2:
        exam_score = ACT()
    else:
        print "    Please try again!"
        scores()
    gpa_score = GPA()
    total_score = round(exam_score + gpa_score, 1)
    return total_score
#recieves applicant number, computes applicant score and returns applicant scores
def score_applicant(applicant_number):
    print "Information for applicant #%s:" %applicant_number
    total_score = scores()
    print
    return total_score
#recieves two floats representing candidate scores, prints the stronger candidate
def comparison(first, second):
    print "The First applicant overall score = %s" %first
    print "The Second applicant overall score = %s" %second
    if first > second:
        print "The first applicant seems to be better."
    elif second > first:
        print "The second applicant seems to be better"
    else:
        print "The two applicants seem to be equal."
################################################################################

intro()
first = score_applicant(1)
second = score_applicant(2)
comparison(first, second)
