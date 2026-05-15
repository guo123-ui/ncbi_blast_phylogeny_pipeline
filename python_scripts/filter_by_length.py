import sys
def filter_by_length(input_file,min_len,output_file):
    current_len = 0
    current_seq =[]
    with open(input_file,'r') as f_in, open(output_file,'w') as f_out:
        for line in f_in:
            line = line.rstrip('\n')
            if line.startswith(">"):
                if current_len >= min_len and current_seq:
                    for l in current_seq:
                        f_out.write(l + '\n')
                current_len = 0
                current_seq =[line]
            else:
                current_len += len(line)
                current_seq.append(line)
        if current_len >= min_len and current_seq:
            for l in current_seq:
                f_out.write(l + '\n')
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("yongfa")
        sys.exit(1)
    min_len = int(sys.argv[2])
    filter_by_length(sys.argv[1],min_len,sys.argv[3])



    
    

            





