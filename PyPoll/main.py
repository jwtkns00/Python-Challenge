# Dependencies

import csv

# Files to load and output
election_data = "Desktop/Resources/election_data.csv"
txt_file = "Desktop/Test.txt"

#setting values/making new directories
total_votes = 0
number_candidates = 0
candidate_list = []
candidate_votes = {}
maxvotes = -1

# Read the csv and convert it into a list of dictionaries
with open(election_data) as poll_data:
    reader = csv.DictReader(poll_data)

    # Start for loop
    for row in reader:
        current_candidate = row['Candidate']
        #conditinoal statement
        if current_candidate not in candidate_list :
            number_candidates = number_candidates + 1
            candidate_list.append(current_candidate)
            candidate_votes[current_candidate] = 0
            
        candidate_votes[current_candidate]=candidate_votes[current_candidate]+1
        total_votes = total_votes + 1
        
        if candidate_votes[current_candidate] > maxvotes :
            maxvotes = candidate_votes[current_candidate]
            maxcandidate = current_candidate


# In[72]:

#print results

line1 = '  Election Results'
line2 = '  -------------------------'
line3 = ('  Total Votes: %d' %(total_votes))
line4 = '  -------------------------'
output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

for name in candidate_list :
    linex = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+total_votes), candidate_votes[name]))
    output = output + '\n' + linex

output = output + '\n' + '  -------------------------'
output = output + '\n' + ('  Winner: %s' %maxcandidate)
output = output + '\n' + '  -------------------------'

#output .txt file
print(output)
with open(txt_file,'w') as outputfile:
        outputfile.write(output)

