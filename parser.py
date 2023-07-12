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
            

    print("Cleaned content has been written to", output_file_path)


##file_path = 'C:/Users/zmigliorini/fb_wdir/a.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/a_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/b.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/b_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/c.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/c_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/d.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/d_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/e.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/e_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/f.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/f_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/g.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/g_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/h.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/h_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/i.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/i_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/j.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/j_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/m.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/m_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/n.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/n_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/q.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/q_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/s.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/s_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/t.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/t_cleaned.html'
##remove_extra_spaces(file_path, output_file_path)