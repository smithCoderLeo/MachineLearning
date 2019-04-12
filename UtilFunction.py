#data原始数据转为csv
def data2Csv(filename):
    handled_file = 'kdd99_handled.csv'
    data_to_file = open(handled_file, 'w', newline='')
    with open(filename, 'r') as fr: #读入的file为原始data文件
        csv_reader = csv.reader(fr)
        csv_writer = csv.writer(data_to_file)
        for each_line in csv_reader:
            temp_line = np.array(each_line) #转换类型
            csv_writer.writerow(temp_line)
    data_to_file.close()
    return handled_file
