import pandas as pd
fileinput = str(input("Enter File Name:"))
spreadsheet = pd.read_csv(r"<location to file>\%s"%(fileinput), encoding='ISO-8859-1', low_memory=False)
high_issues = spreadsheet["Result Severity"] == "High"
print("***********************************************************")
print("Total Number of issues:",spreadsheet[high_issues].shape[0])
print("***********************************************************")
new_issues = spreadsheet.loc[(spreadsheet["Result Severity"] == "High") & (spreadsheet["Result Status"] == "New")]
new_issues.shape[0]
print("Number of New issues:",new_issues.shape[0])
print("***********************************************************")
old_issues = spreadsheet.loc[(spreadsheet["Result Severity"] == "High") & (spreadsheet["Result Status"] == "Recurrent")]
print("Number of Old issues:",old_issues.shape[0])
print("***********************************************************")
print("**********Project Level - Number of Old issues*************")
split_source_loc_old = old_issues.SrcFileName.str.split('/', expand=True)
print(split_source_loc_old[0].value_counts())
print("***********************************************************")
print("**********Project Level - Number of New issues*************")
split_source_loc_new = new_issues.SrcFileName.str.split('/', expand=True)
print(split_source_loc_new[0].value_counts())
print("***********************************************************")
print("**********Project Level - Number of Total issues***********")
split_source_loc_total = spreadsheet[high_issues].SrcFileName.str.split('/', expand=True)
print(split_source_loc_total[0].value_counts())


