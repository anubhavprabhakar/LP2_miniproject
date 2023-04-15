question = {'BODY-TEMPERATURE': ['What is your body temperature'], 'OXYGEN-LEVEL': ['What is your oxygen level'], 'VACCINES-TAKEN': ['How many vaccines have you taken'], 'AGE':['what is your age']}

def takeInput():
	
	for i in question:
		print(question[i][0])
		ans = float(input())
		question[i].append(ans)

		
		
