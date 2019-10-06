import re
import sys

REGEX = re.compile(r'=([^,]+),?')

if __name__ == "__main__":
    print('id;name;frags;owned;trail_size')
    
    filepath = sys.argv[1]
    with open(filepath) as fp:
        for line in fp.readlines():
            if 'player' not in line:
                continue
            
            elements = REGEX.findall(line.strip())
            print(';'.join(elements))
                        