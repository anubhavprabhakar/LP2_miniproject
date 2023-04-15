question = {'COUGH_COLD': ['Do you have cough and cold'], 'SMELL_TASTE': ['Are you able to recognize smell and taste'], 'SORE_THROAT': ['Are you suffering from sore throat'], 'HEADACHE': ['Are you suffering from headache'], 'BP_DIABETES': ['Are you suffering from BP/ diabetes'], 'IN_CONTACT_COVID': ['Have you come in a contact of a Covid suspicious person']}

def diagnosisTest():
	answers = []
	for i in question:
		print(question[i][0])
		ans = input()
		if(ans=='y' or ans=='yes' or ans=='Yes' or ans=='YES'):
			question[i].append(True)
		else:
			question[i].append(False)

