"""
RECORD CHECK  -  my version
===========================

Name  : Maryam Khader
Lane  :  AI 
Date  : 8/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

    # This line of code checks the percentage and returns if the result is over limit, warning, or ok. 


label = input("Label: ")
value = float(input("Value: "))
limit = float(input("Limit: "))

difference = limit - value  
percent = (limit / value) * 100
status = status_of(percent)




# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
