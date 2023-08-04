##matches = ['esp.', 'e.g.', '+', 'season:', 'taste:', 'weight:', 'volume:', 'tips:', 'techniques:',
##           'botanical', 'dishes', 'class=\"exts\"', 'class=\"ext', 'class=\"p1\"', 'class=\"ca\"',
##           'affinities', 'class=\"bl\">', 'class=\"sb\">', 'class=\"ca3\">' 'class=\"h4\">',
##           'function:', '<hr />', 'class=\"img\"', 'class=\"ca3\"', '<p>', 'class=\"sbh\"',
##           'class=\"sbtx1\"', 'class=\"bl']
##
##
##
##def remove_extra_spaces(file_path, output_file_path):
##
##    cleaned_lines = []
##    
##    with open(file_path, 'r', encoding='utf-8') as file:
##        lines = file.readlines()
##        for line in lines:
##            if line != '\n':
##                cleaned_lines.append(line)
##
##    with open(output_file_path, 'w', encoding='utf-8') as output_file:
##        for line in cleaned_lines:
##            #print(line)
##            line = line.lower()
##            if any([x in line for x in matches]):
##                #print(line)
##                continue
##            line = line.replace('<strong>', '').replace('</strong>', '')
##            line = line.replace('1hl', 'lh1')
##            line = line.replace('l1h', 'lh1').replace('1lh', 'lh1')
##            line = line.replace('h1l', 'lh1').replace('hl1', 'lh1')
##
##            output_file.write(line)
##
##
##
##matches_two = ['cuisine', 'cuisines']
##         
##def remove_some_text(file_path, output_file_path):
##    
##    with open(file_path, 'r', encoding='utf-8') as file:
##        lines = file.readlines()
##
##    with open(output_file_path, 'w', encoding='utf-8') as output_file:
##        for line in lines:
##            if any([x in line for x in matches_two]):
##                continue
##            output_file.write(line)
##
##
##    print("Cleaned content has been written to", output_file_path)
##
##
##
##
##def remove_tags(file_path, output_file_path):
##    
##    with open(file_path, 'r', encoding='utf-8') as file:
##        lines = file.readlines()
##
##    with open(output_file_path, 'w', encoding='utf-8') as output_file:
##        for line in lines:
##            line = line.replace('<p class="lh1">', '*')
##            line = line.replace('<p class="ul">', '')
##            line = line.replace('</p>', '')
##            output_file.write(line)
##
##
##    print("Cleaned content has been written to", output_file_path)
##
##
##def expand_punc(file_path, output_file_path):
##    with open(file_path, 'r', encoding='utf-8') as file:
##        lines = file.readlines()
##    
##        
    
##    with open(output_file_path, 'w', encoding='utf-8') as output_file:
##        for line in lines:
##            if 'cheese:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('cheese: ', '').strip()
##                    newtokens.append(token + ' cheese\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'vinegar:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('vinegar: ', '').strip()
##                    newtokens.append(token + ' vinegar\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'oil:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('oil: ', '').strip()
##                    newtokens.append(token + ' oil\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'chile peppers:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('chile peppers: ', '').strip()
##                    newtokens.append(token + ' chile peppers\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'pepper:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('pepper: ', '').strip()
##                    newtokens.append(token + ' peppercorns\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'wine:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('wine: ', '').strip()
##                    newtokens.append(token + ' wine\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'beans:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('beans: ', '').strip()
##                    newtokens.append(token + ' beans\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'stocks:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('stocks: ', '').strip()
##                    newtokens.append(token + ' stock\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'sauce:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('sauce: ', '').strip()
##                    newtokens.append(token + ' sauce\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            if 'mushrooms:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('mushrooms: ', '').strip()
##                    newtokens.append(token + ' mushrooms\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'salads:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('salads: ', '').strip()
##                    newtokens.append(token + ' salads\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'salt:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('salt: ', '').strip()
##                    newtokens.append(token + ' salt\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'bell peppers:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('bell peppers: ', '').strip()
##                    newtokens.append(token + ' bell peppers\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'lemon:' in line:
##                output_file.write('lemons\n')
##            elif 'lime:' in line:
##                output_file.write('limes\n')
##            if 'sugar:' in line:
##                output_file.write('sugar\n')
##            elif 'chocolate:' in line:
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.replace('chocolate: ', '').strip()
##                    newtokens.append(token + ' chocolate\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif ':' in line:
##                tokens = line.split(':')
##                output_file.write(tokens[0] + '\n')
##            if 'beans,' in line:
##                line = line.replace('beans,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' beans\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'salt,' in line:
##                line = line.replace('salt,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' salt\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'vinegar,' in line:
##                line = line.replace('vinegar,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' vinegar\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'chocolate,' in line:
##                line = line.replace('chocolate,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' chocolate\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'stock,' in line:
##                line = line.replace('stock,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' stock\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'cheese,' in line:
##                line = line.replace('cheese,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' cheese\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'chile peppers,' in line:
##                line = line.replace('chile peppers,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' chile peppers\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'pepper,' in line:
##                line = line.replace('pepper,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' peppercorns\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'bell peppers,' in line:
##                line = line.replace('bell peppers,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' bell peppers\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            if 'peppers, piquillo' in line:
##                output_file.write('piquillo peppers\n')
##            elif 'lemon,' in line:
##                output_file.write('lemons\n')
##            elif 'lime,' in line:
##                output_file.write('limes\n')
##            elif 'orange,' in line:
##                output_file.write('oranges\n')
##            if 'mushrooms,' in line:
##                line = line.replace('mushrooms,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' mushrooms\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'wine,' in line:
##                line = line.replace('wine,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' wine\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif 'fish sauce,' in line:
##                output_file.write('fish sauce')
##            elif 'sauce,' in line:
##                line = line.replace('sauce,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' sauce\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            if 'sauces,' in line:
##                line = line.replace('sauces,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' sauces\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            if 'oil,' in line:
##                line = line.replace('oil,', '')
##                newtokens = []
##                tokens = line.split(',')
##                for token in tokens:
##                    token = token.strip()
##                    newtokens.append(token + ' oil\n')
##                print(newtokens)
##                for token in newtokens:
##                    output_file.write(token)
##            elif ',' in line:
##                tokens = line.split(',')
##                output_file.write(tokens[0] + '\n')
##            else:
##            output_file.write(line)

    #print("Cleaned content has been written to", output_file_path)




##def combine_all():
##    all_lines = []
##    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'm', 'n', 'q', 's', 't']
##    for letter in letters:
##        input_path = 'C:/Users/zmigliorini/fb_wdir/manual/{0}_cleaned_man.html'.format(letter)
##    
##        with open(input_path, 'r', encoding='utf-8') as file:
##            lines = file.readlines()
##            for line in lines:
##                all_lines.append(line.strip())
##
##    with open('C:/Users/zmigliorini/fb_wdir/manual/all_lines.txt', 'w', encoding='utf-8') as file:
##        for line in all_lines:
##            file.write(line + '\n')


##def create_csv():
##
##    all_pairs = {}
##    key = ''
##    values = []
##    
##    with open('C:/Users/zmigliorini/fb_wdir/manual/all_lines.txt', 'r', encoding='utf-8') as file_in:
##        lines = file_in.readlines()
##
####        keys_compare = []
####        
####        for line in lines:
####            if '*' in line:
####                keys_compare.append(line.replace('*', '').strip())
##                
##        for line in lines:
##            if '*' in line:
##                if key in all_pairs:
##                    print('Unexpected dupe ' + key)
##                else:
##                    all_pairs[key] = values
##                    key = line.replace('*', '').strip()
##                values = []
##            else:
##                if line.strip() not in values:
##                    values.append(line.strip())
##
##
##    
##    all_keys = sorted(all_pairs)
##
##    with open('C:/Users/zmigliorini/fb_wdir/csv/relationships.csv', 'w', encoding='utf-8') as file_out:
##        file_out.write('foodA,foodB\n')
##        for cur_key in all_keys:
##            cur_values = all_pairs[cur_key]
##            for val in cur_values:
##                file_out.write('{0},{1}\n'.format(cur_key.strip(), val.strip()))
##        
##
##
####    for cur_key in all_keys:
####        cur_values = all_pairs[cur_key]
####        with open('C:/Users/zmigliorini/fb_wdir/csv/{0}.csv'.format(cur_key.strip()), 'w', encoding='utf-8') as file_out:
####            file_out.write('foodA,foodB\n')
####            for val in cur_values:
####                file_out.write('{0},{1}\n'.format(cur_key.strip(), val.strip()))
##        
####        print('In dict only\n')
####        for k in list(all_pairs):
####            if k not in keys_compare:
####                print(k)
####        print('\n\n\nNot in dict')
####        for k in keys_compare:
####            if k not in list(all_pairs):
####                print(k)
##        
##    #print(sorted(all_pairs))
##        
##create_csv()


with open('C:/Users/zmigliorini/fb_wdir/csv/relationships.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    occurances = set()
    for line in lines:
        if 'chestnuts' in line:
            tup = line.split(',')
            tup[0] = tup[0].strip()
            tup[1] = tup[1].strip()
            if (tup[0], tup[1]) in occurances or (tup[1], tup[0]) in occurances:
                continue
            else:
                occurances.add((tup[0], tup[1]))
    for occ in occurances:
        print(occ)
        print('\n')
    print(len(occurances))

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
##file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
##output_file_path = 'C:/Users/zmigliorini/fb_wdir/manual/t_cleaned_man.html'
##expand_punc(file_path, output_file_path)
