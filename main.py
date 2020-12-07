# This is a sample Python script.
import os
import random


def print_hi():
    print(f'Hi, this program generates files using SELAM')  # Press Ctrl+F8 to toggle the breakpoint.


def input_files_num():
    """
    :return: number of files to generate
    """
    print('Please enter number of files to generate ')
    name = int(input())
    return name


def input_selection():
    """

    :return: number between 0 and 1
    """
    print('Please enter place for selection (number between 0 and 1)')
    number = float(input())
    return number


def generating_files():
    files_num = input_files_num()
    select_place = input_selection()
    curr_dir = os.getcwd()
    final_dir = os.path.join(curr_dir, 'files_folder')
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)
    os.system('mv selection.txt output.txt demography.txt files_folder; cd files_folder;')
    for files in range(files_num):
        final_num_1 = random.uniform(0, 1)
        final_num_2 = random.uniform(0, 1)
        final_num_3 = random.uniform(0, 1)
        file = open('selection.txt', 'w')
        file.write('S F\t0' + '\t' + str(select_place) + '\t' + str(final_num_1) + ' ' + str(final_num_2) + ' ' + str(final_num_3))
        file.close()
        cmd_selam = 'SELAM -d demography.txt -o output.txt -s selection.txt -h'
        os.system(cmd_selam)
        cmd_selam_stats = ''
        # os.system(echo "S	F	0	"$1"	"$final_num_1"	"$final_num_2"	"$final_num_3 > selection.txt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    generating_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
