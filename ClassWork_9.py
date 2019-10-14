# Input and Output

# Ex:1
my_int1 = 1
my_int2 = 2
my_int3 = 3

out_put_file = open('OutputFile.txt', 'w')

out_put_file.write(str(my_int1))
out_put_file.write(str(my_int2))
out_put_file.write(str(my_int3))

out_put_file.close()

# Ex:2
my_ints_list = ['Jirayr', 'Jirayr', 'Jirayr', 'Jirayr']

out_put_file = open('OutputFile_1.txt', 'a')
for i in range(len(my_ints_list)):
	my_ints_list[i] += '\n'

out_put_file.writelines(my_ints_list)

out_put_file.close()

# Ex:3
my_ints_list = ['Jirayr', 'Jirayr', 'Jirayr', 'Jirayr']

out_put_file = open('OutputFile_1.txt', 'r')

print(out_put_file.readline())
print(out_put_file.readline())

for line in out_put_file:

out_put_file.close()

# Ex:4
names_list = []
out_put_file = open('OutputFile_1.txt', 'r')

for line in out_put_file:
	names_list.append(line)

out_put_file.close()

print(names_list)