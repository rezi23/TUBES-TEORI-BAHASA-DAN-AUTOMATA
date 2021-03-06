#KELOMPOK15
#IF4407
#AILAL,ERIC,REZI

import streamlit as st
import string

st.write("""
#Tugas Besar Teori Bahasa dan Automata
Web sederhana ini adalah implementasi untuk program lexicalanalyzer yang kami buat
Perkenelakan kami dari kelompok 15
Terdiri dari:
AILAL HAMDI BASRI
ERIC DEO ALAMSYAH
MUHAMMAD FACHREZI
""")

# input example
sentence = st.text_input('input kata/kalimat : ')
st.text_input_string = sentence.lower()+'#'

#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
              'q41', 'q42', 'q43', 'q44']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# space before input string
transition_table['q0', ' '] = 'q0'

#kata: simbuk(nenek)
transition_table[('q0', 's')] = 'q1'
transition_table[('q1', 'i')] = 'q2'
transition_table[('q2', 'm')] = 'q3'
transition_table[('q3', 'b')] = 'q4'
transition_table[('q4', 'u')] = 'q5'
transition_table[('q5', 'k')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : sabhe(rumput)
transition_table[('q0', 's')] = 'q1'
transition_table[('q1', 'a')] = 'q6'
transition_table[('q6', 'b')] = 'q7'
transition_table[('q7', 'h')] = 'q8'
transition_table[('q8', 'e')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : sogo(nasi)
transition_table[('q0', 's')] = 'q1'
transition_table[('q1', 'o')] = 'q9'
transition_table[('q9', 'g')] = 'q10'
transition_table[('q10', 'o')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : labeng(pintu)
transition_table[('q0', 'l')] = 'q11'
transition_table[('q11', 'a')] = 'q12'
transition_table[('q12', 'b')] = 'q13'
transition_table[('q13', 'e')] = 'q14'
transition_table[('q14', 'n')] = 'q15'
transition_table[('q15', 'g')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata: kembeng(bunga)
transition_table[('q0', 'k')] = 'q16'
transition_table[('q16', 'e')] = 'q17'
transition_table[('q17', 'm')] = 'q18'
transition_table[('q18', 'b')] = 'q13'
transition_table[('q13', 'e')] = 'q14'
transition_table[('q14', 'n')] = 'q15'
transition_table[('q15', 'g')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata: bibik(bibi)
transition_table[('q0', 'b')] = 'q19'
transition_table[('q19', 'i')] = 'q20'
transition_table[('q20', 'b')] = 'q21'
transition_table[('q21', 'i')] = 'q22'
transition_table[('q22', 'k')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : nannem(menanam)
transition_table[('q0', 'n')] = 'q23'
transition_table[('q23', 'a')] = 'q24'
transition_table[('q24', 'n')] = 'q25'
transition_table[('q25', 'n')] = 'q26'
transition_table[('q26', 'e')] = 'q27'
transition_table[('q27', 'm')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : nerseken(membersihkan)
transition_table[('q0', 'n')] = 'q23'
transition_table[('q23', 'e')] = 'q28'
transition_table[('q28', 'r')] = 'q29'
transition_table[('q29', 's')] = 'q30'
transition_table[('q30', 'e')] = 'q31'
transition_table[('q31', 'k')] = 'q32'
transition_table[('q32', 'e')] = 'q33'
transition_table[('q33', 'n')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : dheker(makan)
transition_table[('q0', 'd')] = 'q34'
transition_table[('q34', 'h')] = 'q35'
transition_table[('q35', 'e')] = 'q36'
transition_table[('q36', 'k')] = 'q37'
transition_table[('q37', 'e')] = 'q38'
transition_table[('q38', 'r')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

#kata : ghibe(mencari)
transition_table[('q0', 'g')] = 'q39'
transition_table[('q39', 'h')] = 'q40'
transition_table[('q40', 'i')] = 'q41'
transition_table[('q41', 'b')] = 'q42'
transition_table[('q42', 'e')] = 'q43'
transition_table[('q43', '#')] = 'accept'
transition_table[('q43', ' ')] = 'q44'
transition_table[('q44', '#')] = 'accept'

# transition for new kata/kalimat
transition_table[('q44', 's')] = 'q1'
transition_table[('q44', 'l')] = 'q11'
transition_table[('q44', 'k')] = 'q16'
transition_table[('q44', 'b')] = 'q19'
transition_table[('q44', 'n')] = 'q23'
transition_table[('q44', 'd')] = 'q34'
transition_table[('q44', 'g')] = 'q39'

# lexical analysis
idx_char = 0
state = 'q0'
current_katakalimat = ''
while state != 'accept':
    current_char = st.text_input_string[idx_char]
    current_katakalimat += current_char
    state = transition_table[(state, current_char)]
    if state == 'q43':
        st.write('current kata: ', current_katakalimat, ', valid')
        current_katakalimat = ''
    if state == 'error':
        st.write('error, kata/kalimat tidak valid')
        break;
    idx_char = idx_char + 1


# conclusion
if state == 'accept':
    st.write('semua kata/kalimat di input: ', sentence, ', valid')
