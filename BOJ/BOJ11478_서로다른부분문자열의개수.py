string = input()
N = len(string)
string+=" "

sub_list = []
for length in range(1,N+1):
    for i in range(N+1-length):
        sub_string = string[i:i+length]
        sub_list.append(sub_string)

sub_set = set(sub_list)
print(len(sub_set))