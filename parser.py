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


def expand_punc(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
        
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            if 'cheese:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('cheese: ', '').strip()
                    newtokens.append(token + ' cheese\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'vinegar:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('vinegar: ', '').strip()
                    newtokens.append(token + ' vinegar\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'oil:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('oil: ', '').strip()
                    newtokens.append(token + ' oil\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'chile peppers:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('chile peppers: ', '').strip()
                    newtokens.append(token + ' chile peppers\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'pepper:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('pepper: ', '').strip()
                    newtokens.append(token + ' peppercorns\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'wine:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('wine: ', '').strip()
                    newtokens.append(token + ' wine\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'beans:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('beans: ', '').strip()
                    newtokens.append(token + ' beans\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'stocks:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('stocks: ', '').strip()
                    newtokens.append(token + ' stock\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            elif 'sauce:' in line:
                newtokens = []
                tokens = line.split(',')
                for token in tokens:
                    token = token.replace('sauce: ', '').strip()
                    newtokens.append(token + ' sauce\n')
                print(newtokens)
                for token in newtokens:
                    output_file.write(token)
            else:
                output_file.write(line)

    print("Cleaned content has been written to", output_file_path)
    



##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/a_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/a_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/b_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/b_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/c_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/c_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/d_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/d_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/e_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/e_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/f_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/f_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/g_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/g_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/h_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/h_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/j_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/j_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/m_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/m_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/n_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/n_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/q_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/q_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/s_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/s_cleaned_man.html'
##expand_punc(file_path, output_file_path)
##
file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
expand_punc(file_path, output_file_path)
