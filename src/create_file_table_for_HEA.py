import os
import sys
path = sys.argv[1]

project = "HEA"
output = project + "_info.txt"
#get list of files in a directory
fnames = os.listdir(path)

#parse file names
def parse_file_name(file_name):
    result_hash={}
    ss = file_name.split(".")
    result_hash["lab_id"] = ss[0]
    result_hash["tissue_id"] = ss[1]
    result_hash["mark_id"] = ss[2]
    result_hash["sample_id"] = ".".join(ss[3:(len(ss)-1)])
    return(result_hash)
fout = open(output, "w")
for fname in fnames:
    r_hash = parse_file_name(fname)
    fout.write("%s\tproject=%s; "\
                "cell=%s; antibody=%s; lab=%s; "\
                "replicate=%s\n"%(fname, project, 
                                r_hash["tissue_id"], r_hash["mark_id"],
                                r_hash["lab_id"], r_hash["sample_id"]))
fout.close()    
