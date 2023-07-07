matches = ['esp.', 'e.g.', '+', 'season', 'taste', 'weight', 'volume', 'tips',
           'botanical']



def remove_extra_spaces(file_path, output_file_path):

    cleaned_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line is not '\n':
                cleaned_lines.append(line)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in cleaned_lines:
            #print(line)
            output_file.write((line
                .replace('<strong>', '')
                .replace('</strong>', '')))
            

    print("Cleaned content has been written to", output_file_path)


file_path = 'C:/Users/zmigliorini/fb_wdir/a.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/a_cleaned.html'
remove_extra_spaces(file_path, output_file_path)
