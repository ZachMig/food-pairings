matches = ['esp.', 'e.g.', '+', 'season:', 'taste:', 'weight:', 'volume:', 'tips:', 'techniques:',
           'botanical', 'dishes', 'class=\"exts\"', 'class=\"ext', 'class=\"p1\"', 'class=\"ca\"',
           'affinities', 'class=\"bl\">', 'class=\"sb\">', 'class=\"ca3\">' 'class=\"h4\">',
           'function:', '<hr />', 'class=\"img\"', 'class=\"ca3\"', '<p>', 'class=\"sbh\"',
           'class=\"sbtx1\"', 'class=\"bl']



def remove_extra_spaces(file_path, output_file_path):

    cleaned_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line != '\n':
                cleaned_lines.append(line)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in cleaned_lines:
            #print(line)
            line = line.lower()
            if any([x in line for x in matches]):
                #print(line)
                continue
            line = line.replace('<strong>', '').replace('</strong>', '')
            line = line.replace('1hl', 'lh1')
            line = line.replace('l1h', 'lh1').replace('1lh', 'lh1')
            line = line.replace('h1l', 'lh1').replace('hl1', 'lh1')

            output_file.write(line)



matches_two = ['cuisine', 'cuisines']
         
def remove_some_text(file_path, output_file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            if any([x in line for x in matches_two]):
                continue
            output_file.write(line)


    print("Cleaned content has been written to", output_file_path)




def remove_tags(file_path, output_file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            line = line.replace('<p class="lh1">', '*')
            line = line.replace('<p class="ul">', '')
            line = line.replace('</p>', '')
            output_file.write(line)


    print("Cleaned content has been written to", output_file_path)



file_path = 'C:/Users/zmigliorini/fb_wdir/manual/a_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/a_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/b_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/b_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/c_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/c_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/d_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/d_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/e_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/e_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/f_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/f_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/g_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/g_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/h_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/h_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/j_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/j_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/m_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/m_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/n_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/n_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/q_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/q_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/s_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/s_cleaned_man.html'
remove_tags(file_path, output_file_path)

file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
remove_tags(file_path, output_file_path)
