#KELOMPOK15
#IF4407
#AILAL,ERIC,REZI

import streamlit as st

st.write("""
#Tugas Besar Teori Bahasa dan Automata
Web sederhana ini adalah implementasi untuk program parse yang kami buat.
Perkenelakan kami dari kelompok 15
Terdiri dari:
AILAL HAMDI BASRI
ERIC DEO ALAMSYAH
MUHAMMAD FACHREZI
""")

#input
sentence = st.text_input('input kalimat :')
tokens = sentence.lower().split()
tokens.append('EOS')

#symbol
non_terminals = ['S','NN','VB']
terminals = ['simbuk','bibik','labeng','sogo','sabhe','kembeng','nannem','nerseken',
             'dheker','ghibe']

#parse table
parse_table ={}

parse_table[('S', 'simbuk')] = ['NN','VB','NN']
parse_table[('S', 'bibik')] = ['NN','VB','NN']
parse_table[('S', 'labeng')] = ['NN','VB','NN']
parse_table[('S', 'sogo')] = ['NN','VB','NN']
parse_table[('S', 'sabhe')] = ['NN','VB','NN']
parse_table[('S', 'kembeng')] = ['NN','VB','NN']
parse_table[('S', 'nannem')] = ['error']
parse_table[('S', 'nerseken')] = ['error']
parse_table[('S', 'dheker')] = ['error']
parse_table[('S', 'ghibe')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'simbuk')] = ['simbuk']
parse_table[('NN', 'bibik')] = ['bibik']
parse_table[('NN', 'labeng')] = ['labeng']
parse_table[('NN', 'sogo')] = ['sogo']
parse_table[('NN', 'sabhe')] = ['sabhe']
parse_table[('NN', 'kembeng')] = ['kembeng']
parse_table[('NN', 'nannem')] = ['error']
parse_table[('NN', 'nerseken')] = ['error']
parse_table[('NN', 'dheker')] = ['error']
parse_table[('NN', 'ghibe')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'simbuk')] = ['error']
parse_table[('VB', 'bibik')] = ['error']
parse_table[('VB', 'labeng')] = ['error']
parse_table[('VB', 'sogo')] = ['error']
parse_table[('VB', 'sabhe')] = ['error']
parse_table[('VB', 'kembeng')] = ['error']
parse_table[('VB', 'nannem')] = ['nannem']
parse_table[('VB', 'nerseken')] = ['nerseken']
parse_table[('VB', 'dheker')] = ['dheker']
parse_table[('VB', 'ghibe')] = ['ghibe']
parse_table[('NN', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]

# parsing process
while (len(stack) > 0):
    top = stack [len(stack) - 1]
    st.write('top = ', top)
    st.write('symbol = ', symbol)
    if top in terminals:
        st.write('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                st.write('isi stack: ', stack)
                stack.pop()

        else:
            st.write('error')
            break;
    elif top in non_terminals:
        st.write('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            st.write('error')
            break;
    else:
        st.write('error')
        break;
    st.write('isi stack: ', stack)
    st.write()

# conclusion
st.write()
if symbol == 'EOS' and len(stack) == 0:
    st.write('Inputan kata/kalimat -->:',sentence,'-->diterima,sesuai dengan grammar')
else:
    st.write('Error,inputan kata/kalimat -->:',sentence,',-->tidak diterima,tidak sesuai dengan grammar')

