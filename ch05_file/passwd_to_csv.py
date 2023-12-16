#%%
import csv
def passwd_to_csv(passwd_filename,csv_filename) :
    
    with open(passwd_filename,'r') as passwd, open(csv_filename,'w',newline='') as output :
        infile = csv.reader(passwd,delimiter=':')
        outfile = csv.writer(output,delimiter='\t')
        for record in infile :
            if(len(record)>1):
                outfile.writerow((record[0],record[2]))
                
    

# %%
import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as passwd, open(csv_filename, 'w', newline='') as csv_file:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(csv_file, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))
# %%
