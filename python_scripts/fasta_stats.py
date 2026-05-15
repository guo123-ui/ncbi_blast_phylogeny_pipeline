import sys
def fasta_stats(filename):
    current_len = 0
    seq_count = 0
    total_bases = 0
    max_len = 0
    min_len = float('inf')
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_len > 0:
                    seq_count += 1
                    total_bases += current_len
                    if current_len > max_len:
                        max_len = current_len
                    if current_len < min_len:
                        min_len = current_len
                current_len = 0
            else:
                current_len += len(line)
        if current_len > 0:
            seq_count += 1
            total_bases += current_len               
            if current_len > max_len:
                max_len = current_len
            if current_len < min_len:
                min_len = current_len
    if min_len == float('inf'):
        min_len = 0
    print(f"xuliezongshu:{seq_count}")
    print(f"jianjizongshu:{total_bases}")
    print(f"zuidaxuliechangdu:{max_len}")
    print(f"zuiduanxueliechangdu:{min_len}")
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("yongfa")

        sys.exit(1)
    fasta_stats(sys.argv[1])

















    
              
                    
    












